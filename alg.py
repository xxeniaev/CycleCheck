import collections


class Checker:
    def __init__(self, graph):
        self.graph = graph
        self.parent = [[]] * self.graph.size
        self.first_cycle = []

    def isCyclicConnected(self, s, visited: list):
        adj = self.graph.points

        # Create a queue for BFS
        q = collections.deque()

        visited[s] = True
        q.append(s)

        while q:
            u = q.popleft()

            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
                    self.parent[v] = [u] + self.parent[u]
                elif self.parent[u][0] is not v:
                    flag = False
                    for i in range(len(self.parent[v])):
                        for j in range(len(self.parent[u])):
                            if self.parent[v][i] == self.parent[u][j]:
                                if flag:
                                    continue
                                flag = True
                                curV = self.parent[v].index(self.parent[v][i]) + 1
                                curU = self.parent[u].index(self.parent[v][i]) + 1
                                cycle = self.parent[v][:curV] + self.parent[u][:curU] + [u, v]
                                self.first_cycle = list(map(lambda x: x + 1, cycle))
                    return True
        return False

    def isCyclicDisconnected(self):
        n = self.graph.size
        visited = [False] * n

        for i in range(n):
            if not visited[i] and self.isCyclicConnected(i, visited):
                return False
        return True

    def print_results(self):
        if self.isCyclicDisconnected():
            f = open("out.txt", "a")
            f.write("A\n")
            f.close()
        else:
            f = open("out.txt", "a")
            f.write("N\n" + str(set(self.first_cycle)) + "\n")
            f.close()
