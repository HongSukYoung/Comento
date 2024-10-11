# Hash

- Hash: 해시(Hash)는 데이터를 효율적으로 저장하고 조회하기 위한 방법으로, 키(Key)를 기반으로 데이터를 빠르게 찾을 수 있습니다. 해시 테이블은 일반적으로 배열 형태로 구현되며, 해시 함수(Hash Function)를 사용하여 키를 특정 인덱스로 매핑합니다.

- Hash Collision: 두 개 이상의 키가 같은 인덱스로 매핑될 때 발생합니다. 이를 해결하는 대표적인 방법이 체이닝(Chaining)과 오픈 어드레싱(Open Addressing) 입니다. 
모든 가능성을 탐색하는 방법으로, 해를 찾다가 막히면 이전 상태로 돌아가서 다른 경로를 탐색하는 방식입니다.

## Hash 알고리즘의 종류

- MD5 (Message Digest 5): 오래된 해시 알고리즘으로, 데이터의 고유한 128비트 해시값을 생성합니다. 보안 측면에서는 안전하지 않지만 여전히 데이터 무결성 확인에 사용됩니다.

- SHA (Secure Hash Algorithm): 보안성이 강화된 해시 알고리즘입니다. SHA-256 같은 알고리즘은 256비트 해시값을 생성하며, 주로 데이터 무결성 확인과 암호화에 사용됩니다.

- FNV (Fowler–Noll–Vo): 간단하면서도 빠른 해시 알고리즘으로, 해시 테이블 같은 곳에서 자주 사용됩니다.

### Hash 함수 구현
- 효과적인 해시 함수를 설계하는 것이 중요한데, 해시 함수는 주어진 키를 배열의 인덱스로 변환하는 역할을 합니다.
일반적인 해시 함수는 modulus 연산을 이용해 배열의 크기에 맞는 인덱스를 생성합니다.

```python

# 간단한 해시 함수 예시
def simple_hash(key, table_size):
    hash_value = 0
    for char in key:
        hash_value += ord(char)  # 문자의 유니코드 값 사용
    return hash_value % table_size  # 배열 크기에 맞는 인덱스로 변환

# 테이블 크기가 10일 때 key의 해시값 계산
table_size = 10
key = "example_key"
print(simple_hash(key, table_size))  # 해시값 출력
def solve_puzzle(current_state, solution):
    if solution_found(current_state):
        return True
    for next_state in generate_possible_moves(current_state):
        if solve_puzzle(next_state, solution):
            return True
    return False

```