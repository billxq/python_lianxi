#! python

# 输入三个整数x,y,z，请把这三个数由小到大输出。

x = input("请输入x: ")
y = input("请输入y: ")
z = input("请输入z: ")

x = int(x)
y = int(y)
z = int(z)

lis = [x,y,z]
print(lis.sort())
