class Color:
	def __new__(cls):
		if not hasattr(cls, 'instance'):
			cls.instance = super(Color, cls).__new__(cls)
		return cls.instance
	
	def __init__(self):
		self.BLACK		= (0, 0, 0)
		self.WHITE		= (255, 255, 255)
		self.RED		= (255, 0, 0)
		self.GREEN		= (0, 255, 0)
		self.BLUE		= (0, 0, 255)
		self.YELLOW 	= (255, 255, 0)
		self.MAGENTA	= (255, 0, 255)
		self.CYAN 		= (0, 255, 255)

		self.DARKER_PURPLE = (13, 6, 20)
