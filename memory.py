import sys


class MemoryMap:

	def __init__(self, stage):
		if stage == "program":
			self.INT_LOC = 5000
			self.MAX_INT_LOC = 9999
			self.FLOAT_LOC = 10000
			self.MAX_FLOAT_LOC = 14999
			self.BOOL_LOC = 15000
			self.MAX_BOOL_LOC = 19999

		if stage == "function":
			self.INT_LOC = 20000
			self.MAX_INT_LOC = 24999
			self.FLOAT_LOC = 25000
			self.MAX_FLOAT_LOC = 29999
			self.BOOL_LOC = 30000
			self.MAX_BOOL_LOC = 34999

		if stage == "temporal":
			self.INT_LOC = 35000
			self.MAX_INT_LOC = 39999
			self.FLOAT_LOC = 40000
			self.MAX_FLOAT_LOC = 44999
			self.BOOL_LOC = 45000
			self.MAX_BOOL_LOC = 49999

	def get_next_address(self, t):
		total_space = 0
		if 