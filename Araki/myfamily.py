from introfamily import IntroFam

name = "Araki" #args[1]
age = "23" #args[2]
cat_name = "Tako" #args[3]

family = IntroFam(name,age)
print(family.name_out())
print(family.age_out())
print(family.cat_out(cat_name))
