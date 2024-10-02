from collections import deque
import sys
import heapq

def read():
    return sys.stdin.readline().strip()

List = [read().split() for _ in range(5)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

result = set()
def dfs(x,y,num):
    if len(num) == 6:
        result.add(num)
        return
    
    for i in range(4):
        nx = x+ dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, num + List[nx][ny])
            
for i in range(5):
    for j in range(5):
        dfs(i,j,List[i][j])
        
print(len(result))