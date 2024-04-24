'''
Role of setup.py file : Setup.py file contains the metadata about python packages 
, Dependencies of the project and distribution of packages. '''

from setuptools import setup , find_packages

def get_requirements(file_path):
    ## Doc String
    '''This function returns the List of Requirements in the requirements.txt file'''

    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        
        ## readlines() will also read \n , our task is to remove /n from requirements list

        requirements = [req.replace('\n' , "") for req in requirements]

    return requirements

setup(
    name = 'MCQ Generator',
    version= '0.0.1',
    author= 'Harsh Shukla',
    author_email= 'hs081449@gmail.com',
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')
)