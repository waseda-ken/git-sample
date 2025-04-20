x={'リンゴ':120,'バナナ':300,'イチゴ':450}
print(x)

banana=x['バナナ']
print(banana)

x['トマト']=400
print(x)

x['イチゴ']=350
print(x)

y={'梨':150,'メロン':800}
x.update(y)
print(x)

z=x|y
Z=len(z)
print(z," ",Z)