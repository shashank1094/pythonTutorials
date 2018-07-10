class Graph:
    def __init__(self, n):
        self.num = n
        self.nodes = {}
        for i in range(1, n + 1):
            self.nodes[i] = []

    def connect(self, x, y):
        self.nodes[x].append(y)
        self.nodes[y].append(x)

    def find_all_distances(self, s):
        distances = {}
        queue_ = []
        distance_till_now = 0
        queue_.append((s, distance_till_now))
        visited = set()
        while len(queue_) > 0:
            current_node, current_distance = queue_.pop(0)
            if current_node not in distances:
                distances[current_node] = current_distance
            elif distances[current_node] > current_distance:
                distances[current_node] = current_distance
            else:
                continue
            for child in sorted(self.nodes[current_node]):
                if child not in visited:
                    queue_.append((child, current_distance + 6))
                visited.add(current_node)

        for node in range(1, self.num + 1):
            if node in distances:
                if distances[node] == 0:
                    continue
                else:
                    print(distances[node], end=" ")
            else:
                print("-1", end=" ")

        print()


t = int(input())
for i in range(t):
    num_of_nodes, num_of_edges = [int(value) for value in input().split()]
    graph = Graph(num_of_nodes)
    for i in range(num_of_edges):
        from_, to_ = [int(x) for x in input().split()]
        graph.connect(from_, to_)
    start_node = int(input())
    graph.find_all_distances(start_node)
