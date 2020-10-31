#!/usr/bin/env python3
from LMC import LMC

def main():
	#lmc = LMC('fib.lmc')
	#lmc.saveMailbox('fib.mailbox')

	# Load mailbox
	lmc = LMC('fib.mailbox', True)

	# lmc.run(True) to run verbosely
	return lmc.run()

######################

exit(main())