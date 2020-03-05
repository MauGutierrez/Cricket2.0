class SemanticRules:
	def __init__(self):
		self.cube = dict()

		#INT type
		self.cube(["int", "+", "int"])	= "int"
		self.cube(["int", "-", "int"])	= "int"
		self.cube(["int", "*", "int"])	= "int"
		self.cube(["int", "/", "int"])	= "int"
		self.cube(["int", ">", "int"])	= "bool"
		self.cube(["int", "<", "int"])	= "bool"
		self.cube(["int", ">=", "int"])	= "bool"
		self.cube(["int", "<=", "int"])	= "bool"
		self.cube(["int", "==", "int"])	= "bool"
		self.cube(["int", "!=", "int"])	= "bool"

		#FLOAT type
		self.cube(["float", "+", "float"])	= "float"
		self.cube(["float", "-", "float"])	= "float"
		self.cube(["float", "*", "float"])	= "float"
		self.cube(["float", "/", "float"])	= "float"
		self.cube(["float", ">", "float"])	= "bool"
		self.cube(["float", "<", "float"])	= "bool"
		self.cube(["float", ">=", "float"])	= "bool"
		self.cube(["float", "<=", "float"])	= "bool"
		self.cube(["float", "==", "float"])	= "bool"
		self.cube(["float", "!=", "float"])	= "bool"

		#FLOAT and INT type
		self.cube(["float", "+", "int"])	= "float"
		self.cube(["float", "-", "int"])	= "float"
		self.cube(["float", "*", "int"])	= "float"
		self.cube(["float", "/", "int"])	= "float"
		self.cube(["float", ">", "int"])	= "bool"
		self.cube(["float", "<", "int"])	= "bool"
		self.cube(["float", ">=", "int"])	= "bool"
		self.cube(["float", "<=", "int"])	= "bool"
		self.cube(["float", "==", "int"])	= "bool"
		self.cube(["float", "!=", "int"])	= "bool"

		#FLOAT type
		self.cube(["int", "+", "float"])	= "float"
		self.cube(["int", "-", "float"])	= "float"
		self.cube(["int", "*", "float"])	= "float"
		self.cube(["int", "/", "float"])	= "float"
		self.cube(["int", ">", "float"])	= "bool"
		self.cube(["int", "<", "float"])	= "bool"
		self.cube(["int", ">=", "float"])	= "bool"
		self.cube(["int", "<=", "float"])	= "bool"
		self.cube(["int", "==", "float"])	= "bool"
		self.cube(["int", "!=", "float"])	= "bool"

		#BOOL type
		self.cube(["bool", "&&", "bool"])	= "bool"
		self.cube(["bool", "||", "bool"])	= "bool"
		self.cube(["bool", "<", "bool"])	= "bool"
		self.cube(["bool", ">", "bool"])	= "bool"
		self.cube(["bool", "<=", "bool"])	= "bool"
		self.cube(["bool", ">=", "bool"])	= "bool"
		self.cube(["bool", "==", "bool"])	= "bool"
		self.cube(["bool", "!=", "bool"])	= "bool"
