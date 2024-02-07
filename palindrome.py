st=input("Enter the string:")
def palindrome(st,a,b):
    if b==(a//2):
        return True
    if st[b]==st[a-1-b]:
        return (1+palindrome(st,a,b+1))
    else:
        return (0+palindrome(st,a,b+1))
ans=palindrome(st,len(st),0)
if len(st)%2==0:
    if ans==len(st)//2:
        print("Yes")
    else:
        print("No")
elif len(st)%2!=0:
    if ans==len(st)//2+1:
        print("Yes")
    else:
        print("No")
