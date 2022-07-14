from setuptools import setup, find_packages
from typing import List

#Declaring varible  for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.1" #Change Version if any new library is installed
AUTHOR="Anurag P Ekka"
DESCRIPTION="My first ML project with CICD"
PACKAGES=["housing"]
REQUIREMENTS_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description: This function is goib=ng to return list od requiremnts 
    mentioned in requirement.txt file

    return this function is going eo reutun a list which contain name
    of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")

setup(
    name=PROJECT_NAME,
    version=VERSION,
    authors=AUTHOR,
    description=DESCRIPTION,
    #packages=PACKAGES,
    #find_packages() returns all the folders having __init__.py(developer defined packages)
    packages=find_packages(),
    install_requires=get_requirements_list()
)

#if __name__=="__main__":
#    print(get_requirements_list())
