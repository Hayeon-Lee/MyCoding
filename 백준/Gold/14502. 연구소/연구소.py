import sys
from collections import deque
input = sys.stdin.readline

graph = []
answer = 0

n, m = map(int, input().split())
for _ in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)

def bfs():
    #상, 하, 좌, 우
    global answer 
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque(viruses[:])
    bfs_graph = [g[:] for g in graph]

    while queue:
        x,y = queue.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < m and bfs_graph[nx][ny] == 0:
                bfs_graph[nx][ny] = 2
                queue.append((nx, ny))

    tmp_cnt = 0
    for g in bfs_graph:
        for v in g:
            if v == 0: tmp_cnt += 1
    answer = max(answer, tmp_cnt)

def make_walls(wall):
    if wall == 3:
        bfs()
        return
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_walls(wall + 1)
                graph[i][j] = 0

viruses = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2: viruses.append((i,j))

make_walls(0)
print(answer)

'''
벽을 3개 세우고, bfs
'''