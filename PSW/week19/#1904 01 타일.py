import sys

def bin_seq(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    a, b = 1, 2  # dp[1], dp[2]
    for _ in range(3, n + 1):
        a, b = b, (a + b) % 15746
    return b

n = int(sys.stdin.readline())
print(bin_seq(n))
