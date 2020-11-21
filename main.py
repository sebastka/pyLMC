#!/usr/bin/env python3
import argparse
from LMC import LMC

parser = argparse.ArgumentParser(
	"pyLMC",
	description='Little Man Computer interpretor in Python.'
)

parser.add_argument(
	'--verbose', '-v',
	help = 'run verbosely',
	dest = 'verbose',
	action='store_true'
)

parser.add_argument(
	'-r',
	help = 'load and run lmc file',
	dest = 'lmc_in',
	action='store'
)

parser.add_argument(
	'-s',
	help = 'store mailbox to file',
	dest = 'mb_out',
	action='store'
)

parser.add_argument(
	'-l',
	help = 'load and run mailbox file',
	dest = 'mb_in',
	action='store'
)



def main(args):
	if args.lmc_in: # Loads asm file
		lmc = LMC(args.lmc_in)
		
		if args.mb_out:
			lmc.saveMailbox(args.mb_out)
		
		return lmc.run(args.verbose)
	elif args.mb_in: # Load mailbox
		lmc = LMC(args.mb_in, True)
		return lmc.run(args.verbose)
	else:
		print('Usage: pyLMC -h')
		return 1

######################

exit(main(parser.parse_args()))