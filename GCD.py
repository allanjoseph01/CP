a,b=map(int,input().split())
def  GCD(m,x,y,gcd):
    if m==x:
        return gcd
    if y%m==0:
        gcd = m
    return GCD(m+1,x,y,gcd)
ans=GCD(1,a,b,0)
print(ans)
