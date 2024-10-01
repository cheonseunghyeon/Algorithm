from collections import deque
import sys
import heapq

def read():
    return sys.stdin.readline().strip()

Test = deque()
for _ in range(int(read())):
    N = int(read())
    T = list(map(int, read().split())) 
  
    heapq.heapify(T)

    total = 0
    
    while len(T) > 1:
        one = heapq.heappop(T)
        two = heapq.heappop(T)

        cost = one + two
        total += cost
        
        heapq.heappush(T,cost)
    print(total)
        
