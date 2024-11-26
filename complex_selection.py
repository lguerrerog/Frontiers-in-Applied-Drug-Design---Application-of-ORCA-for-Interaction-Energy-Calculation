import os
from pymol import cmd
import numpy as np

#show working directory
os.getcwd()
#resets paramiters and cleans session
cmd.reinitialize()
#download and load the structure from PDB
cmd.fetch('4agl', type = 'pdb')
#Remove all models except the first one
cmd.remove("not state 1")
# Keep only atoms with alternative location indicator 'A' or those without an alternative location
cmd.remove("alt B")
#hides all
cmd.hide('everything', "all")
#Creates selection containing the organic molecules and some elements
cmd.select('haloligands', 'bymol organic and (e. Cl or e. Br or e. I) and chain A')
#Selects active site
cmd.select('binding_pockets', 'byres haloligands around 5')
#Show selections
cmd.show('sticks', 'haloligands')
cmd.show('sticks', 'binding_pockets')
#select complex
cmd.select('complex', 'haloligands or binding_pockets')
# Add hydrogens to the 'complex' selection
cmd.h_add('complex')
# Create a new selection that includes the hydrogen atoms from the 'complex' selection
cmd.select('complex_h', 'complex or elem H')

