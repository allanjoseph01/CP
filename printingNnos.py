n=int(input())
def printn(x,y):
    print(x,end=" ")
    if x==y:
        return False
    printn(x+1,y)
printn(1,n)
