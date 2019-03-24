class Robot:
	def __init__(self):
		self.x = 0
		self.y = 0
	
	
	def up(self, number):
		self.y -= number
	
	
	def down(self, number):
		self.y += number
	
	
	def left(self, number):
		self.x -= number
	
	
	def right(self, number):
		self.x += number
	
	
	def compute_distance(self):
		return round((abs(self.x) ** 2 + abs(self.y) ** 2) ** 0.5)
	
	
	def print_status(self):
		print(self.compute_distance())


robot_action = {
	"UP": Robot.up,
	"DOWN": Robot.down,
	"LEFT": Robot.left,
	"RIGHT": Robot.right,
}

robot = Robot()

while True:
	action = input().split(" ")
	robot_action[action[0]](robot, int(action[1]))
	robot.print_status()
