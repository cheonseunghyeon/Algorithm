from collections import deque

# BFS 함수 정의
def bfs(graph, visited, start):
    queue = deque([start])
    visited[start] = True
    count = 0  # 비행기 종류(간선)의 수
    
    while queue:
        node = queue.popleft()
        # 현재 노드와 연결된 국가들 탐색
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1  # 새로운 국가를 방문할 때마다 간선 수 증가
                
    return count

# 입력 처리
T = int(input())  # 테스트 케이스의 수

for _ in range(T):
    # 국가 수 N, 비행기 종류 수 M 입력 받기
    N, M = map(int, input().split())
    
    # 그래프 초기화
    graph = [[] for _ in range(N + 1)]  # 국가 번호가 1부터 시작하므로 N+1 크기로 생성
    
    # 비행기 정보 입력
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    # 방문 여부 확인 리스트
    visited = [False] * (N + 1)
    
    # BFS를 통해 모든 국가를 방문하면서 비행기 종류 수 계산
    result = bfs(graph, visited, 1)  # 1번 국가에서 BFS 시작
    
    # 결과 출력 (비행기 종류의 수 = 간선 수 = N-1)
    print(result)
