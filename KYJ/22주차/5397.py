import sys

t=int(sys.stdin.readline())
result=[]

for _ in range(t):
    keylog = input().strip()
    left = []
    right = []
    
    for ch in keylog:
        if ch == '-':
            if left:
                left.pop()
        elif ch == '<':
            if left:
                right.append(left.pop())
        elif ch == '>':
            if right:
                left.append(right.pop())
        else:
            left.append(ch)
    
    result.append(''.join(left + right[::-1]))

for x in result:
    print(x)