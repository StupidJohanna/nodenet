from graph import Graph, Edge, Vertex
import sys

def dijkstra(g: Graph, start: Vertex):
    """
    The Dijkstra Algorithm is - as of now - the best Pathfinding Algorithm we have,
    finding the shortest path to every point from one starting vertex.

    -- g: graph.Graph : A Graph() Instance the Algorithm is supposed to be applied on
    -- start: graph.Vertex : A Vertex() Instance that's on g and acts as the start point
    """
    p = []
    dist = Graph()
    for _,v in g.graphmap.items():
        v.dist = sys.float_info.max
        v.seen = False
        v.prev = None
    start.dist = 0
    dist = g
    dist.monodirectional(Vertex("."), Edge(0,start))
    p.append(Edge(0,start))
    while p:
        best = p.pop()
        v = best.dest
        if v.seen: continue
        v.seen = True
        for e in v.edges:
            w = e.dest
            c = e.weight
            if w.dist > v.dist + c:
                w.dist = v.dist + c
                w.prev = v
                t = Edge(w.dist, w)
                dist.monodirectional(v, t)
                p.append(t)

    return dist