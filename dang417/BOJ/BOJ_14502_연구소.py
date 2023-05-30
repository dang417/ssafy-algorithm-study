import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline
from collections import deque, defaultdict

N, M = map(int, input().split())

# 벽 세개를 고르는 알고리즘
# 그 케이스에서 바이러스를 퍼트리는 알고리즘
# 결과물에서 바이러스가 퍼지지 않은 영역의 크기를 세는 알고리즘

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

def BuildWall(original_lab, cnt):

    lab = defaultdict(list)

    for i in range(N):
        lab[i] = original_lab[i][::]

    if cnt == 3:
        Virus(lab)
        return

    for i in range(N):
        for j in range(M):
            if not lab[i][j]:
                lab[i][j] = 1
                BuildWall(lab, cnt + 1)
                lab[i][j] = 0

def Virus(lab):
    global rlt

    q = original_q.copy()
    tmp = 0

    for i in range(N):
        tmp += lab[i].count(0)

    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and not lab[ni][nj]:
                lab[ni][nj] = 2
                tmp -= 1
                if rlt >= tmp:
                    return
                q.append((ni, nj))

    rlt = tmp


lab = [list(map(int, input().split())) for _ in range(N)]

original_q = deque()
for i in range(N):
    for j in range(M):
        if lab[i][j] == 2:
            original_q.append((i, j))

rlt = 0
BuildWall(lab, 0)

print(rlt)