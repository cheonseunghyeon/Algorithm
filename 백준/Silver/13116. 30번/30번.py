from collections import deque
import sys
import heapq

def read():
    return sys.stdin.readline().strip()

def root(value):
    path = []
    while value > 1:
        path.append(value)
        value //= 2
    path.append(1)
    return path

def find(L,R):
    L.reverse()
    R.reverse()
    common = 1
    
    for i in range(min(len(L), len(R))):
        if L[i] == R[i]:
            common = L[i]
        else:
            break
        
    return common
    
for _ in range(int(read())):
    N,M = read().split()
    
    Llist = root(int(N))
    Rlist = root(int(M))
    
    print(find(Llist,Rlist) * 10)
    