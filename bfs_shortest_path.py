class Graph:
    def bfs_path(self, start, end):
        visited = []
        to_visit = [start]
        path = {start: None}
        while to_visit:
            current = to_visit.pop(0)
            if current == end:
                path_list = []
                while current:
                    path_list.append(current)
                    current = path[current]
                path_list.reverse()
                return path_list
            sorted_neighbors = sorted(self.graph[current])
            for neighbor in sorted_neighbors:
                if neighbor not in visited:
                    to_visit.append(neighbor)
                    visited.append(neighbor)
                    path[neighbor] = current
        return None

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
