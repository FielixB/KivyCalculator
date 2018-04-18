from kivy.properties import ObjectProperty
from kivy.uix.textinput import TextInput

class CalcInput(TextInput):

	def __init__(self, **kwargs):
		super(CalcInput, self).__init__(**kwargs)

	def add_input(self, input):
		self.text += input

	#TODO: Evaluate input
	def eval(self):
		pass