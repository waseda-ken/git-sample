x_set={11,222,333}

y_list =[11,333,444,555,11]
y_set=set(y_list)

result1=x_set&y_set
result2=x_set-y_set
result3=x_set|y_set

print(x_set)
print(y_set)
print(result1)
print(result2)
print(result3)

x_tuple=(1,3,5)
y_list=[3,4,5]
y_tuple=tuple(y_list)
result4=x_tuple[2]
result5=x_tuple+y_tuple
print(result4,',',result5)

def test_function():
    x=2*2
    y=3*3
    return x,y

result6,result7=test_function()
result8=test_function()
print(result6,result7)
print(result8)

x_dict={'a':100, 'b':200, 'c':300}
for X in x_dict.items():
    print(X)
for (Y,Z) in x_dict.items():
    print(Y)
    print(Z)