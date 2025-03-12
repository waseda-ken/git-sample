import json
obj = {'item':'apple','price':120}
json_text = json.dumps(obj)
print(json_text)
print(type(json_text))

obj1={'User':'サプー','fllower_ids':[11,13,14]}
json_text1=json.dumps(obj1,ensure_ascii=False)
print(json_text1)
print(type(json_text1))

text='{"id":123,"is_student":true}'
obj2=json.loads(text)
print(obj2)
print(type(obj2))
print(obj2['id'])

obj3={'it"em':'app\\le'}
json_text2=json.dumps(obj3)
print(json_text2)

text1=r'{"user\\_id":123,"na\"ma":"suupu"}'
obj4=json.loads(text1)
print(obj4)
print(obj4[r'user\_id'])