# 수리공 항승 (실버III)

import sys
input = sys.stdin.readline

N, L = map(int, input().split())
hole = list(map(int, input().split()))
hole.sort()

start = hole[0]
cnt = 1

for i in hole[1:]:
    if i in range(start, start+L):
        continue
    else:
        start = i
        cnt +=1

print(cnt)

