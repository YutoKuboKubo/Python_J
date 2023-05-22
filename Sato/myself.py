import sys
import introduce
args = sys.argv
name = args[1]
age = args[2]
human = introduce.Intro(name,age)
human.name_out()
human.age_out()

        