# Hash Collision 해결 방법

## 체이닝(Chaining):

- 해시 충돌이 발생하면, 해당 인덱스에 리스트(Linked List) 형태로 여러 데이터를 저장하는 체이닝을 통해 해결할 수 있습니다.

```python

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # 체이닝을 위한 리스트

    def _hash(self, key):
        return simple_hash(key, self.size)

    def insert(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value  # 키가 같으면 값 업데이트
                return
        self.table[index].append([key, value])  # 체이닝

    def get(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

# 해시 테이블 생성 및 데이터 저장
hash_table = HashTable(10)
hash_table.insert("example_key", "example_value")
hash_table.insert("another_key", "another_value")

# 데이터 검색
print(hash_table.get("example_key"))  # 'example_value' 출력

```

## 오픈 어드레싱(Open Addressing):
- 오픈 어드레싱을 사용해 충돌을 해결할 수 있습니다. 
  이 방법은 충돌이 발생하면 새로운 빈 슬롯을 찾아 데이터를 저장하는 방식입니다. 대표적인 방법으로 선형 탐색(Linear Probing)과 이차 탐색(Quadratic Probing)이 있습니다.

```python

class OpenAddressingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return simple_hash(key, self.size)

    def insert(self, key, value):
        index = self._hash(key)
        while self.table[index] is not None:
            index = (index + 1) % self.size  # 선형 탐색
        self.table[index] = (key, value)

    def get(self, key):
        index = self._hash(key)
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
        return None

```