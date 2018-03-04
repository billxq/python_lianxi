#! python
# 计算100以内能被3整除的正整数之和

sum=0
i=1

while i<=100:
    if i%3==0:
        sum=sum+i
    i+=1
print(sum)
