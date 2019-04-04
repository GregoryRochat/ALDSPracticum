import math
INFINITY = math.inf


class Queue(list):
    def __init__(self, a=[]):
        list.__init__(self, a)

    def dequeue(self):
        return self.pop(0)

    def enqueue(self, x):
        self.append(x)

    def getlen(self):
        return len(self.a)


class Vertex:
    def __init__(self, data):
        self.data = data

    def __repr__(self):  # voor afdrukken
        return str(self.data)

    def __lt__(self, other):  # voor sorteren
        return self.data < other.data


def vertices(G):
    return sorted(G)


def edges(G):
    return [(u, v) for u in vertices(G) for v in G[u]]


def clear(G):
    for v in vertices(G):
        k = [e for e in vars(v) if e != 'data']
        for e in k:
            delattr(v, e)


def BFS(G, s):
    V = vertices(G)
    s.predecessor = None                    # s krijgt het attribuut 'predecessor'
    s.distance = 0                          # s krijgt het attribuut 'distance'
    for v in V:
        if v != s:
            v.distance = INFINITY           # v krijgt het attribuut 'distance'
    q = Queue()
    q.enqueue(s)                            # plaats de startnode in de queue
    #    print("q:", q)
    while q:
        u = q.dequeue()
        for v in G[u]:
            if v.distance == INFINITY:      # v is nog niet bezocht
                v.distance = u.distance + 1
                v.predecessor = u           # v krijgt het attribuut 'predecessor'
                q.enqueue(v)                # plaats v in de queue


def show_tree_info(G):
    print('tree:', end=' ')
    for v in vertices(G):
        print('(' + str(v), end='')
        if hasattr(v, 'distance'):
            print(',d:' + str(v.distance), end='')
        if hasattr(v, 'predecessor'):
            print(',p:' + str(v.predecessor), end='')
        print(')', end=' ')
    print()


def show_sorted_tree_info(G):
    print('sorted tree:')
    V = vertices(G)
    #    V = [v for v in V if hasattr(v,'distance') and hasattr(v,'predecessor')]
    V.sort(key=lambda x: (x.distance, x.predecessor))
    d = 0
    for v in V:
        if v.distance > d:
            print()
            d += 1
        print('(' + str(v) + ',d:' + str(v.distance) + ',p:'
              + str(v.predecessor), end='')
        print(')', end=' ')
    print()


def path_BFS(G, u, v):
    BFS(G, u)
    a = []
    if hasattr(v, 'predecessor'):
        current = v
        while current:
            a.append(current)
            current = current.predecessor
        a.reverse()
    return a


def is_connected(G):
    """
    Function that determines whether each node in the given graph is connected, directly or indirectly, with every other
    node.

    Parameters
    ----------
    G : Graph
        The graph to be evaluated.
    Return
    ------
    bool :
        Returns True if the graph has connections and False if it doesn't.
    """
    V = vertices(G)
    BFS(G, V[1])

    for v in V:
        if not hasattr(v, 'predecessor'):
            return False
    return True


def testgraphconnections():
    """
    Function that tests the is_connected(G) function.

    """
    v = [Vertex(i) for i in range(8)]

    test_G1 = { v[0]: [v[4], v[5]],
                v[1]: [v[4], v[5], v[6]],
                v[2]: [v[4], v[5], v[6]],
                v[3]: [v[7]],
                v[4]: [v[0], v[1], v[2], v[5]],
                v[5]: [v[0], v[1], v[2], v[4]],
                v[6]: [v[1], v[2]],
                v[7]: [v[3]]}

    test_G2 = { v[0]: [v[4], v[5]],
                v[1]: [v[4], v[5], v[6]],
                v[2]: [v[4], v[5], v[6]],
                v[4]: [v[0], v[1], v[2], v[5]],
                v[5]: [v[0], v[1], v[2], v[4]],
                v[6]: [v[1], v[2]]}

    print("Testing a non-connected graph:\n")
    print("Vertices:", vertices(test_G1))
    print("Edges:", edges(test_G1))
    BFS(test_G1, vertices(test_G1)[0])
    show_tree_info(test_G1)
    if is_connected(test_G1):
        print("Failed test, came back as connected.")
    else:
        print("Successful test, came back as unconnected")

    print("\nTesting a connected graph:\n")
    print("Vertices:", vertices(test_G2))
    print("Edges:", edges(test_G2))
    BFS(test_G2, vertices(test_G2)[0])
    if not is_connected(test_G2):
        print("Failed test, came back as unconnected.")
    else:
        print("Successful test, came back as connected")


testgraphconnections()
