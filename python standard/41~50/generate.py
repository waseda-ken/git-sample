def my_generator():
    x=10
    yield x
    x=x+10
    yield x
    x=x+10
    yield x

mg = my_generator()
for x in mg:
    print(x)

print(dir(mg))