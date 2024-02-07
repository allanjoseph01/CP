n=int(input())
def sumofdigit(x):
    if  x==0:
        return 0
    return (x%10 + sumofdigit(x//10))
ans=sumofdigit(n)
print(ans)
