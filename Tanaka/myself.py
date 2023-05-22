import sys
import introduce
args = sys.argv

#引数を変数に代入
name1 = args[1]
age1 = args[2]

myself = introduce.Intro(name1,age1)
print(myself.name_out())
print(myself.age_out())
