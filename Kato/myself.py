from intoroduce import Intro
import sys
args = sys.argv

takashi = Intro(args[1], args[2])
print(takashi.name_out())
print(takashi.age_out())