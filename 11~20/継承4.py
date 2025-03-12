class HumanClass:
    def __init__(self):
        print('HumanClassのinit')
        self.HP=100

class WizardClass(HumanClass):
    def __init__(self):
        super().__init__()
        self.MP=50

    def output_info(self):
        print(f'現在のHPは{self.HP}で、MPは{self.MP}です。')

wizard=WizardClass()
wizard.output_info()