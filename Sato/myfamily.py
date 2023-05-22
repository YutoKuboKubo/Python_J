import introfamily
import sys

name = sys.argv[1]
age = sys.argv[2]
cat_name = sys.argv[3]

fam = introfamily.IntroFam(name,age)

print(fam.name_out())
print(fam.age_out())
print(fam.cat_out(cat_name))
