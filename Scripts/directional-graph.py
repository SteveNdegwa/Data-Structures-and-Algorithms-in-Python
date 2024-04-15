class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.adj_list = []


class Graph(object):
    def __init__(self):
        self.vertex_list = []

    def search_vertex(self, name):
        if not self.vertex_list:
            return None
        for vertex in self.vertex_list:
            if vertex.name == name:
                return vertex
        return None

    def add_vertex(self, name):
        vertex_exists = self.search_vertex(name)
        if vertex_exists:
            return False
        new_vertex = Vertex(name)
        self.vertex_list.append(new_vertex)
        return True

    def remove_vertex(self, name):
        vertex = self.search_vertex(name)
        if not vertex:
            return False
        [v.adj_list.remove(edge) for v in self.vertex_list for edge in v.adj_list if edge[0] == vertex]
        self.vertex_list.remove(vertex)
        return True

    def add_edge(self, name1, name2, distance):
        vertex1 = self.search_vertex(name1)
        vertex2 = self.search_vertex(name2)
        if vertex1 and vertex2:
            vertex1.adj_list.append((vertex2, distance))
            return True
        return False

    def remove_edge(self, name1, name2):
        vertex1 = self.search_vertex(name1)
        vertex2 = self.search_vertex(name2)
        if vertex1 and vertex2:
            [vertex1.adj_list.remove(v) for v in vertex1.adj_list if v[0] == vertex2]
            return True
        return False

    def bfs(self, root):
        root = self.search_vertex(root)
        queue = [root]
        if not root:
            return
        while queue:
            current = queue.pop(0)
            if current.visited:
                continue
            current.visited = True
            print(current.name)
            [queue.append(v[0]) for v in current.adj_list]

    def dfs(self, root):
        root = self.search_vertex(root)
        if not root:
            return
        if root.visited:
            return
        root.visited = True
        [self.dfs(v[0].name) for v in root.adj_list]
        print(root.name)

    def print_graph(self):
        [print(vertex.name, [(v[0].name, v[1]) for v in vertex.adj_list]) for vertex in self.vertex_list if self.vertex_list]


graph = Graph()
graph.add_vertex("thika")
graph.add_vertex("kamwangi")
graph.add_vertex("nairobi")
graph.add_vertex("kiambu")
graph.add_vertex("nakuru")
graph.add_vertex("eldoret")
graph.add_vertex("mombasa")
graph.add_edge("thika", "kamwangi", 25)
graph.add_edge("kamwangi", "thika", 25)
graph.add_edge("thika", "nairobi", 40)
graph.add_edge("nairobi", "thika", 40)
graph.add_edge("nairobi", "kiambu", 10)
graph.add_edge("kiambu", "nairobi", 10)
graph.add_edge("nairobi", "nakuru", 180)
graph.add_edge("nakuru", "nairobi", 180)
graph.add_edge("mombasa", "nairobi", 500)
graph.add_edge("nairobi", "mombasa", 500)
graph.add_edge("kamwangi", "nakuru", 250)
graph.add_edge("nakuru", "kamwangi", 250)
graph.add_edge("nakuru", "eldoret", 100)
graph.add_edge("eldoret", "nakuru", 100)
graph.print_graph()

