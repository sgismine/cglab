# 1629 곱셈

# A, B, C = map(int,input().split())
# n = A
# count = 0
# rem = []
# while(n < C):
#     n*=A
#     count += 1
# start = n % C
# rem.append(start)
# for i in range(count, B) :
#     n*=A
#     remain = n%C
#     if remain == start :
#         break
#     rem.append(remain)
# patternlen = len(rem)
# ans = rem[(B-count)% patternlen]
# print(ans)
    
# 지수 법칙 : A^m+n = A^m x A^n
# 나머지 분배 법칙 : (AxB)%C = (A%C) *(B%C) % C  -> 이건 수학문제 아니냐고..

def multi (A,n):
    if n == 1 :
        return A%C
    else :
        tmp = multi(A,n//2)
        if n%2 == 0:
            return (tmp * tmp) % C
        else :
            return (tmp * tmp * A) % C

A, B, C = map(int,input().split())
print(multi(A,B))


