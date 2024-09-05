# 10872 문제
# 팩토리얼 설계 문제

# 재귀 함수를 사용
def factorial(n: int):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)

number = int(input())

if 0 <= number <= 12:
    print(factorial(number))