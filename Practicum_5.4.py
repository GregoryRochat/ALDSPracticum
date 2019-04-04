import math
INFINITY = math.inf


class Queue(list):
    def __init__(self, a=[]):
        list.__init__(self, a)

    def dequeue(self):
        return self.pop(0)

    def enqueue(self, x):
        self.append(x)

    def len(self):
        return len(self)


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
    BFS(G, V[0])
    for v in V:
        if v.distance == INFINITY:
            return False
    return True


def no_cycles(G):
    """
    Function that determines whether the graph has cycles or not.
    Parameters
    ----------
    G : Graph
        The graph to be evaluated.
    Return
    ------
    : bool
        Returns True if the graph doesn't have cycles and False if it does.
    """
    V = vertices(G)
    for s in V:
        s.predecessor = None
        s.distance = 0
        for v in V:
            if v != s:
                v.distance = INFINITY
        q = Queue()
        q.enqueue(s)
        while q:
            vx = q.dequeue()
            lst = []
            for v in G[vx]:
                if vx.predecessor != v:
                    lst.append(v)
            for v in lst:
                if v.distance == INFINITY:
                    v.distance = vx.distance + 1
                    v.predecessor = vx
                    q.enqueue(v)
                else:
                    return False
    return True


def get_bridges(G):
    """
    Function that determines whether the given graph has bridges and returns those.
    Parameters
    ----------
    G : Graph
        The graph to be evaluated.

    Return
    ------
    bridges: list
        A list of tuples as the bridges found.

    """
    bridges = []
    tempG = G
    edgelist = edges(tempG)
    for edge in edgelist:
        if type(tempG[edge[0]]) == list:
            tempG[edge[0]].remove(edge[1])
            tempG[edge[1]].remove(edge[0])
            BFS(tempG, edge[0])
            if edge[1].distance == INFINITY:
                bridges.append(edge)
            tempG[edge[0]].append(edge[1])
            tempG[edge[1]].append(edge[0])
        if type(tempG[edge[0]]) == dict:
            if tempG[edge[0]][edge[1]]['n'] == 1:
                edge1 = tempG[edge[0]].pop(edge[1])
                edge0 = tempG[edge[1]].pop(edge[0])
                BFS(tempG, edge[0])
                if edge[1].distance == INFINITY:
                    bridges.append(edge)
                tempG[edge[0]][edge[1]] = edge1
                tempG[edge[1]][edge[0]] = edge0
    return bridges


def is_strongly_connected(G):
    """
    Function that determines whether each node in the graph can be approached from all other nodes.

    Parameters
    ----------
    G : Graph
        The graph to be evaluated.

    Return
    ------
    : bool
        Returns True if the graph has strong connections and False if it does not.
    """
    tempG = G
    result = is_connected(tempG)
    if not result:
        return result
    edgelist = edges(tempG)
    path = dict()
    for edge in edgelist:
        if edge[0] in path.keys():
            path[edge[0]].append(edge[1])
        else:
            path[edge[0]] = [edge[1]]
    return result and is_connected(path)


def testis_strongly_connected():
    """
    Function that tests the is_strongly_connected(G) function.

    """
    v = [Vertex(i) for i in range(8)]

    test_G1 = {v[0]: [v[1]],
               v[1]: [v[2]],
               v[2]: [v[0]]
               }

    test_G2 = { v[0]: [v[1]],
                v[2]: [v[0], v[1]],
                }

    print("Testing a strongly connected graph. \n")
    print("Vertices:", vertices(test_G1))
    print("Edges:", edges(test_G1))
    if is_strongly_connected(test_G1):
        print("Test successful, came back as strongly connected.")
    else:
        print("Test failed, didn't came back as strongly connected.")

    print("Testing a strongly connected graph. \n")
    print("Vertices:", vertices(test_G2))
    print("Edges:", edges(test_G2))
    if is_strongly_connected(test_G2):
        print("Test failed, came back as strongly connected.")
    else:
        print("Test successful, didn't came back as strongly connected.")


testis_strongly_connected()

