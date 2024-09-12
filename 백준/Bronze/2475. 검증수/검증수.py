def square(number: int):
  return number**2


def result(list: list):
  total = sum(list) % 10
  return total


number_list = list(map(int, input().split(' ')))
number_list = list(map(square, number_list))

total = result(number_list)

print(total)
