# 2748 피보나치 수2

n=int(input())
fi = [0]*100
res = 0
fi[0] = 0
fi[1] = 1

for i in range(2,n+1):
    fi[i] = fi[i-1] + fi[i-2]
    
print(fi[n])

