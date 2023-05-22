from introfamily import IntroFam
import sys
args = sys.argv


mike = IntroFam(args[1], args[2], args[3])
print(mike.name_out())
print(mike.age_out())
mike.cat_out()