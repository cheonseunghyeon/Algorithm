import sys

def read():
    return sys.stdin.readline().strip()

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if len(x) < len(pivot) or (len(x) == len(pivot) and x < pivot)]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if len(x) > len(pivot) or (len(x) == len(pivot) and x > pivot)]
    
    return quick_sort(left) + middle + quick_sort(right)

N = int(read())
Input = [read() for _ in range(N)]

# 중복 제거
Input = list(set(Input))

sorted_input = quick_sort(Input)

for item in sorted_input:
    print(item)
