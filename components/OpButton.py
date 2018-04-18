from components import CalcButton, CalcInput
from kivy.clock import Clock

class OpButton(CalcButton.CalcButton):

	def __init__(self, **kwargs):
		super(OpButton, self).__init__(**kwargs)

	def add_input(self, input):
		print(CalcInput.CalcInput.ids['num_input'])