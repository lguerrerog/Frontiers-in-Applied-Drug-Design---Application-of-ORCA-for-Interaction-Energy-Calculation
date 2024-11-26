#### This script adds the indicator defining the fragment to which each atom belogns
import pandas as pd

# path to .xyz with the coordinates of the complex residue - ligand
arch_xyz = "/PATHto/4aglSmallComplex_TightOptimization.xyz"
# read .xyz
with open(arch_xyz, 'r') as arch:
    lines = arch.readlines()
    
# First line with number of atoms
n_atom = int(lines[0].strip())
# Second line with comments
comment = lines[1].strip()
# atoms data
data = []

# The lines containing the coordinates
for line in lines[2:]:
    element, x, y, z = line.split()
    data.append([element, float(x), float(y), float(z)])
# Archive as dataframe 
df = pd.DataFrame(data, columns=["Element", "x", "y", "z"])
# Indexes of atoms belonging to ligand will have suffix '(2)' and elements belonging to the residue will have suffix '(1)'
indexes_ligand = [95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 
                 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243]

# adding suffix to atoms
def add_suffix(row):
    if row.name in indexes_ligand:  
        return row["Element"] + "(2)"
    else:
        return row["Element"] + "(1)"

# Apply function to first column
df["Element"] = df.apply(add_suffix, axis=1)
df.to_csv("PATH/to/output/4aglSmallComplex_calculation_Fragmented.txt", sep=' ', index=False, header=False)
