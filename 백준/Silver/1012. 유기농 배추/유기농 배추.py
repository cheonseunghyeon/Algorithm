from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,farm,visited,M,N):
    queue = deque()
    queue.append((x,y))
    visited[y][x] = True
    
    while queue:
        cx,cy = queue.popleft()
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if 0 <= nx < M and 0 <= ny < N and farm[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((nx, ny))
    return -1 

for _ in range(int(input())):
    M,N,K = map(int,input().split())
    
    farm = [[0]* M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    

    for _ in range(K):
        x,y = map(int,input().split())
        farm[y][x] = 1
        
    count = 0
    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1 and not visited[i][j]:
                bfs(j, i, farm, visited, M, N) 
                count += 1
    print(count)