import re
s='090333'
m=re.match(r'[0-9]{3}',s)
print(m)
if m:
    print(m.group())
    print(m.span())

S='bananaは¥300です'
M=re.search(r'¥[1-9][0-9]*',S)
print(M)
if M:
    print(m.group())
    print(m.span())
    print(m.end())

s1='この洋服は$100です'
m1=re.search(r'\$[0-9]+',s1)
print(m1)
if m1:
    print(m.group())
    print(m.span())