#periodify_pdb

periodify_pdb is a single-function Python Package that takes in PDB files and places them in an appropriate Periodic Box environment according to the dimensions of the file. It relies on OpenMM being installed beforehand. This package is currently in its original version, version 0.1. It is important to note that the package will not work for PDB files with duplicate atoms and that the PDB files must have readable dimensions relative to the x, y, and z axes. 

##Installation


Use the package manager [pip](https://pip.pypa.io/en/stable/) to install periodify_pdb
```bash
pip install periodify_pdb
```


## Usage

```python
import periodify_pdb

#returns a new pdb labeled "newperiodic.pdb" in a periodic box environment appropriate to the file inputted. 
periodify_pdb('file_path')

##Development 

periodify_pdb was developed by Brandon Mendoza while an intern for The Illinois Institute of Technology, under the Minh Research Group. 


##License 
