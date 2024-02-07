a,b,m=map(int,input().split())
def power(x,y):
    if y==0:
        return True
    return (x*power(x,y-1))
j=power(a,b)
print(j%m)
