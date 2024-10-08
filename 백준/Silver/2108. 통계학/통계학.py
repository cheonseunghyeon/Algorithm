from collections import deque
import sys
input = sys.stdin.readline

Input = []
for _ in range(int(input())):
    Input.extend(map(int, input().split()))

# 산술 평균
print(round(sum(Input) / len(Input)))

Input.sort()

# 중앙값
print(Input[len(Input)//2])

dic = {}
for i in Input:
    if i in dic:
        dic[i] = dic[i] + 1
    else:
        dic[i] = 1
        
tmp = max(dic.values())
key = [key for key,value in dic.items() if value == tmp]

# 최빈값
if len(key) == 1:
    print(key[0])
else:
    print(key[1])
    
# 범위
print(max(Input) - min(Input))