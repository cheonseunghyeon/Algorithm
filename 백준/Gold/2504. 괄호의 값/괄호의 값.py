def calculate_bracket_value(bracket_string):
    stack = []
    result = 0
    temp = 1
    
    for i in range(len(bracket_string)):
        char = bracket_string[i]
        
        if char == '(':
            stack.append(char)
            temp *= 2
        elif char == '[':
            stack.append(char)
            temp *= 3
        elif char == ')':
            if not stack or stack[-1] != '(':
                return 0
            if bracket_string[i - 1] == '(':
                result += temp
            stack.pop()
            temp //= 2
        elif char == ']':
            if not stack or stack[-1] != '[':
                return 0
            if bracket_string[i - 1] == '[':
                result += temp
            stack.pop()
            temp //= 3
        else:
            return 0

    if stack:
        return 0

    return result

# 예시 입력
bracket_string = input().strip()
print(calculate_bracket_value(bracket_string))
