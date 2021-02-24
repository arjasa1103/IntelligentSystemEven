class Node:

	def __init__(self, parent=None, position=None):
		self.parent = parent
		self.position = position

		self.g = 0
		self.h = 0
		self.f = 0

	def __eq__(self, other):
		return self.position == other.position

def aStar(maze, start, end):
	# Create start and end node

	# Initialize both open and closed list

	# Add the start node

	# Loop until you find the end

		#  Get the current node

		# Pop current off open list, add to closed list

		# Found the goal

		# Generate children of adjacent squares

			# Get node position

			# Make sure within range

			# Make sure walkable terrain

			# Create new node

			# Append

		# Loop through children

			# Child is on the closed list

			# Create the f, g, and h values

			# Child is already in the open list

			# Add the child to the open list

def main(): 

	# Generate maze
	maze = [
		[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	]

	start = (0, 0)
	end = (7, 6)

	path = astar(maze, start, end)
	print(path)

if __name__ == "__main__":
	main()