def solution(n, results):
    # 플로이드-워셜을 위한 그래프 초기화
    INF = float('inf')
    graph = [[INF] * n for _ in range(n)]
    
    # 자기 자신으로 가는 경로는 0
    for i in range(n):
        graph[i][i] = 0

    # 승리 결과 입력 (A가 B를 이겼을 때 graph[A][B] = 1)
    for win, lose in results:
        graph[win-1][lose-1] = 1  # 1을 의미: A가 B를 이겼다.
        graph[lose-1][win-1] = -1 # -1을 의미: B가 A에게 졌다.

    # 플로이드-워셜 알고리즘을 통해 모든 승리/패배 경로 계산
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1  # i가 k를 이기고 k가 j를 이기면 i가 j를 이김
                if graph[i][k] == -1 and graph[k][j] == -1:
                    graph[i][j] = -1  # i가 k에게 지고 k가 j에게 졌으면 i도 j에게 짐

    # 순위를 알 수 있는 선수 수 계산
    answer = 0
    for i in range(n):
        count = 0
        for j in range(n):
            if graph[i][j] != INF:  # 승패 관계가 명확한 경우
                count += 1
        if count == n:  # 자신을 제외한 모든 선수와의 승패 관계가 명확하면 순위를 알 수 있음
            answer += 1
    
    return answer

#코드 설명
#그래프 초기화:

#승리 결과를 그래프에 반영합니다. graph[A][B] = 1은 A가 B를 이겼다는 의미이며, graph[B][A] = -1은 B가 A에게 졌다는 의미입니다.
#초기에는 각 선수 간의 경로는 INF로 초기화하고, 자기 자신으로 가는 경로는 0으로 설정합니다.

#플로이드-워셜 알고리즘:

#k 선수를 거쳐가는 경로를 고려하여, 만약 i 선수가 k를 이기고, k 선수가 j를 이긴다면 i 선수는 j 선수도 이긴다고 할 수 있습니다.
#마찬가지로, i 선수가 k에게 지고, k 선수가 j에게 졌다면 i 선수는 j 선수에게도 진 것입니다.
#순위를 알 수 있는 선수 계산:

#각 선수에 대해 자신을 제외한 다른 모든 선수와의 승패 관계가 명확하면 순위를 알 수 있습니다. 즉, n-1개의 승리 또는 패배 관계가 명확해야 합니다.