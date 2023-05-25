import yamada.introduce as introduce

import sys
args = sys.argv

my_name = args[1]
my_age = args[2]

me = introduce.Intro(my_name, my_age)
print(me.name_out())
print(me.age_out())