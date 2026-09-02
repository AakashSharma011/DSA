n=4
dp={}
def fib(n):
    if n<=1:
        return n
    if n in dp:
        return dp[n]
    dp[n]=fib(n-1)+fib(n-2)
    return dp[n]
print(fib(n))