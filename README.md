# Frontiers-in-Applied-Drug-Design---Application-of-ORCA-for-Interaction-Energy-Calculation

In this repository, I report the process of my project of applying the tool ORCA, using the coupled cluster method with singles, doubles, and perturbatively included triples excitations with the linear-scaling domain-based local pair natural orbital, DLPNO-CCSD(T).


### ORCA 6.0 installation 

The latest version of ORCA for each operating system is available for download in the [official forum](https://orcaforum.kofo.mpg.de/). The information about setting ORCA to run in parallel on multiple cores is found [here](https://sites.google.com/site/orcainputlibrary/setting-up-orca) and the explanation on how to run it with this option is found in the [manual](https://www.faccts.de/docs/orca/5.0/tutorials/first_steps/parallel.html).

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

Since the major problem in this project that led to a very small interaction energy was the preparation energy, which is influenced by the geometry of the system, I looked at some useful considerations for the optimization. In this section of the [manual](https://orca-manual.mpi-muelheim.mpg.de/contents/detailed/geomopt.html) there are keywords detailed for running the optimization in a more refined and specific way. Additionally, I suggested that part of the problem was that my optimization only took the hydrogen atoms into account, leaving the rest of the atoms fixed. However, in the paper some specific atoms were constrained and the optimization was done in the rest to simulate a more realistic scenario. A guide to do this is presented [here](https://www.faccts.de/docs/orca/6.0/manual/contents/typical/optimizations.html).

### Output Files
ORCA creates a directory with the output files. Here is a brief description of them.
* .out: This is the principal output file with the input details, progress updates, and final results.
* .inp: This file stores the exact file given as input for the calculation.
* .xyz: In geometry optimization, this file contains the corrected coordinates at the end of the optimization.
* _trj.xyz: This is the trajectory file, containing the geometry at each step of the calculation in XYZ format.
* .bibtex: This file has the citation information for the methods and basis sets used.
* .densities and .densitiesinfo: This file has information about the electron density. The first is in binary format and the second shows the metadata for easier interpretation.
* .engrad: This is the energy gradient file with the computed gradients (forces) on the nuclei at the current geometry.
* .gbw: This is the wavefunction file which contains the molecular orbitals and wavefunction data.
* .property.txt: This file contains a summary of molecular properties calculated during the run.
* .loc: In the DLPNO-CCSD(T) calculation, this file contains data about the Local Pair Natural Orbitals (LPNOs).
* .ges: The general energy storage file contains detailed energy information that is useful for the following calculations.
  

### Calculation of Energy Contributions in LED Analysis.
The calculation of the total energy interactions between the residue and the ligand was calculated with the following equation, taken from the [LED section](https://www.faccts.de/docs/orca/6.0/tutorials/prop/led.html) in ORCA's manual.


```math
\Delta E_{int} = \Delta E_{el-prep}^{ref} + \Delta E_{elsts}^{ref} + \Delta E_{exch}^{ref} + \Delta E_{non-dispersion}^{C-CCSD} + \Delta E_{dispersion}^{C-CCSD} + \Delta E_{int}^{C-(T)}
```
The electrostatic and the exchange energy are given directly in the output file from the LED analysis of the complex:

```math
\Delta E_{elsts}^{ref} = -0.026346689 Eh
```

```math
\Delta E_{exch}^{ref} = -0.007950562 Eh
```
The dispersion energy is the sum of the two dispersion values in this output file:


$$\eqalign{ 
\Delta E_{dispersion}^{C-CCSD} &= Dispersion (strong pairs) + Dispersion (weak pairs) \\
&= -0.001942662 + \left(-0.006034170\right) \\ 
&= -0.007976832 Eh
}$$


For the preparation energy calculation, we need the information of the Intra fragment in the complex output file and the E0 value for each of the fragments that is contained in the output of each them alone.

$$\eqalign{
\Delta E_{el-prep}^{ref} &= (Intra fragment 1 (REF.) - E(0)\_{frag1}) + (Intra fragment 2 (REF.) - E(0)_{frag2}) \\ 
&= (-1069.405210714 - (-1069.428347806)) +  (-359.220798454 - (-359.233055993)) \\ 
&= 0.03539463099986051 Eh
}$$

The non-dispersion correlation energy calculation is as follows:

$$\eqalign{
\Delta E_{non-dispersion}^{C-CCSD} &= (Non dispersion (strong pairs) + Non dispersion (weak pairs)) - (E(CORR)(corrected)\_{frag1} + E(CORR)(corrected)_{frag2}) \\ 
&= (-3.041870050+(-0.015073379))-(-1.880537976 + (-1.175169112)) \\ 
&= -0.0012363409999998076 Eh
}$$

Finally, the triple excitation correlation energy is calculated as follows:

$$\eqalign{
\Delta E_{int}^{C-(T)} &= (Triples Correction (T)\_{complex} - (Triples Correction (T)\_{frag1} + Triples Correction (T)_{frag2}) \\ 
&= -0.118432443 -(-0.066449215 + (-0.051620108)) \\ 
&= -0.00036311999999999456 Eh
}$$

The sum of all these contributions gives the total interaction energy of the system:
```math
\Delta E_{int} = -0.00847891300013929 Eh = -22.26138608186571 kJ/mol
```



