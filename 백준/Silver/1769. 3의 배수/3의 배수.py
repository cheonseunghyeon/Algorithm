import sys
from collections import deque


number = sys.stdin.readline().strip()
threelist = ["3","6","9"]
count = 0

while len(number) > 1:
    total = sum(map(int,number)) 
    number = str(total)
    count += 1    

if number in threelist:
    print(str(count) + "\nYES")
else:
    print(str(count) + "\nNO")   

