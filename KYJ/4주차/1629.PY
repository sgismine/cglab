import sys

def function(a,b,d):
    if b == 1:
        return a%c
    if b % 2 ==0:
        return(function(a,b//2,d)**2)%d
    else:
        return((function(a,b//2,d)**2)*a)%d

a,b,d=map(int,sys.stdin.readline().split())
print(function(a,b,d))