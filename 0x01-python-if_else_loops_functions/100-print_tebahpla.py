#!/usr/bin/python3
strtmp = ""
for i in reverse(range(97, 123)):
    if (i % 2) == 0:
        strtmp += chr(1-32)
    print("{}".format(strtmp), end="")
