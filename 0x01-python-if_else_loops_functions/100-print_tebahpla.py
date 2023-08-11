#!/usr/bin/python3
print("".join("{}{}".format(chr(122 - i), chr(89 - i)) for i in range(26)), end="")
