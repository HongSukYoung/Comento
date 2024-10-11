# DFS를 이용한 풀이

def dfs(numbers, target, index, current_sum):
    # 모든 숫자를 처리한 경우
    if index == len(numbers):
        # 현재 합계가 타겟 넘버와 같으면 경우의 수 1을 반환
        return 1 if current_sum == target else 0
    
    # 현재 숫자를 더하는 경우와 빼는 경우로 나누어 재귀 탐색
    add_case = dfs(numbers, target, index + 1, current_sum + numbers[index])
    subtract_case = dfs(numbers, target, index + 1, current_sum - numbers[index])
    
    # 두 경우의 수를 더해서 반환
    return add_case + subtract_case

def solution(numbers, target):
    # DFS를 처음 시작할 때는 인덱스 0과 초기 합계 0으로 시작
    return dfs(numbers, target, 0, 0)

#풀이 설명:
#DFS 함수 (깊이 우선 탐색):

#numbers: 숫자들의 리스트.
#target: 목표로 하는 숫자.
#index: 현재 탐색 중인 숫자의 인덱스.
#current_sum: 현재까지 계산된 합계.
#모든 숫자를 다 처리했을 때, 현재까지의 합계가 타겟과 같으면 1을 반환하고, 그렇지 않으면 0을 반환합니다.

#재귀적으로 탐색:

#각 숫자를 더하는 경우와 빼는 경우로 나누어 재귀 호출을 합니다.
#모든 숫자에 대해 재귀 탐색을 완료한 후 두 경우의 수를 합산합니다.

#solution 함수:

#처음에는 DFS 탐색을 시작할 때 인덱스는 0, 초기 합계는 0에서 시작합니다.

# BFS를 이용한 풀이
from collections import deque

def solution(numbers, target):
    queue = deque([(0, 0)])  # (current_sum, index)
    answer = 0
    
    while queue:
        current_sum, idx = queue.popleft()
        
        # 모든 숫자를 사용했을 때
        if idx == len(numbers):
            if current_sum == target:
                answer += 1
        else:
            # 숫자를 더하거나 빼는 두 가지 경우를 큐에 추가
            queue.append((current_sum + numbers[idx], idx + 1))
            queue.append((current_sum - numbers[idx], idx + 1))
    
    return answer

#BFS 풀이 설명:
#BFS는 큐를 사용하여 한 단계씩 모든 경우의 수를 탐색합니다.
#각 단계에서 숫자를 더하는 경우와 빼는 경우를 큐에 추가하여 순차적으로 탐색하며, 마지막에 타겟 넘버와 합계가 일치하는 경우를 카운팅합니다.