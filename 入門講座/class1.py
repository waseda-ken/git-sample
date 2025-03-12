class Student:

    def __init__(self):
        self.name =""


    def avg(self,math,english):
        print((math+english)/2)

a001=Student()
a001.name="sato"
a001.avg(30,70)
print(a001.name)

a002=Student()
a002.name="tanaka"
a002.avg(80,90)
print(a002.name)