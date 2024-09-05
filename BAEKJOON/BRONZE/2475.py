# 2475 문제

def printstar(number : int):

  for i in range(1, number + 1):
    star = "*" * i
    gap = " " * (number - i) * 2
    print(star + gap + star)

  for i in range(1, number + 1):
    star = "*" * (number - i)
    gap = (" " * i) * 2
    print(star + gap + star)

number = int(input())

if number <= 100 and number >= 1:
  printstar(number)
