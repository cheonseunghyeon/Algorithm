import sys

count = int(sys.stdin.readline().strip())

list = {}

for _ in range(count):
  string = sys.stdin.readline().strip()

  if string.find("."):
    string = string[string.find(".") + 1:]

  if string in list:
    list[string] += 1

  else:
    list[string] = 1

sort_list = sorted(list.items())

for key,value in sort_list:
  print('{} {}'.format(key,value))
