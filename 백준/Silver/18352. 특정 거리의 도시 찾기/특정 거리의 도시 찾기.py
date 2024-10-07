from collections import deque

# 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시 X
N, M, K, X = map(int, input().split())

# 그래프를 저장할 리스트
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

distance = [-1] * (N + 1)
distance[X] = 0  # 출발 도시 X에서 자기 자신으로 가는 거리는 0

queue = deque([X])

while queue:
    current_city = queue.popleft()
    
    # 현재 도시에서 이동할 수 있는 모든 도시 확인
    for next_city in graph[current_city]:
        # 아직 방문하지 않은 도시라면
        if distance[next_city] == -1:
            # 최단 거리 갱신
            distance[next_city] = distance[current_city] + 1
            queue.append(next_city)

result = []

for i in range(1, N + 1):
    if distance[i] == K:
        result.append(i)

# 결과가 존재하면 오름차순으로 출력, 없으면 -1 출력
if result:
    for city in sorted(result):
        print(city)
else:
    print(-1)
