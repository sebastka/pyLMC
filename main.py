#!/usr/bin/env python3
from LMC import LMC

def main():
	lmc = LMC('fib.lmc')
	#lmc.saveMailbox()

	# Load mailbox
	#lmc = LMC('code.txt', True)

	# lmc.run(True) to run verbosely
	return lmc.run()

######################

exit(main())