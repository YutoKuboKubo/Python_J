from introduce import Intro


class IntroFam(Intro):
    '''猫のクラス'''
    def __init__(self, name, age, cat_name):
        '''初期化'''
        super().__init__(name, age)
        self.cat_name = cat_name

    def cat_out(self):
        '''猫の名前を紹介'''
        return f"飼い猫の名前は、{self.cat_name}です"
