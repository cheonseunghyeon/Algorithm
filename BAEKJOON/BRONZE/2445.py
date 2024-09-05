# 2445 문제

def square(number: int):
  return number**2


def result(list: list):
  total = sum(list) % 10
  return total


number_list = list(map(int, input().strip().split()))
number_list = list(map(square, number_list))

total = result(number_list)

print(total)