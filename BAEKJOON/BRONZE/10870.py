# 10870 문제
# 피보나치 수열 문제

def fibo(n:int):
  if n <= 1:
    return n
  return fibo(n-2) + fibo(n-1)

number = int(input())
if number == 0 or number <= 20:
  print(fibo(number))