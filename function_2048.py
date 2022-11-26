import random

def start_game():
    
	matrix =[]
	for i in range(4):
		matrix.append([0] * 4)

	# printing controls for user
	print("How to play: ")
	print("'w' : Move Up")
	print("'s' : Move Down")
	print("'a' : Move Left")
	print("'d' : Move Right")

	# add value to the matrix
	add_new_2(matrix)
	add_new_2(matrix)
	return matrix

# To add a new 2 in a random empty cell:
def add_new_2(matrix):
    # Add 2 if there is empty cell:
    if can_add(matrix):
        r = random.randint(0, 3)
        c = random.randint(0, 3)
        # Use a while loop to finally get to the empty cell:
        while(matrix[r][c] != 0):
            r = random.randint(0, 3)
            c = random.randint(0, 3)
        matrix[r][c] = 2 # put a new 2 on that empty cell.
    else:
        print('You cannot move this direction.\nTry different command!')

# Check if there is empty cell to add 2:
def can_add(matrix):
    for r in matrix:
        for c in r:
            if c == 0:
                return True
    return False

# To get the current game state:
def get_current_state(matrix):

	# if any cell contains 2048, we won:
	for i in range(4):
		for j in range(4):
			if(matrix[i][j]== 2048):
				return 'Won'

	# if there are still at least one empty cell, game continues:
	for i in range(4):
		for j in range(4):
			if(matrix[i][j]== 0):
				return 'continues'

	# If no cell is empty now, but there could be two cells be merged after any move left, right, up or down, game continues.
	for i in range(3):
		for j in range(3):
			if(matrix[i][j]== matrix[i + 1][j] or matrix[i][j]== matrix[i][j + 1]):
				return 'continues'
	for j in range(3):
		if(matrix[3][j]== matrix[3][j + 1]):
			return 'continues'
	for i in range(3):
		if(matrix[i][3]== matrix[i + 1][3]):
			return 'continues'

	# else we have lost the game
	return 'Lost'

# Compress the metrix so no empty cells between values:
def compress(matrix):
	changed = False # initiate a bool variable to determine if the metrix changes after compressing.
	new_matrix = [] # create a new matrix to store the cells after compress
	for i in range(4):
		new_matrix.append([0] * 4) # set all cells of the new matrix as empty.
		
	# move all values in the cells to the very left:
	for i in range(4):
		pos = 0
		for j in range(4):
			if(matrix[i][j] != 0):
				new_matrix[i][pos] = matrix[i][j]
				# if the current cell is different with the cell in old matrix, the matrix is changed:
				if(j != pos):
					changed = True
				pos += 1

	return new_matrix, changed

# Merge cells if two adjacent cells has the same value:
def merge(matrix):
	changed = False # initiate a bool variable to determine if the matrix changes after merging.
	for i in range(4):
		for j in range(3):

			# merge the adjacent cells:
			if(matrix[i][j] == matrix[i][j + 1] and matrix[i][j] != 0):
				matrix[i][j] = matrix[i][j] * 2 # the value of the first cell doubles.
				matrix[i][j + 1] = 0 # the value of the second cell changes to empty.
				changed = True # the matrix is changed.

	return matrix, changed

# reverse rows:
def reverse(matrix):
	new_matrix =[]
	for i in range(4):
		new_matrix.append([])
		for j in range(4):
			new_matrix[i].append(matrix[i][3 - j])
	return new_matrix

# interchanging rows and column:
def interchange(matrix):
	new_matrix = []
	for i in range(4):
		new_matrix.append([])
		for j in range(4):
			new_matrix[i].append(matrix[j][i])
	return new_matrix

# to update the matrix:
# move left:
def move_left(matrix):
	temp, changed1 = compress(matrix) # compress the metrix
	temp, changed2 = merge(temp) # merge the cells.
	temp, changed3 = compress(temp) # compress the metrix again after merging
	changed = changed1 or changed2 or changed3 # determine if the matrix has been changed
	return temp, changed

# move right:
def move_right(matrix):
	temp = reverse(matrix) # reverse the rows so we can use the same compress and merge fucntions as moving left.
	temp, changed = move_left(temp)
	temp = reverse(temp) # reverse the rows back to their original order.
	return temp, changed

# move up:
def move_up(matrix):
	temp = interchange(matrix) # interchange the rows and columns so we can use the same compress and merge fucntions as moving left.
	temp, changed = move_left(temp)
	temp = interchange(temp) # interchange the rows and columns back to their original order.
	return temp, changed

# if we move / swipe down
def move_down(matrix):
	temp = interchange(matrix) # interchange the rows and columns so we can use the same compress and merge fucntions as moving right.
	temp, changed = move_right(temp)
	temp = interchange(temp) # interchange the rows and columns back to their original order.
	return temp, changed

# print the metrix row by row:
def print_mat(matrix):
    for i in range(4):
        print(matrix[i])
