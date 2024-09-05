# 24416번 문제
# 재귀함수와 동적 프로그래밍의 차이 구분 문제

counter1 = 0
# 피보나치 수 재귀호출 의사 코드
def fibo(n:int):
  global counter1

  # 탈출 조건 설정
  if n == 1 or n == 2:
    counter1 += 1
    return 1
  else:
    # 재귀 함수를 사용하여 두 항의 합 반환
    return (fibo(n-2) + fibo(n-1))

# 피보나치 수 동적 프로그래밍 의사 코드
def fibonacci(n):
  counter2 = 0
  # 빈 배열 설정
  f = [0] * (n+1)
  f[1] = f[2] = 1

  # 3번째 값부터 데이터 적재
  for i in range(3,n + 1):
    counter2 += 1
    f[i]= f[i-1] + f[i-2]

  return counter2;

number = int(input())
if 5 <= number <= 40:
  fibo(number)

  print(counter1,fibonacci(number))