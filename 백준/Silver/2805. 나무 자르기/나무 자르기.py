import sys
from collections import deque

def read():
    return sys.stdin.readline().strip()


Set = list(map(int, read().split()))
Input = list(map(int, read().split()))

min = 0
max = max(Input)
mid = (min + max) // 2
total = 0

while min <= max:
    mid = (min + max) // 2
    total = 0
    
    for item in Input:
        if item > mid:
            total += item - mid
            
    if total >= Set[1]:
        result = mid  # 현재 높이를 기록
        min = mid + 1  # 더 높은 높이를 탐색
    else:
        max  = mid - 1  # 더 낮은 높이를 탐색

print(result)