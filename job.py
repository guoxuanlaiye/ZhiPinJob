import ssl
from urllib import request
from bs4 import BeautifulSoup
from sql import Sql


ssl._create_default_https_context = ssl._create_unverified_context

def getHtmlData(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    req = request.Request(url, headers=headers)
    resp = request.urlopen(req)
    htmldata = resp.read()
    return htmldata

def getJobList(htmldata):
    soup = BeautifulSoup(htmldata, 'html.parser')
    jobs = soup.find_all('div', class_='job-primary')
    names = []
    for job in jobs:

        name = {}
        info = job.find('div', class_="info-primary").find_next('p').get_text()
        job_id = job.find('div', class_="info-primary").find_next('h3').find_next('a')['data-jobid']
        job_pay = job.find('span', class_='red').get_text()
        name["job_name"] = job.find('div', class_='job-title').get_text()
        name["job_company"] = job.find('div', class_='info-company').find_next('a').get_text()
        name["experience"] = info
        name["job_pay"] = job_pay
        name["job_id"] = job_id
        pay_str = job_pay.replace('k', '').split('-')
        name["min_pay"] = int(pay_str[0])
        name["max_pay"] = int(pay_str[1])
        names.append(name)
    return names

def getData(city_code=None, post_code=None):

    print("###### begin crawl....")

    for index in range(1, 11):
        url = "https://www.zhipin.com/c{}-p{}/h_{}/?page={}&ka=page-next".format(city_code, post_code, city_code,index)
        htmldata = getHtmlData(url)
        jobs = getJobList(htmldata)
        print("###### crawl url ===== {}".format(url))
        if len(jobs) != 0:

            for job in jobs:
                isExistJob = Sql.select_jobs_jobid(job["job_id"])
                if isExistJob == True:
                    Sql.update_jobs(job["job_id"], job["job_name"], job["job_company"], job["experience"], job["job_pay"], job["min_pay"], job["max_pay"])
                else:
                    Sql.insert_jobs(job["job_id"], job["job_name"], job["job_company"], job["experience"], job["job_pay"], job["min_pay"], job["max_pay"])

    print("###### finish crawl....")





if __name__ == '__main__':
    getData(city_code="101010100", post_code="100109")