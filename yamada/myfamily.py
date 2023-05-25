import yamada.introfamily as introfamily

import sys
args = sys.argv

my_name = args[1]
my_age = args[2]
my_cat = args[3]

me = introfamily.IntroFam(my_name, my_age, my_cat)
print(me.name_out())
print(me.age_out())
print(me.cat_out())