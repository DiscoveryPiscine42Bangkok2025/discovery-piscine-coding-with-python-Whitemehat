#!/usr/bin/env python3
import sys
import re

word = sys.argv[1]
sentence = input("What was the parameter? ")
matches = re.findall(rf"\b{re.escape(word)}\b", sentence)
if(matches):
    print("Good job!")
else:
    print("Nope, sorry...")