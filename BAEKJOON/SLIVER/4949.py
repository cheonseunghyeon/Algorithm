# 4949번 문제
# 34028KB	80MS

import sys
from collections import deque

while True:
    result = deque([])
    string = list(sys.stdin.readline().rstrip())

    if string[0] == ".":
        break

    balanced = True
    for i in string:
        if i == "(" or i == "[": # 문자열을 리스트형태로 받아서 비교
            result.append(i)
        elif i == ")":
            if result and result[-1] == "(": # () 한쌍이면 제거 
                result.pop()
            else:
                balanced = False # 
                break
        elif i == "]":
            if result and result[-1] == "[": # [] 한쌍이면 제거 
                result.pop()
            else:
                balanced = False
                break

    if balanced and not result:
        print("yes")
    else:
        print("no")
