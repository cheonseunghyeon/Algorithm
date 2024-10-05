import sys
from collections import deque

def read():
    return sys.stdin.readline().strip()

def bfs(graph, visited, order, R):
    queue = deque([R])
    visited[R] = True
    count = 1
    order[R] = count  # 시작 정점의 방문 순서를 1로 기록
    
    while queue:
        v = queue.popleft()  
        for i in sorted(graph[v]):  # 오름차순으로 인접 노드 탐색
            if not visited[i]: 
                count += 1
                visited[i] = True  # 방문 처리
                order[i] = count  # 방문 순서 기록
                queue.append(i)  # 큐에 추가

Set = list(map(int, read().split()))  # N, M, R
Input = [list(map(int, read().split())) for _ in range(Set[1])] 

visited = [False] * (Set[0] + 1)  # 방문 여부 체크
order = [0] * (Set[0] + 1)  # 방문 순서 기록

graph = [[] for _ in range(Set[0] + 1)]  # 인접 리스트 생성

for u, v in Input:
    graph[u].append(v)
    graph[v].append(u)

# BFS 시작
bfs(graph, visited, order, Set[2])

for i in range(1, Set[0] + 1):
    print(order[i])
