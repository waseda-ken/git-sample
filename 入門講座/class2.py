class Student:

    def __init__(self,i):
        self.name =i


    def avg(self,math,english):
        print((math+english)/2)

a001=Student("sato")
a001.avg(30,70)
print(a001.name)

a002=Student("tanaka")
a002.avg(80,90)
print(a002.name)