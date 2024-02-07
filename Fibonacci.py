n=int(input())
lst=[0,1]
def Fibonacci(n,a,b):
    if a==n-2:
        return False
    lst.append(lst[-1]+lst[-2])
    return Fibonacci(n,a+1,lst[-1])
Fibonacci(n,0,1)
for i in lst:
    print(i,end=" ")
