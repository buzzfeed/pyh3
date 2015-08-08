import igraph
import collections
import logging
import json

from h3.tree import Tree

"""
An example for drawing a random spanning tree with 500 nodes with tagging and equators while logging. 
"""
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        filename="log",
                        filemode="w+",
                        format="%(asctime)-10s \
                        %(levelname)-6s %(message)s")
    log = logging.getLogger()
    edges = igraph.Graph.Barabasi(n=500, m=3, directed=True).spanning_tree(None, True).get_edgelist()
    logging.info(edges)
    tree = Tree(edges)
    tree.scatter_plot()
