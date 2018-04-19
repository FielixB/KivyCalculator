from components.enums import NumBases
from kivy.uix.textinput import TextInput
import sys

class CalcInput(TextInput):

	def __init__(self, **kwargs):
		super(CalcInput, self).__init__(**kwargs)

		self.base = NumBases.DEC
		self.prev_base = NumBases.DEC

	def add_input(self, input):
		self.text += input

	#TODO: Evaluate input
	def eval(self):
		self.text = self.text.lstrip("0") # remove leading zeros
		self.text = str(eval(self.text))

'''
		print(f"converting from {self.prev_base} to {self.base}")

		if self.base == NumBases.DEC:
			if self.prev_base == NumBases.BIN:
				result = int(self.text, 2)
			elif self.prev_base == NumBases.HEX:
				result = int(self.text, 16)
			else:
				result = int(self.text)

		elif self.base == NumBases.BIN:
			if self.prev_base == NumBases.DEC:
				result = bin(int(self.text, 10))
			elif self.prev_base == NumBases.HEX:
				result = hex(int(self.text, 2))
			else:
				result = bin(int(self.text, 2))

		elif self.base == NumBases.HEX:
			if self.prev_base == NumBases.DEC:
				result = hex(int(self.text))
			elif self.prev_base == NumBases.BIN:
				result = hex(int(self.text, 2))
			else:
				result = int(self.text, 16)

		else:
			raise("Ya shit done broke, invalid NumBase")

		self.text = str(result)
'''
