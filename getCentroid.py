# This program calculates the centroid of the structure that has been outlined with landmarks with tpsDig, i.e. centroid of a set of points.
# To use this, please consider the tps file structure example that was used to program the algorithm:
#
# LM=8
# 1,00000 1,00000
# 2,00000 2,00000
# 3,00000 2,00000
# 4,00000 1,00000
# 1,00000 3,00000
# 2,00000 4,00000
# 3,00000 4,00000
# 4,00000 3,00000
# IMAGE=xyz.jpg
# ID=0
# LM=3
# 1,00000 1,00000
# 2,00000 2,00000
# 1,00000 3,00000
# IMAGE=yzx.jpg
# ID=1
#
# To run the program, open the command prompt inside the folder where is both the tps file and this file
# Type the command:
#
# python2 getCentroid.py <your_file's_name>.tps
# or
# python3 getCentroid.py <your_file's_name>.tps
#
# After it's done, the results will be saved in the same folder in a file named <your_file's_name>_CENTROID.tps
import sys

f = open(sys.argv[1])

newCoordinates = False

coordinatesList_x = []
coordinatesList_y = []

specimen = 0
x_bool = True
y_bool = False
number = ""

centroid_file = open(str(sys.argv[1][:-4])+"_CENTROID.txt",'w')

for line in f:
	if line[:2] == "LM":
		# New coordinates to add to the list in the next loop
		newCoordinates = True
		sum_x = 0
		sum_y = 0

		landmarks_total = int(line[3:])
	elif line[:5] == "IMAGE":
		# Reaching the end of the coordinates
		newCoordinates = False
		specimen+=1
		print(line, file=centroid_file)
	elif line[:3] == "ID=":

		ID_number = line[3:]

		# Calculate centroid
		for coordX in coordinatesList_x:
			sum_x += int(coordX)
		centroid_x = sum_x/landmarks_total
		
		for coordY in coordinatesList_y:
			sum_y += int(coordY)
		centroid_y = sum_y/landmarks_total
		
		# Prints the calculated centroid after its specimen's ID
		print("ID= " + ID_number, file = centroid_file)
		print("Centroid:\n" + str(centroid_x) + " " + str(centroid_y), file = centroid_file)
		print("---------------------\n", file = centroid_file)

		#Set new list
		coordinatesList_x = []
		coordinatesList_y = []

	elif newCoordinates == True: # Getting the list of coordinates
		for character in line:
			if character == " ": # If there's a space, next there's going to be the y coordinate
				y_bool = True
			elif character == ",": 
			# As there isn't any number besides zero after the comma in the tps file, the coordinate will be appended to the list
				if x_bool:
					# Appending x coordinates to list
					coordinatesList_x.append(number)
					number = ""
					x_bool = False
				elif y_bool:
					# Appending y coordinates to list
					coordinatesList_y.append(number)
					number = ""
					y_bool = False
			elif y_bool or x_bool:
				number += str(character)
			elif character == "\n":
				x_bool = True

f.close()
centroid_file.close()
