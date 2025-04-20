x_list = [100,190,2980]
for x in x_list:
    x_yen=str(x)+'円'
    print(x_yen)

x_dict={'apple':100,'banana':350}
for key,value in x_dict.items():
    text = key + 'は' + str(value) + '円です'
    print(text)

for x in range(10):
    print(x)