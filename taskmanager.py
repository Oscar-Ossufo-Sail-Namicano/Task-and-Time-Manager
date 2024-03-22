from kivy import Config
Config.set('graphics', 'multisamples', '0')
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

import kivy
#kivy.require("2.2.1")
from kivy.app import App
from kivy.properties import ListProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SwapTransition
from kivy.graphics import Color, Rectangle, Ellipse
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.uix.actionbar import ActionButton
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.clock import Clock

from kivy.garden.navigationdrawer import NavigationDrawer as ND

from kivymd.theming import ThemeManager
import json
from customwidgets import CircRectangleButton, RoundButton, HidenMenuImage

class ScreensManager(ScreenManager):
	"""
	This is the main class that manages all screens of the app
	"""
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.transition = SwapTransition()

class TaskScreen(Screen):
	"""
	For each day of the week, has its own screen
	and this class defines all functionalites for each week screen
	"""
	taskList = {'sunday': [], 'monday': [], 'tuesday': [], 'wednesday': [], 'thursday': [], 'friday': [], 'saturday': []}
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	def on_pre_enter(self, *args):
		self.dataLoader()
		for key in self.taskList:
			if self.name == key:
				# it verifies if the key iguals to the current screen name (sunday, monday...).
				copy = self.taskList[key]
				for task in copy:
					self.ids.task_container.add_widget(Task(str(task)))
					self.ids.task_container.remove_widget(Task(str(2)))
					# o dois fornecido ao Task() acima, ee um simples argumento 
					# para nao dar erro de "zero argument given"

	def remove_task(self, received_task, *args):
		self.ids.task_container.remove_widget(received_task)

	def dataLoader(self):
		try:
			with open('.TTM-Tasks.json', 'r')  as data:
				self.taskList = json.load(data)
		except FileNotFoundError:
			pass

class TaskAdder(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	def dataSaver(self):
		with open('.TTM-Tasks.json', 'w') as data:
			json.dump(TaskScreen.taskList, data)

	def taskRegister(self):
		taskDay = self.ids.taskday.text
		taskDetail = self.ids.taskdetail.text
		if len(taskDay) > 0 and len(taskDetail) > 0:
			if taskDay in TaskScreen.taskList:
				TaskScreen.taskList[taskDay].append(taskDetail)
				self.dataSaver()
		pass

class Task(BoxLayout):
	def __init__(self, tarefa, **kwargs):
		super().__init__(**kwargs)
		self.ids.label.text = tarefa

	def callRemover(self, task):
		TaskScreen().remove_task(self)

class TaskManagerApp(App):
	pass

TaskManagerApp().run()