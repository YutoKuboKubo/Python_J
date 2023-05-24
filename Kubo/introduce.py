class Intro:
    '''自己紹介するクラス'''
    def __init__(self, name, age):
        '''初期化'''
        self.name = name
        self.age = age

    def name_out(self):
        '''自分の名前を紹介する'''
        nametxt = f"私の名前は、{self.name}です"
        return nametxt

    def age_out(self):
        '''自分の年齢を紹介する'''
        agetxt = f"年齢は、{self.age}歳です"
        return agetxt
