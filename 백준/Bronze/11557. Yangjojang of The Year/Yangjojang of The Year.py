import sys

def read():
    return sys.stdin.readline().strip()

def choice (Input):
    for i in range(len(Input)):
        for j in range(i+1,len(Input)):
            if int(Input[i][1]) < int(Input[j][1]):
                Input[i], Input[j] = Input[j], Input[i] 
    
    return Input[0][0]

for _ in range(int(read())):
    Input = [read().split() for _ in range(int(read()))]
    
    print(choice(Input))