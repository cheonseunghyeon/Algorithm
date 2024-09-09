# 2750번 문제
# 76972KB	1280MS

# 정렬 문제

import sys

number = int(sys.stdin.readline().strip())

list = []

for i in range(number):
    count = int(sys.stdin.readline().strip())
    list.append(count)

# 정렬 내장 함수 사용
list.sort()

for i in list:
    print(i)