import time
import csv
import os

filename = input("Enter File Name: ")
                 
#initialize a matrix
maze =[]
#get reading from csv file
with open(filename + '.csv')as myFile:
    reader=csv.reader(myFile)
    for row in reader:
        maze.append(row)

#number of rows in the maze
SIZE = len(maze)
#number of columns in the maze
SIZE1 = len(maze[0])

#solution is stored in the matrix
solution = [[0]*SIZE1 for _ in range(SIZE)]

#support matrix for the path finding
mat= [[0]*SIZE1 for _ in range(SIZE)]

#start position
startx=0
starty=0

#end position
destx=0
desty=0

def solvemaze(r, c):
    #maze is solved if the current position of Robot is the destination
    if (r==destx) and (c==desty):
        solution[r][c] = 1;
        return True;
    
    #checking whether unvisited cells are safe to visit
    if r>=0 and c>=0 and r<SIZE and c<SIZE1 and (solution[r][c] == 0 and maze[r][c] == 0 or maze[r][c]=='S'):
        #if the next cell is not a brick robot visits it
        mat[r][c] = "R"
        
        for i in mat:
            print (*i)
            
        #delay for 1 second
        time.sleep(1)
        #print the path of the current robot
        print("\n")
        print("Robot is travelling\n")
        
        mat[r][c]='.'
        solution[r][c] = 1
        
        #first the robot will try to go down
        if solvemaze(r+1, c):
            return True
        #going right
        if solvemaze(r, c+1):
            
            return True
        #going up
        if solvemaze(r-1, c):
            
            return True
        #going left
        if solvemaze(r, c-1):
            
            return True
        #backtracking
        solution[r][c] = 0;
        mat[r][c] = "R"
        for i in mat:
            print (*i)
        time.sleep(1)
        mat[r][c]="."
        print("Robot is travelling\n")
        return False;
    return 0;


for i in range (0,SIZE):
    for j in range (0,SIZE1):
        if(maze[i][j]=='S'):      #get the source
            startx=i
            starty=j
        elif(maze[i][j]=='D'):    #get the destination
            destx=i
            desty=j
        elif(maze[i][j]=='0'):
            maze[i][j]=1
        elif(maze[i][j]=='1'):
            maze[i][j]=0
        


if(solvemaze(startx,starty)):
    for i in range (0,SIZE):
      for j in range (0,SIZE1):
         if(solution[i][j]==1):
            solution[i][j]='+'

    for i in solution:    #print final path
        print (*i)
else:
    print ("No solution")
