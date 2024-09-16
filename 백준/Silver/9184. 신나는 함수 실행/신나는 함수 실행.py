import sys 

dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)] #20 이상의 값은 모두 20으로 변경됨
def w(a,b,c):
  # 재귀 함수 반환 조건
  if a <= 0 or b <= 0 or c <= 0: # 모두 0 이상인 경우 1을 반환
    return 1
  if a > 20 or b > 20 or c > 20: # 모두 20 이상인 경우 20으로 치환
    return w(20,20,20)

  #메모리제이션으로 계산 값 기록
  if dp[a][b][c]:
    return dp[a][b][c]

  # dp[a][b][c]의 값을 적재
  if a < b < c:
    dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
  else:
    dp[a][b][c] =  w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

  # dp[a][b][c]의 값 반환
  return dp[a][b][c]

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    
    if a==-1 and b==-1 and c==-1:
        break
    print("w({}, {}, {}) = {}".format(a,b,c,w(a,b,c)))
