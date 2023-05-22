import introduce

class IntroFam(introduce.Intro):
    def cat_out(self,cat_name):
        cattxt = "飼い猫の名前は、" + str(cat_name) + "です"
        return cattxt