import tkinter
import time
from func_for_window import *
from dial import Dial

running = True

class Window():
	def __init__(self, window):
		'''set some params'''
		window.geometry('500x600')
		window.title('STOPWATCH')
		window.protocol('WM_DELETE_WINDOW', close)
		window.resizable(False, False)
		'''functions '''
		background = create_background(window)
		text = title(window)
		front = Dial(window)		
		while running:
			window.update()
			time.sleep(0.01)
		window.destroy()

def close():
	global running
	running = False