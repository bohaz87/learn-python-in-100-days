class Point:
	def __init__(self, x = 0, y = 0) -> None:
		self.x, self.y = x, y

	def distance_to(self, other):
		dx = self.x - other.x
		dy = self.y - other.y
		return (dx*dx + dy * dy) ** 0.5
	
	def __str__(self) -> str:
		return f'({self.x}, {self.y})'

pa = Point(1, 1)
pb = Point(2, 2)
print(pa, pb)
print(pa.distance_to(pb))
