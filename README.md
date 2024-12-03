# Frontiers-in-Applied-Drug-Design---Application-of-ORCA-for-Interaction-Energy-Calculation

In this repository, I report the process of my project of applying the tool ORCA, using the coupled cluster method with singles, doubles, and perturbatively included triples excitations with the linear-scaling domain-based local pair natural orbital, DLPNO-CCSD(T).


### ORCA 6.0 installation 

The latest version of ORCA for each operating system is available for downloading in the [official forum](https://orcaforum.kofo.mpg.de/). The information about setting ORCA to run in parallel on multiple cores is found [here](https://sites.google.com/site/orcainputlibrary/setting-up-orca) and the explanaition on how to run it with this option is found in the [manual](https://www.faccts.de/docs/orca/5.0/tutorials/first_steps/parallel.html).

This project was run in serial with a single computer of 16GB RAM.


### Input File
#### Format

The input file in ORCA consists of a free format file with a header in the first line, always starting with "!", followed by the main options indicating the methods that are used for the calculation. Each method is defined by a keyword. A list of these keywords is presented in the [manual of version 4.2.1](https://www.afs.enea.it/software/orca/orca_manual_4_2_1.pdf) in section 6.2.1, but they should be double checked in case of modification in newer versions of the software. A newer version of the manual with all the methods available and their respective keywords are found [here](https://www.faccts.de/docs/orca/6.0/manual/contents/docu.html)

As an example, the header of the input file used for the geometrical optimization in this project, which indicates the use of the Hartree–Fock method with dispersion correction and a tight SCF convergence, is 
```bash
!HF-3c OPT TightSCF
```
It is important to note that ORCA is not case-sensitive, so an input with options like `!hf-3c opt tightscf` will be read the like the one above.

There could be a block for more specific options if it is needed which always starts with "%" and ends with "END". 

Following the geometrical optimization example, the option to specify that the optimization should be done on the hydrogens is 
```bash
% geom
    optimizehydrogens true
END
```

Finally, the section contains the coordinates of the structure. Here, the section starts and ends with "\*". 

In the first line the form of the coordinates is defined: if they are Cartesian the expression "xyz" is used, while if they are Internal coordinates we should use "int". After the coordinates form, we write the system's charge and multiplicity as two integers numbers separated by a space.

In this project, all the structures have their coordinates in format .xyz, the charge was assumed to be 0 and the multiplicity 1, for which the first line of the section is as follows, and the lines after it contain the coordinates.
```bash
* xyz 0 1
...
*
```
It is also possible to use coordinates from an external file by adding the path to the file at the last position in the first line of this section. In this case, the final * is not needed.

### Runnig ORCA
To run the program I used the command:
```bash
PATH/to/ORCA_6.0 input_file.inp > output_file.out
```
I ran this command three times for the geometry optimization, one with each file on the InputFiles/Optimization in this repository corresponding to the complex protein-ligand, the ligand alone and the protein alone. Then, I did the same for the LED analysis with the files in InputFiles/Calculation.
It is possible to add ORCA to the PATH in a single computer, but when running ORCA in parallel it always requires the full path.

If the output file is not given, the results of the calculations are printed in the terminal. Some of these can be very long depending on the size of the molecules, so it is always recommended to save it into an output file.

### Output Files
ORCA creates a directory with the output files. Here is a breif description of them.
* .out: This is the principal output file with the input details, progress updates, and final results.
* .inp: This file stores the exact file that was given as input for the calculation.
* .xyz: In geometry optimization, this file contains the corrected coordinates at the end of the optimization.
* _trj.xyz: This is the trajectory file, containing the geometry at each step of the calculation in XYZ format.
* .bibtex: This file has the citation information for the methods and basis sets used.
* .densities and .densitiesinfo: This file has information about the electron density. The first is in binary format and the second shows the metadata for easier interpretation.
* .engrad: Is the energy gradient file with the computed gradients (forces) on the nuclei at the current geometry.
* .gbw: This is the wavefunction file which contains the molecular orbitals and wavefunction data.
* .property.txt: This file contains a summary of molecular properties calculated during the run.
* .loc: In the DLPNO-CCSD(T) calculation, this file contains data about the Local Pair Natural Orbitals (LPNOs).
* .ges: The general energy storage file contains detailed energy information, useful for following calculations.
%to do

### Calculation of Energy Contributions in LED Analysis.
$\Delta E_{int} = \Delta E_{el-prep}^{ref} + \Delta E_{elsts}^{ref} + \Delta E_{exch}^{ref} + \Delta E_{non-dispersion}^{C-CCSD} + \Delta E_{dispersion}^{C-CCSD} + \Delta E_{int}^{C-(T)}$


%link to constrain optimization

