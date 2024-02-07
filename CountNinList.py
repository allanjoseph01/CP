lst=list(map(int,input("Enter the array:").split()))
n=int(input())
def countN(arr,a,b):
    if b==len(arr):
        return False
    if arr[b]==a:
        return (1+countN(arr,a,b+1))
    else:
        return(0+countN(arr,a,b+1))
ans=countN(lst,n,0)
print(ans)
