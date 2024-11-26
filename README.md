# Frontiers-in-Applied-Drug-Design---Application-of-ORCA-for-Interaction-Energy-Calculation

In this repository, I report my project of applying the tool ORCA, using the coupled cluster method with singles, doubles, and perturbatively included triples excitations with the linear-scaling domain-based local pair natural orbital, DLPNO-CCSD(T).


### ORCA 6.0 installation 

The lastest version of ORCA for each operating system is available for downloading in the [official forum](https://orcaforum.kofo.mpg.de/). The information about setting ORCA to run in parallel on multiple cores is found [here](https://sites.google.com/site/orcainputlibrary/setting-up-orca) and the explanaition on how to run it with this option is found in the [manual](https://www.faccts.de/docs/orca/5.0/tutorials/first_steps/parallel.html).

This project was run in serial with a single computer of 16GB RAM.


### Input File
#### Format

The input file in ORCA consists of a free format file with a header in the first line, always starting with "!", followed by the main options indicating the methods that will be used for the calculation. Each method is defined by a keyword. A list of these keywords is presented in the [manual of version 4.2.1](https://www.afs.enea.it/software/orca/orca_manual_4_2_1.pdf) in section 6.2.1, but they should be double checked in case of modification in newer versions of the software.

As an example, the header of the input file used for the geometrical optimization in this project, which indicates the use of Hartree–Fock method with a correction for dispersion and a tight SCF convergence, is 
```bash
!HF-3c OPT TightSCF
```
It is important to note that ORCA is not case-sensitive, so an input with options like `!hf-3c opt tightscf` will be read the same as the one above.

There could be a block for more specific options if it is needed which always start with "%" and ends with "END". 

Following the geometrical optimization example, the option to specify that the optimization should be done on the hydrogens is 
```bash
% geom
    optimizehydrogens true
END
```

Finally, the section contains the coordinates of the structure. Here, the section starts and ends with "\*". 

In the first line the form of the coordinates is defined: if they are Cartesian the expression "xyz" will be used, while if they are Internal coordinates we should use "int". After the coordinates form comes the system's charge and multiplicity as two integers numbers separated by a space.

In this project, all the structures are given with coordinates in format .xyz, the charge was assumed to be 0 and the multiplicity 1, for which the first line of the section is as follows, and the lines after it contain the coordinates.
```bash
* xyz 0 1
...
*
```
It is also possible to use coordinates from an external file by adding the path to the file at the last position in the first line of this section.


### Output Files
