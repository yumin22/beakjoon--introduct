# 연산자 끼워넣기 (실버I)


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

Max = -1e9
Min = 1e9

def sol(n, tmp):
    global Max, Min

    if n == N-1:
        Max = max(tmp, Max)
        Min = min(tmp, Min)
        return
    
    if B[0] != 0:
        B[0] -= 1
        sol(n+1, tmp+A[n+1])
        B[0] += 1

    if B[1] != 0:
        B[1] -= 1
        sol(n+1, tmp-A[n+1])
        B[1] += 1
    
    if B[2] != 0:
        B[2] -= 1
        sol(n+1, tmp*A[n+1])
        B[2] += 1
    
    if B[3] != 0:
        B[3] -= 1
        sol(n+1, int(tmp/A[n+1]))
        B[3] += 1

sol(0, A[0])
print(Max)
print(Min)
