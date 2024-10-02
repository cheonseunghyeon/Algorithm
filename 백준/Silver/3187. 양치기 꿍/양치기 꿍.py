import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 설정

def read():
    return sys.stdin.readline().strip()

# 입력 처리
L, M = map(int, read().split())
List = [list(read()) for _ in range(L)]
visited = [[False] * M for _ in range(L)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    sheep = 0
    wolf = 0

    if List[x][y] == '#' or visited[x][y]:  # 울타리거나 이미 방문한 좌표라면 탐색 중지
        return 0, 0

    visited[x][y] = True

    # 양 또는 늑대가 있는 경우 카운트
    if List[x][y] == 'v':
        wolf = 1
    elif List[x][y] == 'k':
        sheep = 1

    # 상하좌우 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < L and 0 <= ny < M:  # 범위를 벗어나지 않는지 확인
            ns, nw = dfs(nx, ny)  # 재귀적으로 탐색하고 값을 더함
            sheep += ns
            wolf += nw

    return sheep, wolf

total_sheep = 0
total_wolf = 0

# 전체 좌표 탐색
for i in range(L):
    for j in range(M):
        if not visited[i][j] and List[i][j] != '#':  # 울타리 아니고 방문하지 않은 좌표만 탐색
            sheep, wolf = dfs(i, j)

            # 양과 늑대의 수 비교
            if sheep > wolf:
                total_sheep += sheep  # 양이 더 많으면 늑대는 모두 잡아먹힘
            else:
                total_wolf += wolf  # 늑대가 더 많으면 양이 잡아먹힘

# 결과 출력
print(total_sheep, total_wolf)
