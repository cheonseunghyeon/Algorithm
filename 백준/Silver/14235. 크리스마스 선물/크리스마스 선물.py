import sys
import heapq

def read():
    return sys.stdin.readline().strip()

C = []
for i in range(int(read())):
    text = list(map(int,read().split()))
    
    if text[0] == 0:
        if C:
            print(-int(heapq.heappop(C)))
        else:
            print(-1)
    else:
        for i in range(text[0]):
            heapq.heappush(C,-text[i+1])   
