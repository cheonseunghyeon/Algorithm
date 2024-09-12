def math (a:int, b:int):
  if a > b:
    print(">")
  elif a < b:
    print("<")
  else:
    print("==")

a, b = map(int, input().split(' '))
math(a,b)