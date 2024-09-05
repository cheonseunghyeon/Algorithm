# 11945 문제

def reverse(a:int,b:int):
  array = [list(reversed(list(map(int,input().strip())))) for _ in range(a)]

  return array
  
a,b = map(int,input().split(' '))

if 0 <= a and b <= 10:
  result_array = reverse(a, b)

  for row in result_array:
      print(''.join(map(str, row)))