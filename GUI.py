from tkinter import *
from tkinter.ttk import *


class EncryptGUI(Frame):
	#first valie
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.grid()
		self.createWidgets()
	
	#????????bulid view
	 def createWidgets(self):
		self.it = Label(self)
		self.it["text"] = "Input:"
		self.it.grid(row=0, column=0)
		self.ifd = Entry(self)
		self.ifd["width"] = 60
		self.ifd.grid(row=0, column=1,columnspan=6)
	
		self.ot = Label(self)
		self.ot["text"] = "Output:"
		self.ot.grid(row=1, column=0)
		self.ofd = Entry(self)
		self.ofd["width"] = 60
		self.ofd.grid(row=1, column=1,columnspan=6)
	
		self.nb = Button(self)
		self.nb["text"] = "New"
		self.nb.grid(row=2, column=0)
		self.nb["command"] = self.nm
		self.lb = Button(self)
		self.lb["text"] = "Load"
		self.lb.grid(row=2, column=1)
		self.lb["command"] = self.lm
		self.sb = Button(self)
		self.sb["text"] = "Save"
		self.sb.grid(row=2, column=2)
		self.sb["command"] = self.sm
		self.eb = Button(self)
		self.eb["text"] = "Encode"
		self.eb.grid(row=2, column=3)
		self.eb["command"] = self.em
		self.db = Button(self)
		self.db["text"] = "Decode"
		self.db.grid(row=2, column=4)
		self.db["command"] = self.dm
		self.cb = Button(self)
		self.cb["text"] = "Clear"
		self.cb.grid(row=2, column=5)
		self.cb["command"] = self.cm
		self.cb2 = Button(self)
		self.cb2["text"] = "Copy"
		self.cb2.grid(row=2, column=6)
		self.cb2["command"] = self.cm2
		
		self.dt = Label(self)
		m = "something happened"
		self.dt["text"] = m
		self.dt.grid(row=3, column=0
					columnspan=7)
	#  New Button
	def nm(self):
		self.dt["text"] = "New Button"
	
	#  Load Button
	def lm(self):
		self.dt["text"] = "Load Button"
	
	#   Save
	def sm(self):
		self.dt["text"] = "Save Button"
		
	#  Encode Button
	def em(self):
		self.dt["text"] = "Encode Button"
		
	#  Decode Button
	def dm(self):
		self.dt["text"] = "Decode Button"
		
	#  Clear Button
	def cm(self):
		self.dt["text"] = "Clear Button"
		
	#  Copy Button
	def cm2(self):
		self.dt["text"] = "Copy Button"
		
		
#GUI Start
if __name__ =='__main__'
	root = Tk()
	app = EncryptGUI(master=root)
	app.mainloop()