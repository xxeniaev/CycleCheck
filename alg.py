import collections


class Checker:
    def __init__(self, graph):
        self.graph = graph
        self.first_cycle = []
        self.parent = [-1] * self.graph.size

    def isCyclicConnected(self, s, visited: list):
        adj = self.graph.points

        # Create a queue for BFS
        q = collections.deque()

        visited[s] = True
        q.append(s)

        while q:
            u = q.popleft()
            print("Big ", u, " q=", q)

            for v in adj[u]:
                # print(adj[u])
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
                    self.parent[v] = u
                    print("New step. U=", u, " v=", v, " parent=", self.parent, " q=", q)
                elif self.parent[u] is not v:
                    stop_node = self.parent[v]
                    self.parent[v] = u
                    print("u" , u)
                    print("v" , v)

                    current = v
                    out = []
                    print("current" , current)
                    print("self.parent" , self.parent)
                    while current is not stop_node:
                        out.append(current)
                        current = self.parent[current]
                    out.append(stop_node)
                    self.first_cycle = set(out)
                    print("Answer: ", out)
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
            f.write("N\n" + str(self.first_cycle) + "\n")
            f.close()
