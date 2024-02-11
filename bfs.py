class Graph:
    def breadth_first_search(self, v):
        visited = []
        to_visit = []
        to_visit.append(v)

        while to_visit:
            vertex = to_visit.pop(0)
            if vertex not in visited:
                visited.append(vertex)
                sorted_neighbors = sorted(self.graph[vertex])
                for neighbor in sorted_neighbors:
                    to_visit.append(neighbor)
        return visited

    # don't touch below this line

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    def __repr__(self):
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result
