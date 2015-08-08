#hypy - H3 in Python 

hypy is an pure python implementation of [H3](https://graphics.stanford.edu/papers/munzner_thesis/) from Dr. Tamara Munzner's Ph.D. dissertation in Stanford University, June 2000. It provides a scalable, high performance and interactive graph visualization in 3D hyperbolic space. We found this algorithm is good at tracking and presenting massive amounts of posts sharing across different social networks over time. There's also a Java3D implementation called [Walrus](https://www.caida.org/tools/visualization/walrus/) by Center for Applied Internet Data Analysis (CAIDA), last release in 2005.

## Quick View
```
h3/
├── __init__.py
├── examples
│   ├── __init__.py
│   ├── example1.py
│   ├── example2.py
│   ├── example3.py
│   ├── example4.py
│   └── example5.py
├── h3math.py
├── node.py
├── test
│   └── unit
│       └── test_tree.py
└── tree.py

3 directories, 11 files
```
`node`: implementation of node structure <br>
`tree`: implementation of tree structure <br>
`h3math`: implementation of all h3 algorithms <br>
`examples`: a bunch of examples running hypy, to mxake the life of developers easier <br>

* `example1`: a bare bone example of running hypy with all transparent internal operations, with input and output <br>
* `example2`: simplest example of calling hypy with a random graph and rendered in matlibplot <br>
* `example3`: a example for a specific tree as input: a full spanning tree with 40 nodes in 3 generations <br>
* `example4`: benchmark hypy performance and scalability, showing it running in O(V) <br>
* `example5`: export layout to csv for external renderer (e.g. d3.js) to process <br>

`test/unit/test_tree`: testing tree algorithms work correctly or not <br>

## Get Started
For testing purposes and before connecting to pound database, Barabasi is needed to generate some sample graph data<br>
`$ pip install python-igraph`

To get a first impression of the hypy with 500 nodes and multiplicity = 3. 
```
>>> import igraph
>>> from h3.tree import Tree, get_layout
>>> edges = igraph.Graph.Barabasi(n=500, m=3, directed=True).spanning_tree(None, True).get_edgelist()
>>> tree = get_layout(0, edges)
>>> tree.scatter_plot(equators=False, tagging=False)
```

## Results
![screenshot 2015-08-03 18 34 25](https://cloud.githubusercontent.com/assets/4334970/9049302/87de9d04-3a0e-11e5-91a5-06fb0baba28b.png)
hypy in matplotlib with 50,000 nodes, takes like 30s to get the plot. This is a proof-of-the-concept that is very easy to get from python only. Frame rate is not good, e.g., 5s for a rotation, oh dear. 
<br>

![screenshot 2015-08-06 15 32 29](https://cloud.githubusercontent.com/assets/4334970/9142031/19579a34-3d0b-11e5-8560-1320bfd47525.jpg)
hypy in D3. Lag free with 1 million nodes, rendering maintained at a good fps. It's quite amazing: the csv for coordinates only is big. 10^5 is 11.2 MB, 10^6 is 107.7 MB.

## Performance
To test the performance and scalability of hypy

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


## Disclaimer & License
This program is free software: you can redistribute it and/or modify it under the terms of the Apache License 2.0. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
