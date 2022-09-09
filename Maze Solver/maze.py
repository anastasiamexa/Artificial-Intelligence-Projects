import queue

# creates the maze (2 examples)
# S is the starting point and X is the exit point
def draw_maze():
	maze = []
	maze.append(["■","■", "■", "■", "■"])
	maze.append(["■"," ", "■", " ", "■"])
	maze.append(["■"," ", " ", " ", "X"])
	maze.append(["■"," ", " ", "■", " "])
	maze.append(["S"," ", "■", "■", "■"])

	return maze


def draw_maze2():
	maze = []
	maze.append(["■","■", "■", "■", "■", "■", "■", "X", "■"])
	maze.append(["■"," ", " ", " ", " ", " ", " ", " ", "■"])
	maze.append(["■","■", "■", " ", "■", "■", "■", " ", "■"])
	maze.append(["■"," ", "■", " ", "■", " ", "■", " ", "■"])
	maze.append(["■"," ", "■", " ", "■", " ", " ", " ", "■"])
	maze.append(["■"," ", "■", " ", "■", " ", "■", " ", "■"])
	maze.append(["■"," ", "■", " ", "■", " ", "■", " ", "■"])
	maze.append(["■"," ", " ", " ", " ", " ", "■", " ", "■"])
	maze.append(["S"," ", "■", "■", "■", "■", "■", "■", "■"])

	return maze

def find_start_points(maze):	# finds the coordinates of the starting point
	for l in range(0,len(maze)):	# for every row
		for x, pos in enumerate(maze[l]):	# for every column
			#print(x, pos)
			if pos == "S":
				i = x	# column
				j = l	# row
				return i, j

def print_maze(maze, path=""):	# printing the final maze with solution
	i, j = find_start_points(maze)
	pos = set()
	for move in path:
		if move == "L":
			i -= 1
		elif move == "R":
			i += 1
		elif move == "U":
			j -= 1
		elif move == "D":
			j += 1
		pos.add((j, i))
		
	for j, row in enumerate(maze):
		for i, col in enumerate(row):
			if (j, i) in pos:	#  for every point in the solution path
				print("x ", end="")	# mark
				
			else:
				print(col + " ", end="")
		print()



def valid_move(maze, moves):	# check if the move is valid
	i, j = find_start_points(maze)
	for move in moves:
		if move == "L":
			i -= 1

		elif move == "R":
			i += 1

		elif move == "U":
			j -= 1

		elif move == "D":
			j += 1
		#print(i, j)
		if not(0 <= i < len(maze) and 0 <= j < len(maze)): # outside the borders of the maze
			#print("false")
			return False
		elif (maze[j][i] == "■"): # wall
			#print("false")
			return False
	#print("true")
	return True


def find_end(maze, moves):	# finds the coordinates of the exit point
	i, j = find_start_points(maze)
	for move in moves:
		if move == "L":
			i -= 1

		elif move == "R":
			i += 1

		elif move == "U":
			j -= 1

		elif move == "D":
			j += 1

	if maze[j][i] == "X": 	# if we reached the exit point, print solution
		print("\nFound: " + moves)
		print_maze(maze, moves)
		return True

	return False


combinations = queue.Queue()
combinations.put("")
lst = ""
maze  = draw_maze()
print("1. Breadth First Search")
print("2. Depth First Search\n")

# cheking user input
while True:
	try:
		inp = int(input("Enter your choice: "))
		if inp < 1 or inp > 2:
			raise ValueError
		break
	except ValueError:
		print("Please enter a valid choice\n")
		
	
while not find_end(maze, lst): # run until we reach the exit point
	lst = combinations.get()
	#print(lst)
	if inp == 1:
		s = ["L", "R", "U", "D"] # Breadth First Search
	else:
		s = ["U", "R", "D", "L"] # Depth First Search
	for j in s:	# for its move (left, right, etc...)
		put = lst + j
		if valid_move(maze, put):	# if move is valid
			combinations.put(put)	# remember the valid move