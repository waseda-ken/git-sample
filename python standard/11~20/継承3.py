class HumanClass:
    def __init__(self):
        print('HumanClassのinit')
        self.HP=100

class WizardClass(HumanClass):
    def __init__(self):
        super().__init__()
        self.MP=50

wizard=WizardClass()
print(wizard.HP)
print(wizard.MP)