import traceback

try:
    result=1/0
    print(result)
except ZeroDivisionError:
    print('--- トレースバックを出力開始 ---')
    t= traceback.format_exc()
    print(t)
    print('--- トレースバックを出力終了 ---')
