#自己紹介のクラス
class Intro:
    #初期化
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #自分の名前を紹介する
    def name_out(self):
        name_txt = "わたしの名前は、" + self.name + "です"
        return name_txt
    #自分の年齢を紹介する
    def age_out(self):
        age_txt = "年齢は、" + self.age + "歳です"
        return age_txt
        