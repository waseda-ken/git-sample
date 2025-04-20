class HumanClass:
    def defend(self):
        print('防御しました')

class WizardClass(HumanClass):
    pass

wizard=WizardClass()
wizard.defend()