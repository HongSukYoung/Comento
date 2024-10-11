# Graph 탐색방법

## DFS (Depth-First Search, 깊이 우선 탐색):
- 스택 또는 재귀를 이용하여 한 방향으로 끝까지 탐색 후 다시 돌아옴.
- DFS는 Tree와 Graph 모두에서 사용할 수 있음.
- DFS는 미로 탐색, 그래프의 연결 성분 탐색 등에 자주 사용.

```python

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for neighbor in graph.adj_list[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

```

## BFS (Breadth-First Search, 너비 우선 탐색):
- 큐를 이용하여 가까운 노드부터 탐색.
- BFS는 최단 경로 탐색, 레벨 탐색 등에 효과적.

```python

from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        vertex = queue.popleft()
        print(vertex)
        for neighbor in graph.adj_list[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

```