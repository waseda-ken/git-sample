x=[1,2,3]
print(len(x))
print(x[1])

x.append('a')
print(x)

x.remove('a')
print(x)

y=[4,5]
x.extend(y)
print(x)

z=x+y*3
print(z)

X=[1,2,3,4,5,6,7,8]
print(X[1:6])
print(X[:4])
print(X[4:])