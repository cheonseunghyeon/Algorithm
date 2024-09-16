import sys

number = int(sys.stdin.readline().strip())

list = []

for i in range(number):
    count = int(sys.stdin.readline().strip())
    list.append(count)

for i in range(len(list)):
    min_index = i
    for j in range(i+1,len(list)):
        if list[min_index] > list[j]:
            list[min_index], list[j] = list[j], list[min_index]

for i in list:
    print(i)