import sys
import heapq
def read():
    return sys.stdin.readline().strip()

N = int(read())
First = list(map(int,read().split()))
Second = list(map(int,read().split()))

First.sort()
Second.sort()
Second.reverse()

total = 0

for i in range(N):
    total += First[i] * Second[i]
print(total)
