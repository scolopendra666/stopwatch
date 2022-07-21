import tkinter


def create_background(window):
	background = tkinter.Canvas(window)
	background.place(x=0, y=0, width=500, height=600)

def title(window):
	txt = tkinter.Label(window, text='Секундомер', font=('Arial Bold', 50))
	txt.pack()

