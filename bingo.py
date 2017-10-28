import numpy as np
from collections import defaultdict
import random

def checkBingo(bolded):
    rowsum = np.sum(bolded, axis=1)
    colsum = np.sum(bolded, axis=0)
    diag1sum = bolded[0][0] + bolded[1][1] + bolded[2][2]
    diag2sum = bolded[2][0] + bolded[1][1] + bolded[0][2]
    if ((3 in rowsum) or (3 in colsum) or (diag1sum == 3) or (diag2sum==3)):
        return True
    return False

def getDiceSum():
    a = random.randint(1,6)
    b = random.randint(1,6)
    return(a+b)


def runSimulation(boards, bolded, boardCurrent, scoreDict):
    #boards is list of list of 9 elements
    
    
    for i in range(100):
        #to get the number of turns it takes to win
        if len(scoreDict.values()) == len(boards): #stopping condition
        	break
        roll = getDiceSum()
        for board in boards:
            grid = np.asarray(boardCurrent[tuple(board)]).reshape(3,3)
            mod = grid % roll #list of remainders
            if 0 in mod:
                xindex, yindex = np.where(mod==0) #get index of mod 0 
            else:
            	continue
            indexes = []
            for k in range(len(xindex)):
                indexes.append([xindex[k], yindex[k]])
            choice = random.choice(indexes)
            
            grid[choice[0], choice[1]] = -1
            boldedcheck = np.asarray(bolded[tuple(board)]).reshape(3,3)
            boldedcheck[choice[0], choice[1]] = 1
            
            if checkBingo(boldedcheck) and scoreDict[tuple(board)] == 0:
                # print "bingo"
                # print "no of trials = " + str(i+1)
                scoreDictCollection[tuple(board)].append(i+1)

            boardCurrent[tuple(board)] = grid.reshape(1,-1)[0] #re assign grid to boards
            bolded[tuple(board)] = boldedcheck.reshape(1,-1)[0] #change the bolded grid
    return boards, bolded

boards = [[20, 3, 9, 14, 18, 15, 8, 7, 12], [20, 9, 3, 14, 18, 15, 8, 12, 7]]
# [20, 3, 5, 14, 18, 15, 8, 7, 12]
#[14,12,16, 6,18,15, 11,18,10],
scoreDictCollection = defaultdict(lambda: []) #for scores

# [8, 7, 12, 14, 18, 15, 20, 3, 5]
trailnos =100000
for j in range(trailnos):
	boardCurrent = defaultdict(lambda: np.zeros(9))
	scoreDict = defaultdict(int)
	for board in boards:
		boardCurrent[tuple(board)] = board
	bolded = defaultdict(lambda: np.zeros(9))  #for keeping a track of bolded numbers
	# import ipdb; ipdb.set_trace()
	boards, bolded = runSimulation(boards, bolded, boardCurrent, scoreDict)

for board in boards:
	print np.mean(scoreDictCollection[tuple(board)])