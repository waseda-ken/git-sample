def div(num1,num2,num3):
    return((num1+num2+num3)/3)

i=div(9,4,2)
print(i)


def div(num1,num2,num3):
    arr=[0,1,2]
    sum=0
    for i in arr:
        sum+=i
    return((num1+num2+num3)/sum)
j=div(9,4,2)
print(j)