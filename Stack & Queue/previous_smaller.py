arr=[4,1,2,5,3]
stack=[]
ans=[]
for i in arr:
    while stack and stack[-1]>=i:
        stack.pop()
        if stack:
            ans.append(stack[-1])
        else:
            ans.append(-1)
    stack.append(i)
print(ans)