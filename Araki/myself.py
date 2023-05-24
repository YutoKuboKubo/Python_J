from introduce import Intro
import sys
args = sys.argv
name = "Araki" #args[1]
age = "23" #args[2]

me = Intro(name, age)
print(me.name_out())
print(me.age_out())