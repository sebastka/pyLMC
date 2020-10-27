#!/usr/bin/env python3
from LMC import LMC

def main():
	lmc = LMC('lmc.txt', False) # True to save machinecode to code.txt
	
	# Halt should exit the program
	return lmc.run()

###################### TEMP:

######################

exit(main())