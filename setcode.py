#setcode
def setcode(self):
	a = 3
	b = 4
	
	
	self.code = ""
	c = "a"
	i = 0
	while i <26:
		x = c 
		y = ord(x)*a+b
		m = y % 26
		self.code += chr(m + 97)
		c = chr(ord(c) + 1)
		i += 1