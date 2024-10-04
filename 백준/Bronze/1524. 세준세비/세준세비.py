import sys

def read():
    return sys.stdin.readline().strip()

t = int(read())
for i in range(t) :
    read()	
    N, M = map(int, read().split())
    S = sorted(list(map(int, read().split())), reverse=True)
    B = sorted(list(map(int, read().split())), reverse=True)
    
    while S and B :	# 세준, 세비 병사 리시트가 비어있으면 while문 종료
        if S[-1] >= B[-1] :
            B.pop()
        else :
            S.pop()
    
    if S :
        print('S')
    elif S :
        print('B')
    else :
        print('B')