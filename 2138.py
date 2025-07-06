# 전구와 스위치 (골드IV)

# N개의 스위치와 N개의 전구가 있다. 
# 각각의 전구는 켜져 있는 상태와 꺼져 있는 상태 중 하나의 상태를 가진다. 
# i(1 < i < N)번 스위치를 누르면 i-1, i, i+1의 세 개의 전구의 상태가 바뀐다. 
# 즉, 꺼져 있는 전구는 켜지고, 켜져 있는 전구는 꺼지게 된다. 1번 스위치를 눌렀을 경우에는 1, 2번 전구의 상태가 바뀌고, 
# N번 스위치를 눌렀을 경우에는 N-1, N번 전구의 상태가 바뀐다.

# N개의 전구들의 현재 상태와 우리가 만들고자 하는 상태가 주어졌을 때, 
# 그 상태를 만들기 위해 스위치를 최소 몇 번 누르면 되는지 알아내는 프로그램을 작성하시오.

N = int(input())

In = list(map(int, input()))
Out = list(map(int, input()))

def change(In, Out):
    count = 0

    for i in range(1, N):
        if In[i-1] == Out[i-1]:
            continue
        count += 1

        for j in range(i-1, i+2):
            if j < N:
                In[j] = 1 - In[j]

    if In == Out:
        return count
    else:
        return 1e9

answer = change(In[:], Out)

In[0] = 1 - In[0]
In[1] = 1 - In[1]
answer = min(answer, change(In[:], Out)+1)

if answer != 1e9:
    print(answer)
else:
    print(-1)


