x=[i+1000 for i in range(6)]
print(x)

names=['斎藤','山田','田中']
y=[i+'さん' for i in names]
print(y)

z = [i for i in range (11) if i%2==0]
print(z)

foods = ['apple','banana','lemon']
X=[i for i in foods if 'a' in i]
print(X)

Y1=[i for i in range(6)]
Y2=['ぐ' if i%2==0 else i for i in range(6)]
print(Y1)
print(Y2)

kanto=['千葉','栃木','東京','埼玉','茨城','群馬','神奈川']
Z=[i+'都'if i=='東京' else i + '県' for i in kanto]
print(Z)