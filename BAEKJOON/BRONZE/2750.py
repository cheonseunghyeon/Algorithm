# 2750번 문제
# 31120KB	136MS

# 정렬 문제

import sys

number = int(sys.stdin.readline().strip())

list = []

for i in range(number):
    count = int(sys.stdin.readline().strip())
    list.append(count)

# 선택 알고리즘 
# 0번째 부터 가장 작은 수를 찾아 순서대로 0,1,2 번째 자리를 바꿈
for i in range(len(list)):
    min_index = i
    for j in range(i+1,len(list)):
        if list[min_index] > list[j]:
            list[min_index], list[j] = list[j], list[min_index]
            
# 정렬 함수 사용 시 편함
# list.sort()
for i in list:
    print(i)