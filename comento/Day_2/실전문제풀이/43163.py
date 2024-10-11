from collections import deque

# 두 단어가 변환 가능한지 확인하는 함수 (한 글자만 다를 때 True)
def is_one_letter_different(word1, word2):
    difference_count = 0
    for a, b in zip(word1, word2):
        if a != b:
            difference_count += 1
        if difference_count > 1:
            return False
    return difference_count == 1

def solution(begin, target, words):
    if target not in words:  # target이 words 안에 없다면 변환 불가
        return 0

    # BFS를 위한 큐 준비 (변환된 단어, 변환 횟수)
    queue = deque([(begin, 0)])
    visited = set([begin])  # 방문한 단어를 저장

    while queue:
        current_word, steps = queue.popleft()

        # 목표 단어에 도달하면 변환 횟수를 반환
        if current_word == target:
            return steps

        # words 리스트에서 아직 방문하지 않은 단어 중에서
        # 한 글자만 다른 단어로 변환 가능한 단어들을 큐에 추가
        for word in words:
            if word not in visited and is_one_letter_different(current_word, word):
                visited.add(word)
                queue.append((word, steps + 1))

    return 0  # 변환 불가능할 경우
