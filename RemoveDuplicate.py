st=input("Enter the string")
st1=""
def duplicate(st,a,b):
    global st1
    if a==b:
        return False
    i=a
    count=0
    while i<b and st[i]==st[a]:
        count+=1
        i+=1
    if count>=1:
        st1+=st[a]
    return duplicate(st,a+count,b)
duplicate(st,0,len(st))
print(st1)
