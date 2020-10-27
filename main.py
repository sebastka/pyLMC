#!/usr/bin/env python3
from LMC import LMC

def main():
	lmc = LMC('fib.lmc', False) # True to save machinecode to code.txt
	
	return lmc.run()

######################

exit(main())