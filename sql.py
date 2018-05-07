import pymysql
from pymysql import DatabaseError

conn = pymysql.connect("localhost", "root", "", "test", use_unicode=True, charset="utf8")
cursor = conn.cursor()

class Sql(object):
    # 插入数据
    @classmethod
    def insert_jobs(cls, job_id, job_name, job_company, experience, job_pay, min_pay, max_pay):

        sql = "insert into jobs(job_id, job_name, job_company, experience, job_pay,min_pay,max_pay) values('%s', '%s', '%s', '%s', '%s', '%d', '%d');" % (job_id, job_name, job_company, experience, job_pay, min_pay, max_pay)
        try:
            cursor.execute(sql)
            conn.commit()
        except DatabaseError as dbError:
            print("insert_jobs dbError ==== %s" % dbError)
            conn.rollback()
    # 更新
    @classmethod
    def update_jobs(cls, job_id, job_name, job_company, experience, job_pay, min_pay, max_pay):

        sql = "update jobs set job_name='%s', job_company='%s', experience='%s', job_pay='%s', min_pay='%d', max_pay='%d' where job_id='%s';" % (job_name, job_company, experience, job_pay, min_pay, max_pay, job_id)
        try:
            cursor.execute(sql)
            conn.commit()
        except DatabaseError as dbError:
            print("update_jobs dbError ==== %s" % dbError)
            conn.rollback()

    # 查询
    @classmethod
    def select_jobs_jobid(cls,job_id):
        sql = "select * from jobs where job_id='%s'" % job_id
        cursor.execute(sql)
        ret = cursor.fetchall()
        if len(ret) == 0:
            return False
        return True

    @classmethod
    def select_jobs(cls):
        sql = "select * from jobs;"
        cursor.execute(sql)
        ret = cursor.fetchall()
        return ret

    @classmethod
    def select_jobs_pay(cls, city=None, post=None):
        sql = ""
        if not (city and post):
            sql = "select job_pay from jobs;"
        else:
            sql = "select job_pay from jobs where experience like '%{}%' and job_name like '%{}%'".format(city, post)
        cursor.execute(sql)
        ret = cursor.fetchall()
        return ret

    @classmethod
    def select_jobs_minPay(cls, city=None, post=None):
        sql = ""
        if not (city and post):
            sql = "select min_pay from jobs;"
        else:
            sql = "select min_pay from jobs where experience like '%{}%' and job_name like '%{}%'".format(city, post)
        cursor.execute(sql)
        ret = cursor.fetchall()
        return ret