from setuptools import setup, find_packages

setup(
    name="periodify_pdb",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "openmm",
    ],
)

pip install .
