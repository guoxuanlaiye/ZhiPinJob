from sql import Sql
import matplotlib.pyplot as plt

def main():

    x = [0,5,10,15,20,25,30,35,40,45,50]
    # y_ticks = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

    ret = Sql.select_jobs_minPay(city="成都", post="python")
    y = []
    for min_pay in ret:
        y.append(min_pay[0])

    plt.hist(y, bins=x, normed=1, histtype='bar', rwidth=0.8)
    plt.xlabel('pay(k)')
    plt.ylabel('y')
    plt.xticks(x)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()


# 去除重复的
# u_pays = set(pays)
# for p in u_pays:
#     print("p = {},count = {}".format(p, pays.count(p)))
