import sys
import introduce
import introfamily
args = sys.argv

#引数を変数に代入
name = args[1]
age = args[2]
cat = args[3]

IntroMyFam = introfamily.IntroFam(name, age, cat)
print(IntroMyFam.name_out())
print(IntroMyFam.age_out())
print(IntroMyFam.cat_out())
