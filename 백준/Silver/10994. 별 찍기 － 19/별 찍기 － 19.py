N = int(input())

length = int((4 * N) - 3)
stars = [[' ' for _ in range(length)]for _ in range(length)]

def star(N:int,x:int,y:int):
  if N == 1:
    stars[x][y] = "*"
    return 

  length = int((4 * N) - 3)
  for i in range(length):
    stars[x][y+i] = '*'
    stars[x+i][y] = "*"
    stars[x + length - 1][y + i] = "*"
    stars[x + i][y + length - 1] = "*"

  star(N-1,x+2,y+2)

if 1 <= N <= 100:
  star(N,0,0)
  for i in stars:
    print(''.join(i))
