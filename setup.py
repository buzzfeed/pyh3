try:
  from setuptools import setup, find_packages
except ImportError:
  import distribute_setup
  distribute_setup.use_setuptools()
  from setuptools import setup, find_packages

setup(
    name='pyh3',
    version='1.1',
    author='Songxiao Zhang, Adam Kelleher',
    author_email='ee08b397@gmail.com, adam.kelleher@buzzfeed.com',
    description='Pure Python implementation of h3 for visualizing LARGE graphs',
    long_description='Implements O(|V|) graph layout in hyperbolic space for visualizing very large ( > 1M nodes ) graphs.',
    keywords='walrus h3 graph visualization graphviz dot graphml network rendering render layout hyperbolic',
    packages=['h3'],
    install_requires=[
        'python-igraph==0.7',
        'numpy==1.21.0',
        'matplotlib==1.4.3',
    ],
    url='http://www.github.com/buzzfeed/pyh3',
)
