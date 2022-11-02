# 크루스칼 알고리즘 구현
# 20181447 김동운

# parent 전역 변수로 지정
global parent

# parent 리스트를 정점 갯수 만큼 초기화
def init_set(n):
    global parent
    parent = [-1] * n


# 가중치를 이용한 union 함수
def union(u, v):
    global parent

    # 루트 탐색
    u_root = find(u)
    v_root = find(v)

    # 가중치를 이용하여 union 연산
    if parent[u_root] <= parent[v_root]:    # v_root
        parent[u_root] += parent[v_root]
        parent[v_root] = u_root
    else:
        parent[v_root] += parent[u_root]
        parent[u_root] = v_root


# 붕괴 법칙을 이용한 find 함수
def find(u):
    global parent
    if parent[u] >= 0:  # 자신이 소속된 집합의 루트가 아닐 경우
        parent[u] = find(parent[u])
        return parent[u]
    else:   # 자신이 소속된 집합의 루트일 경우
        return u


# 크루스칼 알고리즘
def krusukal_MST(matrix, n: int):
    global parent  # 전역 변수로 선언
    E = []  # 비용인접행렬을 튜플 (u, v, 가중치) 변환하여 정렬하기 위한 리스트
    MST_E = []  # MST에 선택된 간선 (u, v)을 추가하기 위한 리스트
    edges = 0   # 간선 수
    MST_weight = 0  # MST 가중치

    # 비용인접행렬을 (u, v, 가중치) 형태로 E 리스트에 추가
    for i in range(0, n):
        for j in range(0, n):
            if matrix[i][j] > 0:
                E.append((i, j, matrix[i][j]))
                matrix[j][i] = 0

    # (u, v, 가중치) 간선의 가중치에 따라 오름차순으로 정렬
    E.sort(key=lambda x: x[2])

    # parent 리스트를 정점 개수 만큼 초기화
    init_set(n)

    # '크루스칼 알고리즘 MST의 간선의 개수(n - 1)'만큼 반복
    while edges < n - 1:
        u, v, weight = E.pop(0) # 리스트의 pop(0) 함수로 가중치가 작은 간선부터 가져오기 (u: 정점, v: 정점, weight: 가중치)

        if find(u) != find(v):
            union(u, v)  # 간선 u의 집합과 간선 v의 집합 union
            MST_E.append((u, v))  # MST에 간선 추가
            edges += 1  # MST의 간선 수 +1
            MST_weight += weight    # MST의 가중치 합산

    # 출력
    print(f"parent: {parent}")
    print(f"MST 선택한 간선: {MST_E}")
    print(f"MST 가중치: {MST_weight}")

    # END


# main
if __name__ == '__main__':
    krusukal_MST([  # 비용인접행렬, n
        [0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
    ], 9)
