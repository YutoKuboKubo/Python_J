class Intro:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"私の名前は、{self.name}です\n年齢は、{self.age}歳です")


bob = Intro("Bob", "18")
bob.introduce()
