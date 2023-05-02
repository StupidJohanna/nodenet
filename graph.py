from typing import List, overload
import sys

class Vertex:
    def __init__(self, name, **kwds):
        self.name = name
        self.edges = []

class Edge:
    def __init__(self, weight, dest: Vertex):
        self.weight = weight
        self.dest = dest
    
class Graph:
    def __init__(self):
        self.graphmap = {}
        self.bidirectional = self.addDoubleEdge
        self.monodirectional = self.addEdge

    @classmethod
    def from_matrix(cls, mat):
        """
        Create a Graph from an adjacency Matrix.

        A Matrix is here represented as a list of Lists of Floats.
        For a bidirectional, unweighed graph it could look like this

        [
            [0,1,0,0,0],
            [1,0,1,1,1],
            [0,1,0,0,0],
            [0,1,0,0,0],
            [0,1,0,0,0]
        ]

        Creating a Graph from a Matrix automatically forbids the use of Labels for the Vertices

        
        """
        for n,i in enumerate(mat):
            for x,j in enumerate(i):
                cls.getVertex(x)
                cls.getVertex(n)
                cls.addEdge(x,n,j)
        return cls

    def visual(self, file = sys.stdout):
                
        for vertex in self.graphmap.values():
            print(f"> {vertex.name}", file=file)
            print("\n".join(["-> " + edge.dest.name+ f": {edge.weight}" for edge in vertex.edges]), file=file)


    @overload
    def addEdge(self, source, dest, weight):...

    @overload
    def addEdge(self, vertex: Vertex, edge: Edge):...

    def addEdge(self, *args):
        if len(args) == 2:
            v, w = args
            v.edges.append(w)
        else:
            source, dest, weight = args
            v = self.getVertex(source)
            w = self.getVertex(dest)
            e: Edge = Edge(weight, w)
            print(v.name)
            print(w.name)
            print(e.dest.name)
            print("_")
            v.edges.append(e)
        
    def addDoubleEdge(self, source, dest, weight):
        v = self.getVertex(source)
        w = self.getVertex(dest)
        e: Edge = Edge(weight, w)
        e2: Edge = Edge(weight, v)

        v.edges.append(e)
        w.edges.append(e2)

    def getVertex(self, name):
        if name in self.graphmap:
            v = self.graphmap.get(name)
            return v
        else:
            v = Vertex(name)
            self.graphmap[name] = v
        return v