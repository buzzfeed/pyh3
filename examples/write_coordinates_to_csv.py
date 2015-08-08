import igraph
import csv

from h3.tree import Tree

"""
Export layout to csv: x, y, z
"""
if __name__ == '__main__':
    edges = igraph.Graph.Barabasi(n=1000, m=3, directed=True). \
        spanning_tree(None, True).get_edgelist()
    tree = Tree(edges)
    with open('coordinates.csv', 'w+') as fp:
        csv_w = csv.writer(fp, delimiter=',')
        csv_w.writerow(['x', 'y', 'z'])
        for row in tree.get_coordinates():
            csv_w.writerow(row)
