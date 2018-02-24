#! python


# 题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？

import itertools
res = []
[res.append(i[0]*100 + i[1]*10 + i[2]) for i in itertools.permutations(range(1,5),3)]
print(res,len(res))
