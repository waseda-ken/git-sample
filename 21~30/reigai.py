x=1
y=0
try:
    result1=x/y
except ZeroDivisionError:
    print('ゼロでは割れません')

try:
    result2=x/y
except ZeroDivisionError as e:
    print('ゼロでは割ることができません')
    print(e)
except NameError as e:
    print('定数が定義されていません')
    print(e)
else:
    print(result2)
    print('正常に終了しました')
finally:
    print('割り算を終了しました')