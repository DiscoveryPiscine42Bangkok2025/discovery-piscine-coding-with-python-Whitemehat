import sys

if len(sys.argv) < 2:
    print("none")
else:
    text = sys.argv[1]
    result = "".join([c for c in text if c == "z"])
    print(result if result else "none")
