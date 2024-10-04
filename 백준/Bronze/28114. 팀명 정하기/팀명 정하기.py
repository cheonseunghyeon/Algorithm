import sys


def read():
    return sys.stdin.readline().strip()

Input = [read().split() for _ in range(3)]    
name = "" 
year = ""
# 선택 정렬
for i in range(3):
    min = i
    for j in range(i+1,3):
        if int(Input[i][0]) < int(Input[j][0]):
            Input[i], Input[j] = Input[j], Input[i] 
            
    name += list(Input[i][2])[0]
            
# Input.sort(key=lambda x: x[1])

# 삽입 정렬
for i in range(1,3):
    for j in range(i,0,-1):
        if int(Input[j - 1][1])  > int(Input[j][1]):
            Input[j-1], Input[j] =  Input[j],Input[j-1]
        else:
            break

for i in range(3):
    year += "".join(list(Input[i][1])[2:])

print(year)
print(name)