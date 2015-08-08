import unittest
import igraph
import collections
import json

from h3.tree import Tree

"""
Test some properties of the tree structure
"""


class TestTree(unittest.TestCase):

    """
    Test all nodes are inserted by the comparing the total number of nodes in the tree and the number of
    nodes in the input graph
    """

    def test_all_nodes_inserted(self):
        node_number = 500
        edges = igraph.Graph.Barabasi(n=500, m=3, directed=True).spanning_tree(None, True).get_edgelist()
        tree = Tree(0, edges)
        self.assertEqual(node_number, len(tree.nodes))

    """
    Test all nodes are sorted by subtree size by comparing the tree size and the next node's tree size. 
    nodes in the input graph
    """

    def test_sort_tree_size(self):
        edges = igraph.Graph.Barabasi(n=500, m=3, directed=True).spanning_tree(None, True).get_edgelist()
        tree = Tree(0, edges)
        tree.set_subtree_size(edges)
        tree.sort_children_by_tree_size()
        children = tree.nodes[tree.root].children
        tmp_size = len(tree.nodes)
        for n in children:
            self.assertTrue(tree.nodes[n].tree_size <= tmp_size)
            tmp_size = tree.nodes[n].tree_size

if __name__ == '__main__':
    unittest.main()
