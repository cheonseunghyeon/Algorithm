from collections import deque

# 입력 받기
n = int(input())  # 게임판의 크기 N
game_board = [list(map(int, input().split())) for _ in range(n)]  # 게임판 정보

# 방향 이동: 오른쪽(0, 1), 아래쪽(1, 0)
directions = [(0, 1), (1, 0)]

# BFS를 사용하여 게임판을 탐색하는 함수
def bfs():
    # 큐 초기화: 시작점 (0, 0)
    queue = deque([(0, 0)])
    visited = [[False] * n for _ in range(n)]  # 방문 여부 기록
    visited[0][0] = True  # 시작점 방문 처리

    while queue:
        x, y = queue.popleft()
        if game_board[x][y] == -1:  # 승리 지점에 도달하면
            print("HaruHaru")
            return
        
        # 현재 위치에서 이동할 수 있는 칸 수
        jump = game_board[x][y]

        # 오른쪽과 아래로 이동 시도
        for dx, dy in directions:
            nx, ny = x + dx * jump, y + dy * jump  # 이동할 새로운 좌표 계산

            # 새로운 좌표가 게임판 내에 있고, 방문하지 않은 경우
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True  # 방문 처리
                queue.append((nx, ny))  # 큐에 새로운 좌표 추가

    # 모든 경로를 탐색했으나 도착하지 못한 경우
    print("Hing")

# BFS 탐색 시작
bfs()
