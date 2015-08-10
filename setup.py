try:
  from setuptools import setup, find_packages
except ImportError:
  import distribute_setup
  distribute_setup.use_setuptools()
  from setuptools import setup, find_packages

setup(
    name='pyh3',
    version='1.0',
    author='Songxiao Zhang, Adam Kelleher',
    author_email='ee08b397@gmail.com, adam.kelleher@buzzfeed.com',
    packages=['h3'],
    install_requires=[
        'python-igraph==0.7',
        'numpy==1.9.2',
        'matplotlib==1.4.3',
    ],
    url='http://www.github.com/buzzfeed/pyh3',
)
