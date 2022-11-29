from setuptools import find_packages,setup

def get_requirments():
    pass 

setup(
    name="sensor", 
    version="0.0.1",
    author= "pritam bhakta",
    author_email="pritambhakta90@gmail.com",
    packages=find_packages(),
    install_required = get_requirments()
)