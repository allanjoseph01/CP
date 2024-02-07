n,r,m=map(int,input().split())
def factorial(x):
    if x<=1:
        return 1
    return x*factorial(x-1)
def combination(a,b):
    return (factorial(a)/(factorial(b)*factorial(a-b)))
ans = combination(n,r)
print(int(ans%m))
