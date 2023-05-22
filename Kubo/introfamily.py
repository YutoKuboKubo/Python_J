from introduce import Intro


class IntroFam(Intro):
    def __init__(self, cat_name):
        self.cat_name = cat_name

    def cat_out(self):
        return f"飼い猫の名前は、{self.cat_name}です"
