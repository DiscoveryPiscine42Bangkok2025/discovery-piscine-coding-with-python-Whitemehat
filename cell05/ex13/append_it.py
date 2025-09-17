import sys

for i in sys.argv:
    if "ism" in i:
        continue
    else:
        print(f"{i}ism")