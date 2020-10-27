#!/usr/bin/env python3
from LMC import LMC

def main():
	# True to save machinecode to code.txt
	lmc = LMC('fib.lmc', False)
	
	# lmc.run(True) to run verbosely
	return lmc.run()

######################

exit(main())