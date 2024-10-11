# Tree 탐색 방법

## 전위 순회(Pre-order Traversal)
루트 → 왼쪽 자식 → 오른쪽 자식
예: 1 -> 2 -> 4 -> 5 -> 3

```python
def pre_order(node):
    if node:
        print(node.value)
        pre_order(node.left)
        pre_order(node.right)

```

## 중위 순회(In-order Traversal):
왼쪽 자식 → 루트 → 오른쪽 자식
예: 4 -> 2 -> 5 -> 1 -> 3

```python

def in_order(node):
    if node:
        in_order(node.left)
        print(node.value)
        in_order(node.right)

```

## 후위 순회(Post-order Traversal):
왼쪽 자식 → 오른쪽 자식 → 루트
예: 4 -> 5 -> 2 -> 3 -> 1

```python

def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.value)
        
```