# J. Melo-Ferreira 10/04/2018
##
# Adapted to least weasel winter morphs analysis: I. Miranda 05/2019
##
# Combines scaffold|site keys from different populations in a non-duplicated and ordered list
##
# Usage:
# python 1-combine-keys.py keys-SweNiv keys-SweVulg keys-PolNiv keys-PolVulg > combinekeys-output
##


import sys

# Read Swedish nivalis keys:

SN_key_file = open(sys.argv[1], 'r')
SN_key_list = SN_key_file.readlines()

SN_key_file.close()


# Read Swedish vulgaris keys:

SV_key_file = open(sys.argv[2], 'r')
SV_key_list = SV_key_file.readlines()

SV_key_file.close()


# Combine Swedish nivalis + Swedish vulgaris keys:

combined_list = SN_key_list + SV_key_list

SN_key_list = []
SV_key_list = []


combined_list = set(combined_list)
combined_list = list(combined_list)


# Add Polish nivalis keys:

PN_key_file = open(sys.argv[3], 'r')
PN_key_list = PN_key_file.readlines()

PN_key_file.close()

combined_list = combined_list + PN_key_list

PN_key_list = []

combined_list = set(combined_list)
combined_list = list(combined_list)


# Add Polish nivalis keys:

PV_key_file = open(sys.argv[4], 'r')
PV_key_list = PV_key_file.readlines()

PV_key_file.close()

combined_list = combined_list + PV_key_list

PV_key_list = []

combined_list = set(combined_list)
combined_list = list(combined_list)


# Order keys:

combined_list = sorted(combined_list, key = lambda x: (x.split('|')[0], int(x.split('|')[1])))


print ''.join(combined_list)


sys.exit()
