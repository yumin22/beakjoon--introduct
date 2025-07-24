# 통나무 건너뛰기 (실버I)

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()

    cnt = 0
    for i in range(2, N):
        cnt = max(cnt, abs(L[i] - L[i - 2]))
    
    print(cnt)
