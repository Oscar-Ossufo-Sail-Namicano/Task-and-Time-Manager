#This package contain a customized button\
#To make beautifull apps"

# A rectangle button with round borders:
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.properties import ListProperty, StringProperty
from kivy.graphics import Color, Rectangle, Ellipse
from kivy.uix.image import Image

class CircRectangleButton(ButtonBehavior, Label):
	buttonColor = ListProperty([.1,.5,.7,1])
	buttonColor2 = ListProperty([.1,.1,.1,1])
	def __ini__(self, **kwargs):
		super().__init__(**kwargs)
		self.updateCanvas()
		
	def on_size(self, *args):
		self.updateCanvas()
		
	def on_pos(self, *args):
		self.updateCanvas()
		
	def on_press(self, *args):
		self.buttonColor, self.buttonColor2 = self.buttonColor2, self.buttonColor
		
	def on_release(self, *args):
		self.buttonColor, self.buttonColor2 = self.buttonColor2, self.buttonColor
		
	def on_buttonColor(self, *args):
		self.updateCanvas()
		
	def updateCanvas(self, *args):
		self.canvas.before.clear()
		with self.canvas.before:
			Color(rgba=self.buttonColor)
			Ellipse(pos=self.pos, size=(self.height, self.height))
			Ellipse(pos=(self.x+self.width-self.height, self.y), size=(self.height, self.height))
			Rectangle(pos=(self.x+self.height/2, self.y), size=(self.width-self.height, self.height))
			
#A circle plus Icon Button:
class RoundButton(ButtonBehavior, Label):
	buttonColor = ListProperty([1,1,1,1])
	buttonImage2 = StringProperty('images/Plus.png')
	buttonImage = StringProperty('images/blackThinPlus.png')
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.updateCanvas()
		
	def on_pos(self,*args):
		self.updateCanvas()
	
	def on_size(self, *args):
		self.updateCanvas()
		
#	def on_press(self, *args):
	#	self.buttonImage, self.buttonImage2= self.buttonImage2, self.buttonImage
	
	
#	def on_release(self, *args):
		#self.buttonImage, self.buttonImage2= self.buttonImage2, self.buttonImage
		
	def updateCanvas(self, *args):
		self.canvas.before.clear()
		with self.canvas.before:
			Color(rgba=self.buttonColor)
			Ellipse(source=self.buttonImage, pos=self.pos, size=(self.height, self.height))
			
class HidenMenuImage(Image):
	source=('images/hidenMenu.png')
	size_hint=(None, None)