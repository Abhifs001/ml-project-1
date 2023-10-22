from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:


    require =[]

    with open(file_path) as file_obj:
        require= file_obj.readlines()
        require = [req.replace("\n", " ") for req in require]

        if '-e .' in require:
            require.remove('-e .')
    return require



setup(
    name='ML-Project',
    version='0.0.1',
    author='Abhinav Pandey',
    author_email='info.codexcrank@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')
)