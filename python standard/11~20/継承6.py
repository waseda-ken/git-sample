class WizardClass:
    def __init__(self):
        self.HP=100
        self.MP=50
        print('WizardClassのinit')

    def cast_spell(self):
        print('呪文を唱える')


class SwordFighterClass:
    def attack_with_sword(self):
        print('剣で攻撃する')

class MagicSwordFighterClass(WizardClass,SwordFighterClass):
    def output_info(self):
        print(f'現在のHPは{self.HP}で、MPは{self.MP}です。')
msf=MagicSwordFighterClass()
msf.output_info()
msf.attack_with_sword()
msf.cast_spell()