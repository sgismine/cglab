# 10816

# lower bound : 찾고자 하는 숫자 이상의 값이 처음으로 시작하는 지점 (bisect_left)
# upper bound : 찾고자 하는 숫자 초과의 값이 처음으로 시작하는 지점 (bisect_right)

# bisect_left : 가장 마지막의 start 값이 lower bound
# bisect_right : 가장 마지막의 end 값이 upper bound

# -> 정렬된 리스트에서 같은 수의 개수는 bisect_right - bisect_left 
# 이걸 lower bound와 upper bound로 구하면 upper bound - lower bound +1 이지만
# bisect_right, bisect_left를 사용하면 +1을 안해야함 ,, 이유는 모르겠음 ㅜ

import sys
from bisect import bisect_left,bisect_right

n = int(sys.stdin.readline())
lst_n = list(map(int,sys.stdin.readline().split()))

m = int(sys.stdin.readline())
lst_m = list(map(int,sys.stdin.readline().split()))


lst_n.sort()


for i in lst_m:
    print(bisect_right(lst_n,i)-bisect_left(lst_n,i),end=" ")