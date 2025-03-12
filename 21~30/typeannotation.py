def total_price_1item(unit_price, quantity=1):
    total_price=unit_price*quantity
    return total_price

total_price1=total_price_1item(120)
print(total_price1)

total_price2=total_price_1item(quantity=20,unit_price=130)
print(total_price2)

def total_price_2item(unit_price2:int, quantity2:int)->int:
    total_price3=unit_price2*quantity2
    return total_price3

total_price4=total_price_2item(130,3)
print(total_price4)

def total_price_3item(unit_price3:int, quantity3:int=1)->str:
    total_price5=unit_price3*quantity3
    return f'¥{total_price5:,}'

total_price6=total_price_3item(1300)
print(total_price6)