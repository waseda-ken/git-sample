x=0
while x<=10:
    x+=1
    if x%7==0:
        continue
    print('whileの最終行')
    print(f'1を加算した後のxは {x}')

while x<=11:
    x+=1
    print(x)
    if x%5==0:
        break

with open('text.txt')as f:
    t=f.readline()
    while t!='':
        print(t)
        t=f.readline()