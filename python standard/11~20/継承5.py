class WizardClass:
    def __init__(self):
        print('WizardClassのinit')

class SwordFighterClass:
    def __init__(self):
        print('SwordFighterClassのinit')

class MagicSwordFighterClass(WizardClass,SwordFighterClass):
    pass

msf=MagicSwordFighterClass()