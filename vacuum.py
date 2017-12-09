#!/usr/bin/env python

#-------file opening-------#
file = open("instructions.txt", "r")
#-------file opening-------#

#-------variable declaration-------#
size = 3;
matrix = [[0 for x in range(size)] for y in range(size)] 
directions = ['N', 'E', 'S', 'W']
x = 0
dir_index = 0

#-------input file analysis-------#
for lines in file:
    matrix[x] = lines.split()
    x += 1
#-------input file analysis-------#

size_x = int(matrix[0][0])
size_y = int(matrix[0][1])

pos_x = int(matrix[1][0])
pos_y = int(matrix[1][1])
pos_dir = matrix[1][2]

instructions = matrix[2][0]
#-------variable declaration-------#

#-------closing the input file-------#
file.close()
#-------closing the input file-------#

#-------direction instrutctions analysis-------#
if pos_dir == 'N':
    dir_index = 0
if pos_dir == 'E':
    dir_index = 1
if pos_dir == 'S':
    dir_index = 2
if pos_dir == 'W':
    dir_index = 3
#-------direction instrutctions analysis-------#


#-------debug prints-------#
def debug_prints():
    print ("size_x = %d" %size_x)
    print ("size_y = %d" %size_y)
    print
    print ("pos_x = %d" %pos_x)
    print ("pos_y = %d" %pos_y)
    print ("pos_dir = %c" %pos_dir)
    print
    print ("instructions = %s" %instructions)
    print
    print
#-------debug prints-------#

#debug_prints()

#-------instructions analysis and processing-------#
for char in instructions:
    if dir_index > 3:
        dir_index = 0
    if char == 'D':
        dir_index += 1
    if char == 'G':
        dir_index -= 1
    if char == 'A':
        if pos_x < size_x and pos_y < size_y and pos_x > 0 and pos_y > 0:
            if directions[dir_index] == 'N':
                pos_y += 1
            elif directions[dir_index] == 'S':
                pos_y -= 1
            elif directions[dir_index] == 'E':
                pos_x += 1
            elif directions[dir_index] == 'W':
                pos_x -= 1
    if char == 'R':
        if pos_x < size_x and pos_y < size_y and pos_x > 0 and pos_y > 0:
            if directions[dir_index] == 'N':
                pos_y -= 1
            elif directions[dir_index] == 'S':
                pos_y += 1
            elif directions[dir_index] == 'E':
                pos_x -= 1
            elif directions[dir_index] == 'W':
                pos_x += 1
#-------instructions analysis and processing-------#

#-------final print of the result-------#
print ("%d " %pos_x + "%d "  %pos_y + "%c" %pos_dir)
#-------final print of the result-------#
