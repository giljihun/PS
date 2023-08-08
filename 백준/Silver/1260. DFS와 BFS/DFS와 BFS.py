# 정점의 개수, 간선의 개수, 시작할 정점의 번호!

def dfs(idx) :
    global visited
    visited[idx] = True
    print(idx, end = ' ')
    for next in range(1, N + 1):
        if not visited[next] and graph[idx][next]:
            dfs(next)

def bfs():
    global que, visited
    while que:
        current = que.pop(0)
        print(current, end = ' ')
        for next in range(1, N + 1):
            if not visited[next] and graph[current][next]:
                visited[next] = True
                que.append(next)

N, M, V = map(int, input().split())

# (N + 1) X (N + 1) 짜리 배열
graph = [[False] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)


# graph 정보 입력!
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

# V부터 dfs를 수행해라!
dfs(V)
print()

# bfs를 수행하기 위해 visited를 다시 False로 초기화 시켜준다!
visited = [False] * (N + 1)

que = [V]
visited[V] = True
bfs()
