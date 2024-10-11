# Backtracking

- Backtracking: 모든 가능성을 탐색하는 방법으로, 해를 찾다가 막히면 이전 상태로 돌아가서 다른 경로를 탐색하는 방식.

- 주로 퍼즐 문제나 최적화 문제에서 사용됨.

- Backtracking은 N-Queen 문제, Sudoku 문제와 같은 퍼즐에서 사용.

```python

def solve_puzzle(current_state, solution):
    if solution_found(current_state):
        return True
    for next_state in generate_possible_moves(current_state):
        if solve_puzzle(next_state, solution):
            return True
    return False

```