from collections import Counter

def solution(participant, completion):
    # Counter로 참가자와 완주자 목록의 빈도수 계산
    participant_counter = Counter(participant)
    completion_counter = Counter(completion)
    
    # 참가자 목록에서 완주자 목록을 빼서 차이를 계산
    result = participant_counter - completion_counter
    
    # 남은 항목(완주하지 못한 사람) 중 하나를 반환
    return list(result.keys())[0]

#Counter(participant)로 참가자 목록의 각 이름이 몇 번 나왔는지 셉니다.

#Counter(completion)로 완주자 목록의 각 이름이 몇 번 나왔는지 셉니다.

#participant_counter - completion_counter를 하면 두 Counter의 차이가 계산되어, 완주하지 못한 사람만 남게 됩니다.

#차이의 키를 리스트로 만들고, 첫 번째 값을 반환합니다.
