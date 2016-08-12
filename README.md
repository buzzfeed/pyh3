#h3py - H3 in Python 

h3py is an pure python implementation of [H3](https://graphics.stanford.edu/papers/munzner_thesis/) from Dr. Tamara Munzner's Ph.D. dissertation in Stanford University, June 2000. It provides a scalable, high performance and interactive graph visualization in 3D hyperbolic space. We found this algorithm is good at tracking and presenting massive amounts of posts sharing across different social networks over time. There's also a Java3D implementation called [Walrus](https://www.caida.org/tools/visualization/walrus/) by Center for Applied Internet Data Analysis (CAIDA), last release in 2005.

The motivation behind this project was to build a Python version of H3 for visualizing data from the Pound project at Buzzfeed. Songxiao Zhang, working with Adam Kelleher of Buzzfeed's Optimization Squad successfully managed to implement this package, capable of laying out trees on the order of millions of nodes in a matter of minutes. Andrew, Adam's brother, took care of minor cleanups packaging. 

## Quick View
```
├── LICENSE
├── README.md
├── examples
│   ├── __init__.py
│   ├── benchmark_layout.py
│   ├── print_tree_to_console.py
│   ├── render_tree_as_scatterplot.py
│   └── write_coordinates_to_csv.py
├── h3
│   ├── __init__.py
│   ├── h3math.py
│   ├── node.py
│   └── tree.py
├── setup.py
└── test
    └── unit
            └── test_tree.py
```
* `node.Node`: The node data structure provides a nice model for bookkeeping during layout.<br>
* `tree.Tree`: The bulk of the algorithm takes place here. You simply pass an edgelist and the Tree is laid out. 
`h3math`: This should be considered "private". These are the nuts and bolts, some building blocks of the h3 algorithm. 
`examples`: Start here! A few basic examples will show you what this baby can do, and make your life easier as you try implementing it. 

## Get Started
You can install this via pip from the package index as 

```
pip install h3py
```

Or you can clone from github and install using setuptools:

```
git clone https://github.com/buzzfeed/pyh3 ./pyh3;
cd pyh3;
python setup.py install
```

Try it out on a simple graph!
```
>>> import igraph
>>> from h3.tree import Tree
>>> edges = igraph.Graph.Barabasi(n=500, m=3, directed=True).spanning_tree(None, True).get_edgelist()
>>> tree = Tree(edges)
>>> tree.scatter_plot(equators=False, tagging=False)
```

## Results
![screenshot 2015-08-03 18 34 25](https://cloud.githubusercontent.com/assets/4334970/9049302/87de9d04-3a0e-11e5-91a5-06fb0baba28b.png)
h3py in matplotlib with 50,000 nodes, takes like 30s to get the plot on my machine. This is a proof-of-the-concept that is very easy to get from python only. Frame rate is not good, e.g., 5s for a rotation, oh dear. 
<br>

![screenshot 2015-08-06 15 32 29](https://cloud.githubusercontent.com/assets/4334970/9142031/19579a34-3d0b-11e5-8560-1320bfd47525.jpg)
h3py in D3. Lag free with 1 million nodes, rendering maintained at a good fps. It's quite amazing: the csv for coordinates only is big. 10^5 is 11.2 MB, 10^6 is 107.7 MB.

## Performance
H3 performs in O(|V|) time, which is AWESOME. We have some benchmarks available for you in the examples to show it is, in fact, linear.  

| #nodes | time (seconds)    |
|--------|-------------------|
| 10e+1  | 0.000465893745422 |
| 10e+2  | 0.0039183139801   |
| 10e+3  | 0.0426687955856   |
| 10e+4  | 0.47996442318     |
| 10e+5  | 5.2688544035      |
| 10e+6  | 55.304875803      |

Testbed: MacBook Pro (mid 2014)
  - 2.2GHz Intel Core i7
  - 16 GB 1600 MHz DDR3

![log_cmp](https://cloud.githubusercontent.com/assets/4334970/17611401/e3d47084-6014-11e6-918d-535728ecea78.png)


If you have any questions about the package or if you find a bug please write Song at ee08b397@gmail.com or Adam at adam.kelleher@buzzfeed.com or Andrew at andrew.kelleher@buzzfeed.com. 
