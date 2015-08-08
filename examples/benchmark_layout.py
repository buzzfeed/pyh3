import igraph
import collections
import logging
import json
import csv
from timeit import Timer

from h3.tree import Tree

"""
Benchmark the performance of getting layout
"""

setup = """
import igraph
from h3.tree import Tree
edges = [(parent, child) for parent, child in igraph.Graph.Barabasi(n={0}, m=3, directed=True).\
    spanning_tree(None, True).get_edgelist()]
"""

stmt = """
Tree(edges)
"""

if __name__ == '__main__':
    print "Nodes\tTime (s)"
    print "---------------"
    for n in xrange(1, 5):
        N = int(10**n)
        t = Timer(setup=setup.format(N),
                  stmt=stmt).timeit(number=5)
        print "N={0}\tt={1:.4f}".format(N, t)
