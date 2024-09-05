# 10994
# 좌표 문제
# 1.시작 좌표(0,0)부터 2차원 배열의 값을 변경(네모 그리기)
# 2.시작 좌표를 변경 후 재귀적으로 해당 작업 반복

N = int(input())

length = int((4 * N) - 3) # 2차원 배열의 최대 크기 설정
stars_loc = [[' ' for _ in range(length)]for _ in range(length)] # ' ' 값으로 초기화

def star(N:int,x:int,y:int): # N = 네모 개수, x,y = 시작 좌표
  if N == 1:
    stars_loc[x][y] = "*"
    return

  length = int((4 * N) - 3) # 좌표의 최대 크기
  for i in range(length):
    stars_loc[x][y+i] = '*'
    stars_loc[x+i][y] = "*"
    stars_loc[x + length - 1][y + i] = "*"
    stars_loc[x + i][y + length - 1] = "*"

  star(N-1,x+2,y+2)

if 1 <= N <= 100:
  star(N,0,0)
  for i in stars_loc:
    print(''.join(i)) # 리스트 출력
