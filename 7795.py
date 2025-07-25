# 먹을 것인가 먹힐 것인가 (실버III)

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    start = 0
    cnt = 0

    for j in range(N):
        while True:
            if start == M or A[j]<=B[start]:
                cnt += start
                break
            else:
                start+=1
    
    print(cnt)

