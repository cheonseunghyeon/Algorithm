import sys

test = True
count_list = {}
for n in range(int(sys.stdin.readline().strip())):
    
    input_data = sys.stdin.readline().strip()
    count_list[input_data] = True

for count in count_list:
    reverse_count = count[::-1]
    if reverse_count in count_list:
        length = len(count)
        middle_char = count[length // 2]  
        print(length, middle_char)
        break