import sys
from collections import deque

while True:
    result = deque([])
    string = list(sys.stdin.readline().rstrip())

    if string[0] == ".":
        break

    balanced = True
    for i in string:
        if i == "(" or i == "[":
            result.append(i)
        elif i == ")":
            if result and result[-1] == "(":
                result.pop()
            else:
                balanced = False
                break
        elif i == "]":
            if result and result[-1] == "[":
                result.pop()
            else:
                balanced = False
                break

    if balanced and not result:
        print("yes")
    else:
        print("no")
