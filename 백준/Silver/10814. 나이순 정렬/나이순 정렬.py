N = int(input())
result = []
for i in range(N):
    age, name = map(str, input().split())
    result.append([int(age), name])

result = sorted(result, key=lambda x: x[0])

for j in result:
    print(*j)