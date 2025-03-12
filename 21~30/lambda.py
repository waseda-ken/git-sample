func=lambda X,Y:print(f'{X}さんは{Y}です')
func('鈴木','学生')

names = ['鈴木','斎藤','田中']
result=list(map(lambda x:x+'さん',names))
print(result)

n1=['鈴木','斎藤','田中']
n2=['めい','ゆづき','ひなた']
result2=list(map(lambda x, y: x+y+'さん',n1,n2))
print(result2)

numbers=[5,8,10,12,30]
result3=list(filter(lambda x:x>=10,numbers))
print(result3)