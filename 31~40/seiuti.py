x=list(range(10))
if(n:=len(x))>=10:
    print('このリストは長すぎます')
print(f'n;{n}')

with open('text.txt')as f:
    while(t:=f.readline())!='':
        print(t)

import re

s='合計金額は1200円です'
if (m:=re.search(r'[0-9]+円',s)):
    print(m.group())