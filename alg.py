import collections


class Checker:
    def __init__(self, graph):
        self.graph = graph

    # def dfs(self, start, visited=None):
    #     if visited is None:
    #         visited = set()
    #     visited.add(start)
    #     print(start)
    #     for next in self.graph.points[start]:
    #         if next not in visited:
    #             self.dfs(next, visited)
    #     return visited

    def bfs(self, root):
        visited, queue = set(), collections.deque([root])
        visited.add(root)
        bfs_str = ''
        bfs_str += str(root)
        while queue:
            vertex = queue.popleft()
            for neighbour in self.graph.points[vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
                    bfs_str += str(neighbour)
        return bfs_str
