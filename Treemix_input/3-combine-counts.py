# J. Melo-Ferreira 10/04/2018
##
# Adapted to least weasel winter morphs analysis: I. Miranda 05/2019
##
# Combines complete file from each population into a single table.
# Sites with missing data are removed.
# Invariable sites are removed.
# Sites with same minor allele count < N (suggestion 4) in all populations and = 0 in the outgroup (Ferret) are removed
##
# Usage:
# python 3-combine-counts.py complete-SweNiv complete-SweVulg complete-PolNiv complete-PolVulg complete-Ferret N-minor-count > combine-output
##


import sys
import itertools
from itertools import izip

print 'SCAF\tSITE\tSwe-niv\tSwe-vulg\tPol-niv\tPol-vulg\tFerret'

SN_file = open(sys.argv[1], 'r')
SV_file = open(sys.argv[2], 'r')
PN_file = open(sys.argv[3], 'r')
PV_file = open(sys.argv[4], 'r')
FERRET_file = open(sys.argv[5], 'r')

for line_SN, line_SV, line_PN, line_PV, line_FERRET in izip(SN_file, SV_file, PN_file, PV_file, FERRET_file):
	site_SN = line_SN.split('\t')[0]
	chromosome = site_SN.split('|')[0]
	coordinate = site_SN.split('|')[1]
	var_SN = line_SN.split('\t')[1].rstrip('\n')	
	site_SV = line_SV.split('\t')[0]
	var_SV = line_SV.split('\t')[1].rstrip('\n')
	site_PN = line_PN.split('\t')[0]
	var_PN = line_PN.split('\t')[1].rstrip('\n')
        site_PV = line_PV.split('\t')[0]
	var_PV = line_PV.split('\t')[1].rstrip('\n')
	site_FERRET = line_FERRET.split('\t')[0]
	var_FERRET = line_FERRET.split('\t')[1].rstrip('\n')
	variants = [var_SN, var_SV, var_PN, var_PV, var_FERRET]
	if 'x' not in variants:
		der_SN = var_SN.split(',')[0]
		anc_SN = var_SN.split(',')[1]
		der_SV = var_SV.split(',')[0]
		anc_SV = var_SV.split(',')[1]
		der_PN = var_PN.split(',')[0]
		anc_PN = var_PN.split(',')[1]
                der_PV = var_PV.split(',')[0]
		anc_PV = var_PV.split(',')[1]
		der_FERRET = var_FERRET.split(',')[0]
		anc_FERRET = var_FERRET.split(',')[1]
		varlist_SN = [int(der_SN), int(anc_SN)]
		varlist_SV = [int(der_SV), int(anc_SV)]
		varlist_PN = [int(der_PN), int(anc_PN)]
                varlist_PV = [int(der_PN), int(anc_PV)]
		varlist_FERRET = [int(der_FERRET), int(anc_FERRET)]
		if site_SN == site_SV == site_PN == site_PV == site_FERRET:
			if der_SN == der_SV == der_PN == der_PV == der_FERRET == '0':
				pass
			else:
				if  anc_SN == anc_SV == anc_PN == anc_PV == anc_FERRET == '0':	
				        pass
				else:
                                        if min(int(der_SN), int(anc_SN))>=int(sys.argv[6]):
                                                print chromosome+'\t'+coordinate+'\t'+var_SN+'\t'+var_SV+'\t'+var_PN+'\t'+var_PV+'\t'+var_FERRET
                                        elif min(int(der_SV), int(anc_SV))>=int(sys.argv[6]):
                                                print chromosome+'\t'+coordinate+'\t'+var_SN+'\t'+var_SV+'\t'+var_PN+'\t'+var_PV+'\t'+var_FERRET
                                        elif min(int(der_PN), int(anc_PN))>=int(sys.argv[6]):
                                                print chromosome+'\t'+coordinate+'\t'+var_SN+'\t'+var_SV+'\t'+var_PN+'\t'+var_PV+'\t'+var_FERRET
                                        elif min(int(der_PV), int(anc_PV))>=int(sys.argv[6]):
                                                print chromosome+'\t'+coordinate+'\t'+var_SN+'\t'+var_SV+'\t'+var_PN+'\t'+var_PV+'\t'+var_FERRET
                                        else:
                                                if varlist_SN.index(min(varlist_SN)) == varlist_SV.index(min(varlist_SV)) == varlist_PN.index(min(varlist_PN)) == varlist_PV.index(min(varlist_PV)) == varlist_FERRET.index(min(varlist_FERRET)):
                                                        pass
                                                else:
                                                        print chromosome+'\t'+coordinate+'\t'+var_SN+'\t'+var_SV+'\t'+var_PN+'\t'+var_PV+'\t'+var_FERRET
		else:
			print 'ERROR - SITE DOES NOT CORRESPOND'


sys.exit()
