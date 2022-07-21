import tkinter
class Dial():
	def __init__(self, window):
		front = tkinter.Canvas(window, height = 400, width = 350)
		front.place(x=70, y=30)
		dial = tkinter.PhotoImage(file='dial.png')
		dial = dial.subsample(7, 7)
		cheesImg = front.create_image(0,-20, anchor=NW, image = dial)