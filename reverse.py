s=input()
def reverse(a):
    if a==-(len(s)+1):
        return ""
    return s[a]+reverse(a-1)
ans=reverse(-1)
print(ans)
