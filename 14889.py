# 스타트와 링크 (실버I)

import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
S = []

for i in range(N):
    S.append(list(map(int, input().split())))

ability = []
team = []

for i in combinations(range(N), N//2):
    ability_team = 0

    for j in combinations(i, 2):
        ability_team += S[j[0]][j[1]] + S[j[1]][j[0]]
    ability.append(ability_team)
link = ability[len(ability)//2:]
start = ability[:len(ability)//2]
min_ability = float("inf")

for i in range(len(link)):
    min_ability = min(min_ability, abs(start[i]-link[len(link)-1-i]))

print(min_ability)
