#!/usr/bin/env python3
from LMC import LMC

def main():
	lmc = LMC('fib.asm')
	#lmc.saveMailbox('fib.lmc')

	# Load mailbox
	#lmc = LMC('fib.lmc', True)

	# lmc.run(True) to run verbosely
	return lmc.run()

######################

exit(main())