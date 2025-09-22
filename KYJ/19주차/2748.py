import sys

n=int(sys.stdin.readline())
fib=list(range(n+1))

for i in range(n+1):
    if i==0:
        fib[i]=0
    elif i==1:
        fib[i]==1
    else:
        fib[i]=fib[i-1]+fib[i-2]

print(fib[n])




'''
def fib(k):
    if k==0:
        return 0
    elif k==1:
        return 1
    else:
        return fib(k-1)+fib(k-2)
    

n=int(sys.stdin.readline())

print(fib(n))
'''
    

