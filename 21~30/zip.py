sales_2020=[400239,560213,542490]
sales_2019=[489028,400123,442489]

for current,previous in zip(sales_2020,sales_2019):
    result=(current/previous-1)*100
    print(f'{result:.1f}%')