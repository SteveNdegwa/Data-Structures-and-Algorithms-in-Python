import heapq


class Vertex:
    def __init__(self, name):
        self.name = name
        self.min_distance = float('inf')
        self.predecessor = None
        self.adjacency_list = []
        self.visited = False

    def __lt__(self, other):
        return self.min_distance < other.min_distance


class Edge:
    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex


class Dijkstra:
    def __init__(self):
        self.heap = []

    def calculate(self, start_vertex):
        start_vertex.min_distance = 0
        heapq.heappush(self.heap, start_vertex)

        while self.heap:
            actual_vertex = heapq.heappop(self.heap)
            if not actual_vertex.visited:
                for edge in actual_vertex.adjacency_list:
                    u = edge.start_vertex
                    v = edge.target_vertex
                    new_distance = u.min_distance + edge.weight
                    if new_distance < v.min_distance:
                        v.predecessor = u
                        v.min_distance = new_distance
                        heapq.heappush(self.heap, v)
            actual_vertex.visited = True

    @staticmethod
    def shortest_distance(*args):
        for vertex in args:
            print("The shortest distance to %s is: %s kms" % (vertex.name, vertex.min_distance))
            actual_vertex = vertex
            while actual_vertex:
                print(actual_vertex.name)
                actual_vertex = actual_vertex.predecessor
            print()


thika = Vertex("thika")
kamwangi = Vertex("kamwangi")
nakuru = Vertex("nakuru")
eldoret = Vertex("eldoret")
nairobi = Vertex("nairobi")
kiambu = Vertex("kiambu")
mombasa = Vertex("mombasa")

thika.adjacency_list.append(Edge(25, thika, kamwangi))
kamwangi.adjacency_list.append(Edge(25, kamwangi, thika))

thika.adjacency_list.append(Edge(40, thika, nairobi))
nairobi.adjacency_list.append(Edge(40, nairobi, thika))

nairobi.adjacency_list.append(Edge(10, nairobi, kiambu))
kiambu.adjacency_list.append(Edge(10, kiambu, nairobi))

mombasa.adjacency_list.append(Edge(500, mombasa, nairobi))
nairobi.adjacency_list.append(Edge(500, nairobi, mombasa))

nakuru.adjacency_list.append(Edge(180, nakuru, nairobi))
nairobi.adjacency_list.append(Edge(180, nairobi, nakuru))

kamwangi.adjacency_list.append(Edge(250, kamwangi, nakuru))
nakuru.adjacency_list.append(Edge(250, nakuru, kamwangi))

nakuru.adjacency_list.append(Edge(100, nakuru, eldoret))
eldoret.adjacency_list.append(Edge(100, eldoret, nakuru))

algorithm = Dijkstra()
algorithm.calculate(eldoret)
algorithm.shortest_distance(thika, nakuru, mombasa, kiambu, kamwangi, eldoret)
