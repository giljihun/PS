n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y, visited, cnt):
    visited[x][y] = True
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if graph[nx][ny] == 1 and not visited[nx][ny]:
            cnt = dfs(nx, ny, visited, cnt+1)
    return cnt

cnt = 0
result = []
visited = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            cnt += 1
            house_cnt = dfs(i, j, visited, 1)
            result.append(house_cnt)

result.sort()
print(cnt)
for i in range(cnt):
    print(result[i])
