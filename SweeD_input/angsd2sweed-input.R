# PREPARE SWEED INPUT
# FROM ANGSD MAFS FILE OUTPUT
#
# I. Miranda (03/2019)
#
# This script assumes that the ANGSD .mafs output was produced using the ancestral state (ancestral reference provided with -anc) as major allele (-doMaf 5).
#

#Import required library:
library(tidyverse)

#Set working directory:
setwd ("/path/to/mafs-file-directory")

#Read .mafs file:
angsd_mafs <- read.table("angsd-output.mafs", header = T, row.names = NULL)

#Calculate SweeD input columns:
input_prep <- mutate(angsd_mafs, x = round(knownEM*nInd*2, digits = 0),   #x column = number of derived alleles sampled
            n = nInd*2,  #n column = total number of alleles in the population
            folded = 0)  #folded = 0; known ancestral state

#Create dataframe with columns of interests:
sweeD_input <- data.frame(input_prep$position, input_prep$x, input_prep$n, input_prep$folded)

#Add column names to SweeD input:
names(sweeD_input) <- c("position", "x", "n", "folded")

#Output SweeD input file:
write.table(sweeD_input, "SeeD_input_file.txt", col.names=T, row.names = F, quote = F, sep = "\t")

