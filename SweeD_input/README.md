# SweeD input from ANGSD .mafs output

This folder contains the R script used to generate an input file for [SweeD](https://cme.h-its.org/exelixis/web/software/sweed/) from an allele frequencies file (.mafs) generated with [ANGSD](http://www.popgen.dk/angsd/index.php/ANGSD). 
* It's assumed that the .mafs files were produced using the ancestral state (ancestral reference provided with -anc) as major allele (-doMajorMinor 5).
* The SweeD input is generated in the SweepFinder format.
