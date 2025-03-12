x=float('nan')
print(x+1)
print(x-2)
print(x*3)
print(x/4)

import math
x=float('nan')
y=float('nan')
print(x==y)
print(x is y)
print(math.isnan(x))

p_inf=float('inf')
m_inf=float('-inf')
print(p_inf==float('inf'))
print(m_inf==float('-inf'))

x=None
y=None
if x is None:
    print('xはNoneです')
print(id(x))
print(id(y))
if x:
    print('if文の中を通ります')
else:
    print('elseの中を通ります')