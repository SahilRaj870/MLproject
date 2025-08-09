from setuptools import find_packages,setup

from typing import List

hypen_e_dot='-e .'

def get_requirements(file_path:str)->List[str]:

    requirement=[]
    with open(file_path) as file_obj:
        requirement=file_obj.readlines()
        reqirement=[req.replace("\n","") for req in requirement]
        if hypen_e_dot in requirement:
            requirement.remove(hypen_e_dot)
        
    return requirement


setup(
    name='MLproject',
    version='0.0.1',
    author='Sahil',
    author_email='raj363344@gmail.com',
    packages=find_packages(),
    install_require=get_requirements('requirement.txt')
)