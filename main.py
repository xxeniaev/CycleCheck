from graph import ReadGraphsFromFile as Reader
from alg import Checker

if __name__ == '__main__':
    reader = Reader("in.txt")

    graph_list = reader.reading()

    f = open("out.txt", "w")
    f.close()

    for graph in graph_list:
        checker = Checker(graph)
        print(graph.points)
        # checker.bfs(1)
        # print(checker.bfs(1))
        # if checker.isCyclic():
        #     print("Graph contains cycle!")
        # else:
        #     print("Graph does not contain cycle ")
        checker.print_results()

