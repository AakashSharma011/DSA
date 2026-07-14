s="(){}[]"
def isValid(s):
    stack=[]
    pairs = {
    ')': '(',
    ']': '[',
    '}': '{'
}
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        else:
            if len(stack)==0:
                return False
            if stack[-1]!=pairs[ch]:
                return False
            stack.pop()
    return not stack
print(isValid(s))
