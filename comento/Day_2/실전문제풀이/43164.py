def solution(tickets):
    # 경로를 저장할 사전
    routes = {}
    for ticket in tickets:
        # 출발 공항을 key, 도착 공항들을 value로 저장
        if ticket[0] in routes:
            routes[ticket[0]].append(ticket[1])
        else:
            routes[ticket[0]] = [ticket[1]]

    # 사전순으로 가장 앞서는 경로를 찾기 위해 도착 공항들을 알파벳 순으로 정렬
    for key in routes:
        routes[key].sort(reverse=True)

    # DFS를 위한 스택과 결과 경로 저장 리스트
    stack = ["ICN"]
    path = []

    while stack:
        current = stack[-1]

        # 더 이상 연결된 공항이 없으면 경로에 추가
        if current not in routes or len(routes[current]) == 0:
            path.append(stack.pop())
        else:
            # 연결된 공항이 있으면 그 공항으로 이동
            stack.append(routes[current].pop())

    # 경로를 뒤집어서 반환
    return path[::-1]
