def start_end(func):
    def add_start_end(*args,**kwargs):
        print('start')
        x = func(*args, **kwargs)
        print('end')
        return x
    return add_start_end

@start_end
def add_exclamataion(text):
    print('add_exclamationが実行されました')
    return 'これはバナナですか？',text+'!'

result1,result2=add_exclamataion('これはリンゴです')
print(result1)
print(result2)