# my_package/pdb_operations.py

from openmm.app import *
from openmm import *
from openmm.unit import *
from sys import stdout
import openmm as mm 
import MDAnalysis as mda


def periodify_pdb(file_path):
    pdb = PDBFile(file_path) 
    forcefield = ForceField('amber14-all.xml', 'amber14/tip3pfb.xml')
    system = forcefield.createSystem(pdb.topology, nonbondedMethod=NoCutoff, nonbondedCutoff=1*nanometer, constraints=HBonds)
    """Load and analyze the PDB file."""
    u = mda.Universe(file_path)

    # Perform operations on the PDB data
    # For example:
    box_dimensions = u.dimensions
    # Extract the dimensions (box vectors) from the box_dimensions
    box_vector_1, box_vector_2, box_vector_3 = box_dimensions[:3]
    box_size = [box_vector_1, box_vector_2, box_vector_3]  # Dimensions of the periodic box
    # Convert the box_size to Quantity with angstroms unit
    box_size_quantity = [size * angstroms for size in box_size]

    # Create Vec3 objects for the box vectors
    box_vectors = (
        openmm.Vec3(box_size_quantity[0]._value, 0, 0),
        openmm.Vec3(0, box_size_quantity[1]._value, 0),
        openmm.Vec3(0, 0, box_size_quantity[2]._value)
        )

    pdb.topology.setPeriodicBoxVectors(box_vectors)

    # Save the modified PDB file with the periodic box information
    app.PDBFile.writeFile(pdb.topology, pdb.positions, open('newperiodic.pdb', 'w'))

    # Set the periodic box vectors using the box_vectors

    return system.setDefaultPeriodicBoxVectors(*box_vectors)


