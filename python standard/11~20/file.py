with open('text.txt') as f:
    for _ in range(4):
        s_line=f.readline()
        print(s_line)
        if s_line=='':
            print('終了です')

with open('text.txt') as f:
    s=f.read()
    print(s)
    
with open('text.txt') as f:
    s_line2=f.readlines()
    print(s_line2)

with open('text.txt2','w') as f:
    f.write('ddd\neee\nooo')

x_list=['apple','orange', 'banana']
s2='\n'.join(x_list)
with open('text.txt3','w') as f:
    f.write(s2)