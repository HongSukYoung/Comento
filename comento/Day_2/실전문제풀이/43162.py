# DFS를 이용한 풀이
def dfs(computers, visited, node):
    # 현재 노드를 방문 처리
    visited[node] = True
    # 해당 노드와 연결된 다른 노드를 방문
    for i in range(len(computers)):
        if computers[node][i] == 1 and not visited[i]:
            dfs(computers, visited, i)

def solution(n, computers):
    visited = [False] * n  # 각 컴퓨터가 방문되었는지 확인하는 리스트
    network_count = 0  # 네트워크 수를 저장하는 변수

    # 모든 컴퓨터를 탐색
    for i in range(n):
        # 아직 방문되지 않은 컴퓨터라면 새로운 네트워크 시작
        if not visited[i]:
            dfs(computers, visited, i)
            network_count += 1  # 네트워크 카운트 증가

    return network_count

# BFS를 이용한 풀이

from collections import deque

def bfs(computers, visited, node):
    queue = deque([node])
    visited[node] = True
    while queue:
        current_node = queue.popleft()
        for i in range(len(computers)):
            if computers[current_node][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i] = True

def solution(n, computers):
    visited = [False] * n
    network_count = 0

    for i in range(n):
        if not visited[i]:
            bfs(computers, visited, i)
            network_count += 1

    return network_count

