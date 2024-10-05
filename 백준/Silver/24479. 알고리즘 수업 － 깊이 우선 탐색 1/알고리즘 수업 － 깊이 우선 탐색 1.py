import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한을 늘림

def read():
    return sys.stdin.readline().strip()

def dfs(graph, visited, order, R, count):
    visited[R] = True
    order[R] = count  # 방문 순서 기록
    count += 1
    for i in sorted(graph[R]):  # 인접한 정점을 오름차순으로 탐색
        if not visited[i]:
            count = dfs(graph, visited, order, i, count)  # 방문 순서를 증가시키며 재귀 호출
    return count

Set = list(map(int, read().split())) 
Input = [list(map(int, read().split())) for _ in range(Set[1])]  

visited = [False] * (Set[0] + 1)  # 방문 여부 체크 
order = [0] * (Set[0] + 1)  # 방문 순서 기록 

graph = [[] for _ in range(Set[0] + 1)]  # 인접 리스트 생성

# 간선 정보로 그래프 
for u, v in Input:
    graph[u].append(v)
    graph[v].append(u)

# DFS 시작
dfs(graph, visited, order, Set[2], 1)

for i in range(1, Set[0] + 1):
    print(order[i])
