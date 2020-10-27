import re

#def printList(m_list):
#	i = 0
#	for el in m_list:
#		print('#' + str(i) + ':\t' + str(el))
#		i += 1

class LMC:
	def __init__(self, filename, save = False):
		self._mailbox = [0 for x in range(100)]
		self._program = []
		self._labels = {}

		self.instructionSet = {
			'HLT': 000, 
			'ADD': 100, 
			'SUB': 200, 
			'STA': 300, 
			'LDA': 500, 
			'BRA': 600, 
			'BRZ': 700, 
			'BRP': 800, 
			'INP': 901, 
			'OUT': 902, 
			'OTC': 922, # Non standard
			'DAT': None
		}

		self.ParseFile(filename)
		self.toMailbox(save)

	def openFile(self, filename, mode = 'r'):
		try:
			return open(filename, mode)
		except IOError:
			print('Error: could not open file: ' + filename)
			exit(1)

	def ParseFile(self, filename):
		f = self.openFile(filename)

		i = 0
		for line in f.readlines():
			line = self.parseLine(self.trimLine(line))
			if line != None:
				if line[0] != None:
					self._labels.update({line[0]: i})
				
				self._program.append(line)
				i += 1
		
		f.close()
	
	def trimLine(self, line):
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
		if line == None:
			return None
		
		cols = len(line)
		label_from = None
		instruction = None
		label_to = None

		if cols == 1:
			instruction = line[0].upper()
		elif cols == 2:
			if line[0].upper() in self.instructionSet:
				instruction = line[0].upper()
				label_to = line[1].upper()
			elif line[1].upper() in self.instructionSet:
				label_from = line[0].upper()
				instruction = line[1].upper()
		elif cols == 3:
			label_from = line[0].upper()
			instruction = line[1].upper()
			label_to = line[2].upper()

		if instruction not in self.instructionSet:
			print('Unknown instruction \'' + instruction + '\'!')
			exit(0)
		
		return [label_from, instruction, label_to]

	def toMailbox(self, save):
		i = 0
		for line in self._program:
			if line[1] == 'DAT':
				self._mailbox[i] = int(line[2])
			else:
				self._mailbox[i] = int(self.instructionSet[line[1]])

				if line[2] in self._labels:
					self._mailbox[i] += int(self._labels[line[2]])
				elif line[1] == 'LDA' and line[2].isnumeric():
					self._mailbox[i] += int(line[2])
			
			i += 1
		
		if save:
			self.writeMailbox()

	def writeMailbox(self):
		f = self.openFile('code.txt', 'w')

		for i in self._mailbox:
			f.write(str(i) + '\n')

		f.close()

	def run(self):
		acumulator = 0
		counter = 0

		while True:
			machinecode = self._mailbox[counter]

			#print('\n----------------------------')
			#print('Counter: ' + str(counter))
			#print('Acumulator: ' + str(acumulator))
			#print('Machinecode: ' + str(machinecode))
			#print('----------------------------')

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