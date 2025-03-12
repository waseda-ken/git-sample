def price_format(x):
    return f'{x:,}円'

def shipping_fee(x):
    if x<12000:
        return x+500
    else:
        return x

def main():
    hand_bag=5000
    shoes=6000
    total=hand_bag+shoes
    print(total)
    total=shipping_fee(total)
    print(total)
    total=price_format(total)
    print(total)

if __name__=='__main__':
    main()