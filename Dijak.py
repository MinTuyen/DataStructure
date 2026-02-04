import random
import heapq
class Vertex:
    def __init__(self, label, index):
        self.label = label
        self.index = index
        self.edges = []  # List of (index of adjacent vertex, weight of edge)

    def add_edge(self, to_index, weight):
        self.edges.append((to_index, weight))

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def enqueue(self, item_with_priority):
        heapq.heappush(self.heap, item_with_priority)

    def dequeue(self):
        if not self.is_empty():
            return heapq.heappop(self.heap)
        raise IndexError("dequeue from an empty priority queue")

    def is_empty(self):
        return len(self.heap) == 0

    def peek(self):
        if not self.is_empty():
            return self.heap[0]
        raise IndexError("peek from an empty priority queue")

class Graph:
    def __init__(self):
        self.vertices = []

    def add_vertex(self, label):
        index = len(self.vertices)
        v = Vertex(label, index)
        self.vertices.append(v)
        return v

    def add_edge(self, from_index, to_index, weight=1):
        if from_index < len(self.vertices) and to_index < len(self.vertices):
            self.vertices[from_index].add_edge(to_index, weight)

    def dijkstra(self, start_index):
        # Add code here
        #priority_queue.enqueue((distance, neighbor_index)) (smaller index will be handled first)
        # for neighbor in current_vertes.edges:
        # neighbor_index, weight= neighbor
        distances = {vertex.label: float('inf') for vertex in self.vertices}
        predecessors = {vertex.label: None for vertex in self.vertices}
        distances[self.vertices[start_index].label]=0
        priority_queue=PriorityQueue()
        priority_queue.enqueue((0,start_index))

        while not priority_queue.is_empty :
            distance, current_vertex= priority_queue.dequeue()
            current_vertex=self.vertices[current_vertex]
            current_distance=distances[current_vertex.label]
            if distance>current_distance:
                continue
            for neighbor_index, weight in current_vertex.edges:
                neighbor =self.vertices[neighbor_index]
                new_distance=current_distance + weight
                if new_distance < distance[neighbor.label]:
                    distances[neighbor.label] = new_distance
                    predecessors[neighbor.label]=current_vertex.label
                    priority_queue.enqueue((new_distance, neighbor_index))
        return distances, predecessors








def reconstruct_path(predecessors, start_label, end_label):
    path = []
    step = end_label
    while step != start_label:
        path.append(step)
        step = predecessors[step]
        if step is None:
            return None  # path not reachable
    path.append(start_label)
    path.reverse()
    return path

# Helper function to print result
def print_result(test_id, passed):
    if passed:
        print(f"Test {test_id} Complete")
    else:
        print(f"Test {test_id} Failed")

# Test 0: Testing with an empty graph
def test_0():
    graph = Graph()
    try:
        distances, predecessors = graph.dijkstra(0)
    except IndexError as e:
        # Expected failure as there are no vertices to start Dijkstra's algorithm
        print_result(0, True)
        return
    print_result(0, False)

# Test 1: Testing with a graph that has a single vertex and no edges
def test_1():
    graph = Graph()
    graph.add_vertex('A')
    distances, predecessors = graph.dijkstra(0)
    assert distances == {'A': 0} and predecessors == {'A': None}, "Single vertex test failed"
    print_result(1, True)

# Test 2: Testing with a graph with two vertices connected by a single edge
def test_2():
    graph = Graph()
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_edge(0, 1)
    distances, predecessors = graph.dijkstra(0)
    assert distances == {'A': 0, 'B': 1} and predecessors == {'A': None, 'B': 'A'}, "Test with two vertices failed"
    print_result(2, True)

# Test 3: Testing with a linear graph of three vertices
def test_3():
    graph = Graph()
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    distances, predecessors = graph.dijkstra(0)
    assert distances == {'A': 0, 'B': 1, 'C': 2} and predecessors == {'A': None, 'B': 'A', 'C': 'B'}, "Linear graph test failed"
    print_result(3, True)

# Test 4: Testing with a complete graph of four vertices
def test_4():
    graph = Graph()
    vertices = ['A', 'B', 'C', 'D']
    for v in vertices:
        graph.add_vertex(v)
    weights = [[0, 2, 3, 4], [2, 0, 1, 5], [3, 1, 0, 1], [4, 5, 1, 0]]
    for i in range(4):
        for j in range(4):
            if i != j:
                graph.add_edge(i, j, weights[i][j])
    distances, predecessors = graph.dijkstra(0)
    assert distances['D'] == 4, "Complete graph test failed"
    print_result(4, True)

# Test 5: Testing with a disconnected graph
def test_5():
    graph = Graph()
    graph.add_vertex('A')
    graph.add_vertex('B')
    distances, predecessors = graph.dijkstra(0)
    assert distances == {'A': 0, 'B': float('inf')} and predecessors == {'A': None, 'B': None}, "Disconnected graph test failed"
    print_result(5, True)

# Test 6: Testing with a dense graph of five vertices
def test_6():
    graph = Graph()
    n = 5
    for i in range(n):
        graph.add_vertex(str(i))
    for i in range(n):
        for j in range(n):
            if i != j:
                graph.add_edge(i, j, i + j)
    distances, predecessors = graph.dijkstra(0)
    assert all(distances[str(v)] != float('inf') for v in range(n)), "Dense graph test failed"
    print_result(6, True)

# Test 7: Testing with a linear graph of ten vertices
def test_7():
    graph = Graph()
    for i in range(10):
        graph.add_vertex(f'V{i}')
    for i in range(9):
        graph.add_edge(i, i + 1)
    distances, predecessors = graph.dijkstra(0)
    expected_distances = {f'V{i}': i for i in range(10)}
    expected_predecessors = {f'V0': None}
    expected_predecessors.update({f'V{i}': f'V{i-1}' for i in range(1, 10)})
    assert distances == expected_distances and predecessors == expected_predecessors, "Linear graph (10 vertices) test failed"
    print_result(7, True)

# Test 8: Testing with a complete graph of five vertices with random weights
def test_8():
    random.seed(0)
    graph = Graph()
    vertices = ['A', 'B', 'C', 'D', 'E']
    for v in vertices:
        graph.add_vertex(v)
    for i in range(5):
        for j in range(5):
            if i != j:
                weight = random.randint(1, 10)
                graph.add_edge(i, j, weight)
    distances, _ = graph.dijkstra(0)
    # Test by ensuring no vertex is unreachable
    assert distances == {'A': 0, 'B': 4, 'C': 6, 'D': 1, 'E': 4}, "Complete graph (random weights) test failed"
    print_result(8, True)

# Test 9: Testing with a disconnected graph with three sets of vertices
def test_9():
    graph = Graph()
    # Create three clusters: 0-1-2, 3-4-5, 6-7-8
    for i in range(9):
        graph.add_vertex(f'V{i}')
    for i in [0, 3, 6]:
        graph.add_edge(i, i + 1)
        graph.add_edge(i + 1, i + 2)
    distances, _ = graph.dijkstra(0)
    assert distances['V5'] == float('inf') and distances['V8'] == float('inf'), "Disconnected graph test failed"
    print_result(9, True)

# Test 10: Testing with a dense graph of six vertices
def test_10():
    graph = Graph()
    n = 6  # Dense graph
    for i in range(n):
        graph.add_vertex(str(i))
    for i in range(n):
        for j in range(n):
            if i != j:
                graph.add_edge(i, j, i + j + 1)
    distances, _ = graph.dijkstra(0)
    assert all(dist != float('inf') for dist in distances.values()), "Dense graph test failed"
    print_result(10, True)

# Test 11: Testing with a sparse graph of ten vertices with only three edges
def test_11():
    graph = Graph()
    n = 10  # Sparse graph
    for i in range(n):
        graph.add_vertex(str(i))
    edges = [(0, 1), (1, 2), (2, 3)]
    for (from_idx, to_idx) in edges:
        graph.add_edge(from_idx, to_idx)
    distances, _ = graph.dijkstra(0)
    unreachable = {str(i): float('inf') for i in range(4, 10)}
    assert all(distances[str(i)] != float('inf') for i in range(4)) and all(distances[str(i)] == float('inf') for i in range(4, 10)), "Sparse graph test failed"
    print_result(11, True)

# Test 12: Large linear graph with 20 vertices
def test_12():
    graph = Graph()
    for i in range(20):
        graph.add_vertex(f'V{i}')
    for i in range(19):
        graph.add_edge(i, i + 1)
    distances, predecessors = graph.dijkstra(0)
    expected_distances = {f'V{i}': i for i in range(20)}
    expected_predecessors = {f'V0': None}
    expected_predecessors.update({f'V{i}': f'V{i-1}' for i in range(1, 20)})
    assert distances == expected_distances and predecessors == expected_predecessors, "Large linear graph test failed"
    print_result(12, True)

# Test 13: Large complete graph with 10 vertices with random weights
def test_13():
    random.seed(0)
    graph = Graph()
    n = 10
    for i in range(n):
        graph.add_vertex(f'V{i}')
    for i in range(n):
        for j in range(n):
            if i != j:
                weight = random.randint(1, 15)
                graph.add_edge(i, j, weight)
    distances, _ = graph.dijkstra(0)
    # Test by ensuring no vertex is unreachable
    assert distances == {'V0': 0, 'V1': 7, 'V2': 3, 'V3': 4, 'V4': 6, 'V5': 6, 'V6': 1, 'V7': 2, 'V8': 5, 'V9': 7}, "Large complete graph test failed"
    print_result(13, True)

# Test 14: Disconnected graph with 15 vertices in three clusters
def test_14():
    graph = Graph()
    # Create three clusters: 0-4, 5-9, 10-14
    for i in range(15):
        graph.add_vertex(f'V{i}')
    for cluster_start in [0, 5, 10]:
        for i in range(cluster_start, cluster_start + 4):
            graph.add_edge(i, i + 1)
    distances, _ = graph.dijkstra(0)
    assert distances['V14'] == float('inf') and distances['V9'] == float('inf'), "Disconnected large graph test failed"
    print_result(14, True)

# Test 15: Dense graph with 8 vertices
def test_15():
    graph = Graph()
    n = 8  # Moderately dense graph
    for i in range(n):
        graph.add_vertex(str(i))
    for i in range(n):
        for j in range(n):
            if i != j:
                graph.add_edge(i, j, i + j + 1)
    distances, _ = graph.dijkstra(0)
    assert all(dist != float('inf') for dist in distances.values()), "Dense medium graph test failed"
    print_result(15, True)

# Test 16: Sparse graph with 12 vertices and 5 edges
def test_16():
    graph = Graph()
    n = 12  # Larger sparse graph
    for i in range(n):
        graph.add_vertex(str(i))
    edges = [(0, 1, 1), (1, 2, 1), (2, 3, 1), (3, 4, 1), (10, 11, 1)]  # Adding weights to edges
    for (from_idx, to_idx, weight) in edges:
        graph.add_edge(from_idx, to_idx, weight)
    distances, _ = graph.dijkstra(0)
    # Constructing unreachable dictionary in a compatible way
    unreachable = {str(i): float('inf') for i in range(5, 10)}
    unreachable.update({str(i): float('inf') for i in [11]})
    assert all(distances[str(i)] != float('inf') for i in range(5)) and all(distances[str(i)] == float('inf') for i in unreachable), "Large sparse graph test failed"
    print_result(16, True)

def test_17():
    # Simple linear graph where path reconstruction is straightforward
    graph = Graph()
    for i in range(5):  # Creating a linear graph V0 -> V1 -> V2 -> V3 -> V4
        graph.add_vertex(f'V{i}')
    for i in range(4):
        graph.add_edge(i, i + 1, 1)  # Weight of each edge is 1
    distances, predecessors = graph.dijkstra(0)
    path = reconstruct_path(predecessors, 'V0', 'V4')
    assert path == ['V0', 'V1', 'V2', 'V3', 'V4'], "Path reconstruction failed for linear graph"
    print_result(17, True)

def test_18():
    # Graph with multiple paths and checking for the shortest path
    graph = Graph()
    vertices = ['A', 'B', 'C', 'D', 'E']
    for v in vertices:
        graph.add_vertex(v)
    graph.add_edge(0, 1, 1)  # A -> B
    graph.add_edge(1, 2, 5)  # B -> C
    graph.add_edge(0, 3, 2)  # A -> D
    graph.add_edge(3, 4, 1)  # D -> E
    graph.add_edge(4, 2, 1)  # E -> C, making A -> D -> E -> C shorter than A -> B -> C
    distances, predecessors = graph.dijkstra(0)
    path = reconstruct_path(predecessors, 'A', 'C')
    assert path == ['A', 'D', 'E', 'C'], "Path reconstruction failed for multiple path graph"
    print_result(18, True)

def test_19():
    # Disconnected graph test to ensure path reconstruction handles non-reachable nodes
    graph = Graph()
    for i in range(6):  # 0 to 5
        graph.add_vertex(f'V{i}')
    graph.add_edge(0, 1, 1)
    graph.add_edge(1, 2, 1)  # A cluster V0 -> V1 -> V2
    # V3, V4, and V5 are disconnected from the first cluster
    distances, predecessors = graph.dijkstra(0)
    path = reconstruct_path(predecessors, 'V0', 'V5')
    assert path is None, "Path reconstruction should fail for disconnected graph nodes"
    print_result(19, True)

eval(f"test_{input()}()")