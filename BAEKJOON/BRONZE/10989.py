# 10989번 문제
# 정렬 문제 
# 총합 개수 비교 

import sys

number = int(sys.stdin.readline().strip())

list = []

for i in range(number):
    count = int(sys.stdin.readline().strip())
    list.append(count)

# 삽입 정렬 
# 2750번의 선택 정렬보다 빠르고 메모리 누수도 적음
# 왼쪽을 비교해서 작으면 계속 이동
for i in range(len(list)):
    for j in range(i,0,-1):
        if list[j] < list[j-1]:
            list[j], list[j-1] = list[j-1], list[j]
        else:
            break

for i in list:
    print(i)