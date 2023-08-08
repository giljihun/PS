from collections import deque

def bfs(start):
    global visited
    queue = deque([start])
    visited[start] = True
    while queue:
        current = queue.popleft()
        for next in range(1, N+1):
            if not visited[next] and graph[current][next]:
                visited[next] = True
                queue.append(next)

# 정점의 개수 : N, 간선의 개수 : M
N, M = map(int,input().split())

# graph, visited 배열 생성
graph = [[False] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)

# graph 정보 입력
for _ in range(M):
    u, v = map(int, input().split())
    graph[u][v] = True
    graph[v][u] = True

# 연결 요소의 개수를 저장하는 변수 count
count = 0

# 모든 정점에 대한 DFS 탐색
for i in range(1, N + 1):
    if not visited[i]:
        bfs(i)
        count += 1

print(count)
