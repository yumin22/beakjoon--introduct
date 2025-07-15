# 연구소 (골드IV)
# 보류

import sys
import copy
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
mapList = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def sol():
    queue = deque()
    tmp_map = copy.deepcopy(mapList)

    for i in range(N):
        for j in range(M):
            if tmp_map[i][j] == 2:
                queue.append((i, j))
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i][0]
            ny = y + dy[i][1]

            if (0<=nx<N) and (0<=ny<M):
                if tmp_map[nx][ny] == 0:
                    tmp_map[nx][ny] = 2
                    queue.append((nx, ny))

    global answer
    cnt = 0

    for i in range(N):
        for j in range(M):
            if tmp_map[i][j] == 0:
                count += 1

    answer = max(answer, cnt)

def wall(cnt):
    if cnt == 3:
        sol()
        return
    
    for i in range(N):
        for j in range(M):
            if mapList[i][j] == 0:
                mapList[i][j] = 1
                wall(cnt+1)
                mapList[i][j] = 0

for i in range(N):
    mapList.append(list(map(int, input().split())))

answer = 0
wall(0)
print(answer)

