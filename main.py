from kivy.app import App
from kivy.config import Config

from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from kivy.uix.boxlayout import BoxLayout

# Components
from components.enums import NumBases
from components import CalcButton, CalcInput, NumButton, OpButton

class CalculatorApp(App):

	def __init__(self, **kwargs):
		super(CalculatorApp, self).__init__(**kwargs)

	def eval_input(self):
		print('eval_input')

	def add_input(self, string):
		pass

	def on_base_changed(self, old, new):
		pass


# TODO:
# ACTION BAR
# OTHER STUFF

SCREEN_WIDTH = 108
SCREEN_HEIGHT = 192
SCREEN_SCALE = 3

'''
# Less code, not as readable as
# doing Config.set(...) for each

settings = {
	"graphics": {
		"resizable": False,
		"width": SCREEN_WIDTH,
		"height": SCREEN_HEIGHT
	}
	"kivy": {
		"log_level": "warning"
	}
}

for section, options in settings.items():
	for option, value in options.items():
		Config.set(section, option, value)
'''
Config.set("graphics", "width", str(SCREEN_WIDTH*SCREEN_SCALE))
Config.set("graphics", "height", str(SCREEN_HEIGHT*SCREEN_SCALE))

Config.set('graphics', 'resizable', False)

Config.set('kivy', 'log_level', 'warning')

Config.write()

CalculatorApp().run()

