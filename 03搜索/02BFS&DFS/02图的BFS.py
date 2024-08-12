from collections import deque


(n, m) = map(int, input().split())
# * 3
matrix = [[0] * m for _ in range(n)]
q = deque()
visited = [[0] * m for _ in range(n)]

for i in range(n):
    matrix[i] = list(map(int, input().split()))


def bfs():
    # ! 5
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    step = 0
    visited[0][0] = 1
    q.append((0, 0))
    # * 3
    while q:
        step += 1
        for _ in range(len(q)):
            x, y = q.popleft()
            for i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]
                # 条件判断
                # *终止
                if new_x == n - 1 and new_y == m - 1:
                    return step
                # * 新的点符合规则
                if (
                    new_x >= 0
                    and new_x < n
                    and new_y >= 0
                    and new_y < m
                    and matrix[new_x][new_y] == 0
                    and visited[new_x][new_y] == 0
                ):
                    visited[new_x][new_y] = 1
                    q.append((new_x, new_y))
    return 0


ans = bfs()
print(ans)
