import unittest
import igraph
import collections
import json

from h3.tree import Tree

"""
Customized print tree to terminal
Note: implemented by recursion, not scalable to a large number of nodes, 
      only suitable for a small number of nodes
"""


def print_tree(tree, node_id, depth=0):
    children = tree.nodes[node_id].children
    total_children_area = 0
    for child in children:
        total_children_area += tree.nodes[child.node_id].area
    print "\t" * tree.nodes[node_id].depth, \
        "{0}, radius: {1}, parent: {2}, area: {3}, total_children_area: {4}" \
        .format(node_id,
                tree.nodes[node_id].radius,
                tree.nodes[node_id].parent,
                tree.nodes[node_id].area,
                total_children_area)
    for child in children:
        print_tree(tree, child.node_id, depth)

if __name__ == '__main__':
    edges = ((child, parent) for parent, child in igraph.Graph.Tree(40, 3).get_edgelist())
    tree = Tree(edges)
    print_tree(tree, 0)
