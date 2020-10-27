class LMC:
	def __init__(self, filename, save = False):
		""" Initialize LMC machine

			Args:
				filename (str): file to parse
				save (bool): to save machine code or not
		"""

		self._mailbox = [0 for x in range(100)]
		self._program = []
		self._labels = {}

		self.instructionSet = {
			'HLT': 000, 
			'ADD': 100, 
			'SUB': 200, 
			'STA': 300, 'STO': 300,
			'LDA': 500, 
			'BRA': 600, 
			'BRZ': 700, 
			'BRP': 800, 
			'INP': 901, 
			'OUT': 902, 
			'OTC': 922, # Non standard
			'DAT': None
		}

		self.parseFile(filename)
		self.toMailbox(save)

	def openFile(self, filename, mode = 'r'):
		""" Open and test if a file can be opened

			Args:
				filename (str): file to open
				mode (str): mode to open with. Default i 'r'
			
			Returns:
				file handle upon success
				exits upon failure
		"""

		try:
			return open(filename, mode)
		except IOError:
			print('Error: could not open file: ' + filename)
			exit(1)

	def parseFile(self, filename):
		""" Parse opened file line by line and add each relevant line to _program

			Args:
				filename (str): file to parse
		"""

		f = self.openFile(filename)

		i = 0
		for line in f.readlines():
			line = self.parseLine(self.trimLine(line)) # Parse line

			if line != None:
				if line[0] != None:
					self._labels.update({line[0]: i}) # If line has a label, add to label list
				
				self._program.append(line) # Save line to _program
				i += 1
		
		f.close()
	
	def trimLine(self, line):
		""" Remove comments, tabs and spaces and nl from line

			Args:
				line (str)
			
			Returns:
				str: a stripped line or None if line does not contain code
		"""

		# Remove comments:
		line = line.split('//')
		line = line[0].split('#')

		#Remove whit spaces and tanbs
		line = line[0].strip('\t\n\r').replace('\t', ' ').split(' ')
		line = list(filter(None, line))
		
		# If we have something, return line
		if line:
			return line
		else:
			return None
	
	def parseLine(self, line):
		""" Parse line

			Args:
				line: str
			
			Returns:
				list: [label, instruction, address]
		"""

		if line == None:
			return None
		
		cols = len(line)
		label = None
		instruction = None
		address = None

		if cols == 1: # If the line has one column, it's only an instruction
			instruction = line[0].upper()
		elif cols == 2: # If two, it's either a label with instruction, or instruction with address
			if line[0].upper() in self.instructionSet:
				instruction = line[0].upper()
				address = line[1].upper()
			elif line[1].upper() in self.instructionSet:
				label = line[0].upper()
				instruction = line[1].upper()
		elif cols == 3: # If three, all of them
			label = line[0].upper()
			instruction = line[1].upper()
			address = line[2].upper()

		# If instruction is invalid, bail out
		if instruction not in self.instructionSet:
			print('Unknown instruction \'' + str(instruction) + '\'!')
			exit(0)
		
		return [label, instruction, address]

	def toMailbox(self, save):
		""" Save _program to mailbox with machine code

			Args:
				save (bool): save machine code in file or not
		"""

		i = 0
		for line in self._program: # Loop through program (parsed file)
			if line[1] == 'DAT':
				if line[2]: # DAT is not always initialized to 0
					self._mailbox[i] = int(line[2])
				else:
					self._mailbox[i] = 0
			else:
				self._mailbox[i] = int(self.instructionSet[line[1]]) # mailbox = Instruction code

				if line[2] in self._labels: # mailbox += address as label (if indicated)
					self._mailbox[i] += int(self._labels[line[2]])
				elif line[1] == 'LDA' and line[2].isnumeric(): # Load an address explicitly
					self._mailbox[i] += int(line[2])
			
			i += 1
		
		if save: # Save mailbox to code.txt
			self.writeMailbox()

	def writeMailbox(self):
		""" 
			Save mailbox to code.txt
		"""

		f = self.openFile('code.txt', 'w')

		for i in self._mailbox:
			f.write(str(i) + '\n')

		f.close()

	def run(self, verbose = False):
		""" Run mailbox

			Args:
				verbose (bool): run verbosely (for debugging)
		"""
		acumulator = 0
		counter = 0

		while True:
			machinecode = self._mailbox[counter]
			
			if verbose:
				print('\n----------------------------')
				print('Counter: ' + str(counter))
				print('Acumulator: ' + str(acumulator))
				print('Machinecode: ' + str(machinecode))
				print('----------------------------')

			if machinecode == 0: # HLT
				return 0
			elif machinecode in range(100, 199): # ADD
				acumulator += self._mailbox[machinecode-100]
			elif machinecode in range(200, 299): # SUB
				acumulator -= self._mailbox[machinecode-200]
			elif machinecode in range(300, 399): # STA
				self._mailbox[machinecode-300] = acumulator
			elif machinecode in range(400, 499): # Undefined
				pass
			elif machinecode in range(500, 599): # LDA
				acumulator = self._mailbox[machinecode-500]
			elif machinecode in range(600, 699): # BRA
				counter = machinecode - 600
				continue
			elif machinecode in range(700, 799): # BRZ
				if acumulator == 0:
					counter = machinecode - 700
					continue
			elif machinecode in range(800, 899): # BRP
				if acumulator >= 0:
					counter = machinecode - 800
					continue
			elif machinecode == 901: # INP
				acumulator = int(input('Input: '))
			elif machinecode == 902: # OUT
				print(acumulator)
			elif machinecode == 922: # OTC
				print(chr(acumulator), end='')
			else: # DAT
				pass

			counter += 1
		
		print('Unexpected behaviour. Does your program halt?')
		exit(1)