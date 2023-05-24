from introduce import Intro

class IntroFam(Intro):
    def __init__(self, name, age, cat):
        self.name = name
        self.age = age
        self.cat = cat

    def cat_out(self):
        print("飼い猫の名前は、" + self.cat + "です")