# Tree와 Graph의 차이점:

# Tree #
- 사이클이 없는 연결된 그래프. 부모-자식 관계가 있는 계층 구조.

# Graph #
- 노드와 엣지로 구성된 구조로, 사이클이 있을 수 있음. 방향성 여부에 따라 방향 그래프와 무방향 그래프로 구분.

## Tree와 Graph의 특징:

# Tree #
- 노드 간 계층적 관계를 나타내는 데 주로 사용되며, 하나의 루트 노드를 중심으로 하위 노드들이 연결되어 있다.

# Graph #
- 노드와 엣지로 이루어져 있으며, 복잡한 상호 관계나 네트워크 구조를 나타내는 데 적합하다.

# 구현(python)

# Tree #
- Tree는 보통 Node 클래스와 자식 노드를 관리하는 방식으로 구현.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Graph #
- Graph는 인접 리스트나 인접 행렬로 구현.

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        self.adj_list[u].append(v)