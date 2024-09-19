n=int(input())
list = []
for i in range(n):
    [a, b] = map(int, input().split())
    list.append([a, b])
list.sort()
for i in list:
    print(i[0], i[1])