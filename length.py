st=input()
def length(st,a):
    if a==len(st)-1 :
        return True
    return (1+length(st,a+1))
ans=length(st,0)
print(ans)
