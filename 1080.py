# 행렬 (실버I)

# 0과 1로만 이루어진 행렬 A와 행렬 B가 있다. 
# 이때, 행렬 A를 행렬 B로 바꾸는데 필요한 연산의 횟수의 최솟값을 구하는 프로그램을 작성하시오.
# 행렬을 변환하는 연산은 어떤 3×3크기의 부분 행렬에 있는 모든 원소를 뒤집는 것이다. (0 → 1, 1 → 0)

import sys

N, M = map(int, sys.stdin.readline().split())

A = []
for _ in range(N):
    A.append(list(map(int, list(input()))))

B = []
for _ in range(N):
    B.append(list(map(int, list(input()))))

count = 0

def check(a, b):
    for i in range(a, a+3):
        for j in range(b, b+3):
            if A[i][j] == 0:
                A[i][j] = 1
            else:
                A[i][j] = 0

if (N < 3 or M < 3) and A!=B:
    count = -1
else: 
    for i in range(N-2):
        for j in range(M-2):
            if A[i][j] != B[i][j]:
                count += 1
                check(i, j)

if count != -1:
    if A != B:
        count = -1

print(count)