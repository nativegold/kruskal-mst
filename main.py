class Kruskal:
    def __init__(self, graph, n):
        self.graph = graph  # 입력 그래프를 인접 행렬로
        self.n = n  # 정점의 개수
        self.parent = [-1] * n  # 부모 리스트 초기화
        self.mst_e = []  # MST에 포함된 간선을 저장하는 리스트
        self.mst_weight = 0  # MST의 총 가중치

    # 정점 u가 속한 집합의 루트를 찾는 메소드
    def find(self, u):
        if self.parent[u] >= 0:  # u가 속한 집합의 루트가 아닐 경우
            self.parent[u] = self.find(self.parent[u])  # 재귀적으로 u의 루트 찾기
            return self.parent[u]
        else:  # u가 속한 집합의 루트일 경우
            return u

    # 정점 u와 v가 속한 집합을 합치는 메소드
    def union(self, u, v):
        u_root = self.find(u)
        v_root = self.find(v)
        if self.parent[u_root] <= self.parent[v_root]:
            self.parent[u_root] += self.parent[v_root]
            self.parent[v_root] = u_root
        else:
            self.parent[v_root] += self.parent[u_root]
            self.parent[u_root] = v_root

    # 크루스칼 알고리즘으로 그래프의 MST를 찾는 메소드
    def kruskal_mst(self):
        E = []  # 그래프의 모든 간선을 저장하는 리스트
        edges = 0  # MST에 포함된 간선의 개수
        for i in range(0, self.n):  # 인접 행렬을 순회하여 모든 간선 찾기
            for j in range(0, self.n):
                if self.graph[i][j] > 0:
                    E.append((i, j, self.graph[i][j]))  # 간선 (i, j)와 가중치 self.graph[i][j]를 리스트 E에 추가
                    self.graph[j][i] = 0  # 중복 간선 피하기
        E.sort(key=lambda x: x[2])  # 간선들을 가중치의 오름차순으로 정렬

        while edges < self.n - 1:  # MST에 (n - 1)개의 간선이 포함될 때까지
            u, v, weight = E.pop(0)  # 가장 작은 가중치를 가진 간선 선택
            if self.find(u) != self.find(v):  # u와 v가 다른 집합에 속해 있을 경우
                self.union(u, v)  # u와 v가 속한 집합 합치기
                self.mst_e.append((u, v))  # 간선 (u, v)를 MST에 추가
                edges += 1  # MST에 포함된 간선의 개수 증가
                self.mst_weight += weight  # 간선의 가중치를 MST의 총 가중치에 추가
        self.print_results()  # 결과 출력

    # 알고리즘 실행 결과를 출력하는 메소드
    def print_results(self):
        print(f"Parent: {self.parent}")
        print(f"MST에서 선택된 간선: {self.mst_e}")
        print(f"MST의 총 가중치: {self.mst_weight}")


if __name__ == '__main__':
    Kruskal([
        [0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
    ], 9).kruskal_MST()
