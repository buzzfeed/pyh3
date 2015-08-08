try:
  from setuptools import setup, find_packages
except ImportError:
  import distribute_setup
  distribute_setup.use_setuptools()
  from setuptools import setup, find_packages

setup(
    name='h3',
    version='1.1',
    packages=['h3'],
    install_requires=[
        'python-igraph==0.7',
        'numpy==1.9.2',
        'matplotlib==1.4.3',
    ],
    url='http://www.github.com/buzzfeed/h3',
)
