#! python

# 打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个“水仙花数”，因为153=1的三次方＋5的三次方＋3的三次方。
import itertools
res = itertools.product(range(1,10),range(10),range(10))
for i in res:
    a = i[0]*100+i[1]*10+i[2]
    b = i[0]**3+i[1]**3+i[2]**3
    if a == b:
        print(a)
