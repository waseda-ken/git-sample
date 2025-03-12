class HumanClass:
    def __init__(self):
        print('HumanClassのinit')
        self.HP=100

class WizardClass(HumanClass):
    pass

wizard=WizardClass()
print(wizard.HP)