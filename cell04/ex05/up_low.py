sen = input()
for i in sen:
    if i.isupper():
        print(i.lower() , end="")
    elif i.islower():
        print(i.upper() , end="")
    else:
        print(i , end="")
print("\n")