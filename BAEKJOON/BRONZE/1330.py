# 1330 문제
# 입출력 문제

def math (a:int, b:int):
  if a > b:
    print(">")
  elif a < b:
    print("<")
  else:
    print("==")

a, b = map(int, input().strip().split())
math(a,b)
