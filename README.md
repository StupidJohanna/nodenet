# NodeNet

Simple Graph Library for Python


Basic Usage:

```py
from nodenet.graph import Graph

g = Graph()
me = g.getVertexOrCreateNew("My House")
jane = g.getVertexOrCreateNew("Jane's House")
flynn = g.getVertexOrCreateNew("Flynn's House")
g.monodirectional("My House", "Jane's House", 5)
g.monodirectional("My House", "Flynn's House", 25)
g.monodirectional("Jane's House", "Flynn's House", 10)
```

This creates a new Graph for us that we can do out calculations on. 

A Built-in Calculation for Graphs is the nodenet.dijkstra.dijkstra() Algorithm.