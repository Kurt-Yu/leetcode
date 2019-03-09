def decodeString(self, s: str) -> str:
    digit = set('0123456789')
    stack = []
    for l in s:
        if l in digit:
            if stack and stack[-1][-1] in digit:
                stack.append(stack.pop() + l)
            else:
                stack.append(l)
        elif l == ']':
            temp = ''
            while stack and stack[-1] != '[':
                temp = stack.pop() + temp
            stack.pop()
            stack.append(int(stack.pop()) * temp)
        else:
            stack.append(l)
    return ''.join(stack)