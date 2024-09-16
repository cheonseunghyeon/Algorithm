import sys

number = int(sys.stdin.readline().strip())

list = []

for i in range(number):
    count = int(sys.stdin.readline().strip())
    list.append(count)

list.sort()

for i in list:
    print(i)