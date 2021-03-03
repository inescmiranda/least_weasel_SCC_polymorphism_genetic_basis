# J. Melo-Ferreira 10/04/2018
##
# Adapted to least weasel winter morphs analysis: I. Miranda 05/2019
##
# Opens angsd -doMaf output file (.mafs) and outputs scaffold|site key
##
# Usage:
# python 0-keys.py angsd-mafs-file > keys-output 
# Run per population


import sys

keys = []


with open(sys.argv[1], 'r') as f:
	header = f.readline()
	for line in f:
		if line is not '':
			columns = line.split('\t')
			key = '|'.join([columns[0], columns[1]])
			print key
		else:
			pass

f.close()

sys.exit()
