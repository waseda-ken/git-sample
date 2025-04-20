def start_end(func):
    def add_start_end():
        print('start')
        func()
        print('end')
    return add_start_end

def print_apple():
    print('これはリンゴです')

    start_end(print_apple)()
    #func=start_end(print_apple)
    #func()

#@start_end
#def print_apple():
    #print('これはリンゴです')
#print_apple()