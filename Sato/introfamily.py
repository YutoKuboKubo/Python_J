import introduce

class IntroFam(introduce.Intro):
    def __init__(self, name, age,cat_name):
        super().__init__(name, age)
        self.cat_name = cat_name 

    def cat_out(self):
        cattxt = "飼い猫の名前は、" + str(self.cat_name) + "です"
        return cattxt