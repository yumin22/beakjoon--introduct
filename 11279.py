# 최대 힙 (실버II)

###
# 널리 잘 알려진 자료구조 중 최대 힙이 있다. 최대 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.
# 1. 배열에 자연수 x를 넣는다.
# 2. 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
# 프로그램은 처음에 비어있는 배열에서 시작하게 된다.
###

import sys
import heapq

N = int(sys.stdin.readline())
heap = []
max_index = 0

for i in range(N):
    X = int(sys.stdin.readline())

    if X > 0:
        heapq.heappush(heap, -X)
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(heap))

###
# 어려웠던 점
# - 시간 초과 문제: heapq 안썼을 때 시간초과 문제 겪음 
# - heapq 시간 복잡도: O(log N) // 안쓰고 list로만 작성 시: O(N)
###