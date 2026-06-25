Matrix=[1,2,3],[4,5,6],[7,8,9]
n=len(Matrix)
for i in range(n):
    for j in range(i+1,n):
        Matrix[i][j],Matrix[j][i]=Matrix[j][i],Matrix[i][j]
for i in range(n):
    Matrix[i].reverse()
print(Matrix)