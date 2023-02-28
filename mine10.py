#Welcome to Py-sweeper!



#Importing random to create random mine positions
import random
#
inmenu = True
gaff = 0
help = ["help", "Help", "HELP"]
quit = ["Quit","QUIT","quit"]
start = ["start","Start","START"]  
menu = ["Menu","MENU","menu"]
dig = ['dig', 'Dig', 'DIG']
flag = ['flag', 'Flag', 'FLAG']
unflag = ['unflag', 'Unflag', 'UNFLAG', 'UnFlag']
while inmenu == True:
	
	userinput = str(input("--== Welcome to Py-sweeper! ==-- \nType 'Start' to start, or type 'Quit' to quit. \nYou may type 'Help' at any time to print all accepted commands.\n>>"))
	
	if userinput in quit:
		exit("quit detected")
	
	elif userinput in help:
		print("Type all commands as they are written, and press enter.\nStart\nQuit\nHelp\n")
	
	elif userinput in start:
		done = False
		while done == False:
			userinput = str(input("What difficulty game would you like?\n>>"))
			beginner = ["beginner", "Beginner", "BEGINNER"]
			intermediate = ["intermediate", "Intermediate", "INTERMEDIATE"]
			advanced = ["advanced", "Advanced", "ADVANCED"]
			custom = ["custom", "Custom", "CUSTOM"]
			if userinput in beginner:
				gridsizex = 9
				gridsizey = 9
				difficulty = 10
				done = True
			elif userinput in intermediate:
				gridsizex = 16
				gridsizey = 16
				difficulty = 40
				done = True
			elif userinput in advanced:
				gridsizex = 16
				gridsizey = 30
				difficulty = 99
				done = True
			elif userinput in custom:
				gridsizey = int(input("How large would you like the width of your grid?\n>>"))
				gridsizex = int(input("How large would you like the height of your grid?\n>>"))
				difficulty = int(input("How many bombs will be on the board?\n>>"))
				if (gridsizex*gridsizey) < difficulty:
					#print(gridsizex*gridsizey, difficulty)
					print("Error: More bombs than grid squares")
				else:
					done = True
			elif userinput in help:
				print("Accepted commands are 'Beginner', 'Intermediate', Advanced', or 'Custom'.")
			else:
				print("Error: User entered '" + userinput + "'. Type 'Help' for a list of commands.")



		grid = []
		for x in range(gridsizex):
			row = []
			for y in range(gridsizey):
				row.append('.')
			grid.append(row.copy())

		screen = []
		for x in range(gridsizex):
			row = []
			for y in range(gridsizey):
				row.append('#')
			screen.append(row.copy())

		def printgrid():
			for x in range(gridsizex):
				printrow = ''
				for y in range(gridsizey):
					printrow += str(grid[x][y])
				print(printrow)

		def printscreen():
			for x in range(gridsizex):
				printrow = ''
				for y in range(gridsizey):
					printrow += str(screen[x][y])
				printrow += '|' + str(x)
				print(printrow)
			b0 = ''
			b1 = ''
			b2 = ''
			for x in range(gridsizey):
				if x < 10:
					b1 += str(x)
					b2 +=' '
				else:
					b1 += str(x)[0]
					b2 += str(x)[1]
				b0 += '='
			print(b0)
			print(b1)
			print(b2)



		bombs = []
		x = 1
		while x <= difficulty:
			x1 = random.randint(0, gridsizex - 1)
			y1 = random.randint(0, gridsizey - 1)
			if grid[x1][y1] == 'F':
				continue
			else:
				grid[x1][y1] = 'F'
				bombs.append([y1, x1])
				x += 1

		for x in range(gridsizex):
			for y in range(gridsizey):
				count = 0
				for a in range(-1, 2):
					for b in range(-1, 2):
						if grid[x][y] == 'F':
							continue
						if not x+a in range(gridsizex) or not y+b in range(gridsizey):
							continue
						if grid[x+a][y+b] == 'F':
							count += 1
				if count == 0:
					continue
				else:
					grid[x][y] = count

		#printgrid()
		printscreen()
		#print(bombs)
		Gaming = True
		userinput = False


		while Gaming:
			command = input("Type your command, followed by the x and y coordinates. Or, type 'Help' for commands.\n>>")
			if command in help:
				print("Accepted commands are 'Dig', 'Flag', and 'Unflag'.")
			command = command.replace(" ", ",")
			command = command.replace(",,", ",")
			comma = 0
			for x in command:
				#print(x)
				if x == ",":
					comma += 1
					#print("adding")
			if ',' in command and comma == 2:
				x,y,z = command.split(',')
				str(x)
				y = int(y)
				z = int(z)
				#print(x,y,z)
				userinput = True
				if not (y in range(gridsizex) and z in range(gridsizey)):
					userinput = False
					print("Error: coordinates outside of grid")
			else:
				print('Error. User entered:',command)
			
			if userinput == True:
				if x in dig:
					if grid[z][y] == ".":
						#print("success")
						xval = []
						yval = []
						xval.append(y)
						yval.append(z)
						popped = True
						while popped == True:
							popped = False
							xvalnew = []
							yvalnew = []
							for l in range(len(xval)):
								for a in range(-1, 2):
									for b in range(-1, 2):
										#print(yval[l]+b, xval[l]+a)
										if 0 > yval[l]+b or yval[l]+b >= gridsizey or 0 > xval[l]+a or xval[l]+a >= gridsizex:
											#print("skipped")
											continue
										elif grid[yval[l]+b][xval[l]+a] == "." and screen[yval[l]+b][xval[l]+a] == "#":
											xvalnew.append(xval[l]+a)
											yvalnew.append(yval[l]+b)
											screen[yval[l]+b][xval[l]+a] = grid[yval[l]+b][xval[l]+a]
											#print("blank space")
										else:
											screen[yval[l]+b][xval[l]+a] = grid[yval[l]+b][xval[l]+a]
											#print("number")
							#print("checking to see if we're done")
							if len(xvalnew) > 0:
								#print(len(xvalnew))
								popped = True
								xval = xvalnew
								yval = yvalnew
					
					if grid[z][y] in range(0, 10):
						screen[z][y] = grid[z][y]
					
					if grid[z][y] == "F":
						for a in range(gridsizex):
							for b in range(gridsizey):
								if grid[a][b] == 'F' and not screen[a][b] == 'F':
									screen[a][b] = '@'
								if screen[a][b] == 'F' and not grid[a][b] == 'F':
									screen[a][b] = 'X'
						
						
						print("KABOOM")
						Gaming = False
						   
					print("dug")	
				elif x in flag:
					if screen[z][y] == "#":
						screen[z][y] = "F"
						print("flagged")
					else:
						print("Can not flag square.")
				elif x in unflag:
					if screen[z][y] == "F":
						screen[z][y] = "#"
						print("unflagged")
					else:
						print("Can not unflag square.")
				else:
					print("Error: Unrecognized command '" + x + "'. Type 'Help' for a list of commands.")
				complete = 0
				for a in range(gridsizex):
					for b in range(gridsizey):
						if grid[a][b] == screen[a][b]:
							complete += 1
				if complete == gridsizex * gridsizey:
					Gaming = False
					print("Congradulations")
			
				printscreen()

		endgame = str(input("Would you like to return to the 'Menu' or 'Quit' the game?\n"))
		
		if endgame in menu:
			continue
		
		elif endgame in quit:
			inmenu = False
	else:
		
		if gaff == 0:
			print("Unknown command, please try again\n")
		
		elif gaff == 1:
			print("Unknown command, remember you can type 'Help' to print the list of commands.\n")
		
		elif gaff >= 2:
			print("Unknown command. Type all commands exactly as they are written, and press enter. These are the commands:\nStart\nQuit\nHelp\n")
		gaff += 1
