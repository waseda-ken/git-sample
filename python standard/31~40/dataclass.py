from dataclasses import dataclass

@dataclass
class User:
    name:str
    age:int
    
user=User('sato',20)
print(user.name)
print(user.age)

from dataclasses import dataclass,field

@dataclass
class User1:
    name:str
    age:int
    items:list[int]=field(default_factory=list)

user1=User1('supu',10)
print(user1.items)
print(user1)

from dataclasses import dataclass,field

@dataclass
class User2:
    name:str
    age:int
    items:list[int]=field(default_factory=lambda:['note','pen'])

user2=User2('supu',10)
print(user2)
print(user2.items)

class User3:
    def __init__(self,name,age):
        self.name=name
        self.age=age

user3=User3('supu',20)
user4=User3('supu',20)
print(user3==user4)

from dataclasses import dataclass

@dataclass(frozen=True)
class User4:
    name:str
    age:int

user5=User4('supu',20)
user6=User4('supu',20)
print(user5==user6)

import dataclasses

@dataclass(frozen=True)
class User5:
    name:str
    age:int

user7=User5('supu',20)
result=dataclasses.asdict(user7)
print(result)