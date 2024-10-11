# 실사용 예

- 데이터베이스 인덱싱
해시는 데이터베이스에서 데이터를 빠르게 검색하는 데 자주 사용됩니다. 테이블에서 데이터 검색 시, 해시 함수는 특정 열(키)의 값을 해시화하여 저장 위치를 결정합니다. 이로 인해 데이터 검색 속도가 크게 향상됩니다.

- 캐시 시스템
웹 브라우저나 서버에서 자주 사용하는 파일이나 데이터를 캐싱할 때 해시를 사용합니다. 각 파일이나 데이터를 해시화하여 빠르게 저장하고 나중에 동일한 데이터를 효율적으로 검색할 수 있습니다. 예를 들어, Memcached와 같은 캐시 시스템에서 데이터를 저장할 때 키-값 쌍을 해시 테이블로 관리합니다.

- 데이터 중복 제거
해시는 파일 중복 제거 시스템에서 파일의 해시값을 생성해 고유한 파일인지 여부를 빠르게 확인하는 데 사용됩니다. 이는 파일 저장 공간을 절약하고 불필요한 중복을 방지하는 데 유용합니다.

- 비밀번호 저장
웹 애플리케이션에서 비밀번호를 안전하게 저장하기 위해 해시 함수가 사용됩니다. 비밀번호를 해시하여 저장하고, 사용자가 로그인할 때 입력한 비밀번호도 동일한 해시 함수를 통해 해시화하여 비교하는 방식입니다. SHA-256 같은 보안 해시 함수가 여기에 사용됩니다.

## Key에 따라 활용할 수 있는 Hash Function의 종류 및 실례 적용 코드

- 간단한 해시 함수
모듈로 해시 함수는 문자열의 각 문자를 숫자로 변환한 후 이를 더한 값을 배열 크기로 나누는 방식입니다. 이 방법은 간단하지만 충돌이 발생할 가능성이 높아 더 정교한 해시 함수가 필요할 수 있습니다.

```python

def simple_mod_hash(key, table_size):
    return sum(ord(c) for c in key) % table_size

table_size = 10
key = "example"
print(simple_mod_hash(key, table_size))  # 7과 같은 인덱스 출력

```

- MD5 (Message Digest Algorithm 5)
MD5는 데이터의 무결성을 확인하기 위해 파일의 고유한 해시값을 생성하는 데 자주 사용됩니다. 현재는 보안성이 취약해 암호화 목적으로 사용되지 않지만, 여전히 데이터 무결성 확인 등에 유용합니다.

```python

import hashlib

def md5_hash(key):
    return hashlib.md5(key.encode()).hexdigest()

key = "example_key"
print(md5_hash(key))  # MD5 해시값 출력

```

- SHA-256 (Secure Hash Algorithm 256-bit)
SHA-256은 암호화된 해시 값을 생성하는 보안 해시 함수입니다. 보안이 필요한 시스템(예: 비밀번호 저장, 데이터 서명)에서 많이 사용됩니다.

```python

import hashlib

def sha256_hash(key):
    return hashlib.sha256(key.encode()).hexdigest()

key = "secure_key"
print(sha256_hash(key))  # SHA-256 해시값 출력

```

- FNV-1a (Fowler-Noll-Vo Hash Function)
FNV-1a는 간단하면서도 빠르게 해시값을 생성하는 알고리즘입니다. 주로 해시 테이블에서 키를 해싱할 때 사용됩니다.

```python

def fnv1a_hash(key):
    fnv_prime = 0x1000193
    hash_value = 0x811c9dc5  # FNV 오프셋 기준값
    for char in key:
        hash_value ^= ord(char)
        hash_value *= fnv_prime
    return hash_value & 0xffffffff  # 32비트 마스킹

key = "example_key"
print(fnv1a_hash(key))  # FNV-1a 해시값 출력

```

- CRC32 (Cyclic Redundancy Check)
CRC32는 데이터를 전송하거나 저장할 때 오류를 검출하기 위한 해시 함수로 사용됩니다. 네트워크 통신에서 전송된 데이터의 무결성을 확인하는 데 자주 쓰입니다.

```python

import zlib

def crc32_hash(key):
    return zlib.crc32(key.encode())

key = "data_to_check"
print(crc32_hash(key))  # CRC32 해시값 출력

```