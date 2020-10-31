# pyLMC

## Simple Little Man Computer interpretor in Python

Usage: See main.py

Load asm file:
* lmc = LMC(filename: str)

Load asm file and save mailbox:
* lmc = LMC(filename: str)
* lmc.saveMailbox()

Load mailbox:
* lmc = LMC('code.txt', True)

Run:
* lmc.run()

Run verbosely:
* lmc.run(True)

