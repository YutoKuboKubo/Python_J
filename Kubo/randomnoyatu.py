import random
import string
a = random.sample(string.ascii_uppercase[:10], k=10)
for i, v in enumerate(a):
    print(f"{i+1}番目は、{v}チーム")