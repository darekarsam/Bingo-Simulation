# Bingo-Simulation
Created a simulation for modified version of Bingo as follows

Create a 3x3 bingo board using integers in [1,20]. we may use the same integer more than once.													
													
We will then play bingo as follows:													
In each turn of the game, we will roll two six sided dice and add the results. We will mark one square on your bingo board if you have at least one unmarked square that is a multiple of the total rolled (if more than one unmarked square is a multiple of the total, we will pick one at random). We will take turns until at least one board has bingo (3 marks in a row, horizontal, vertical, or diagonal). Each player whose board has bingo gets a share of the win (if n players get bingo, then each gets 1/n wins). We will simulate 10,000 games using all the bingo boards submitted. The goal is to get the most wins out of all contestants.																								
													
Example Roll													
Die 1	3												
Die 2	2												
Total	5												
													
Bolded numbers on the submitted board are all multiples of 5.  We mark one at random (in this case the 10 in the top row).													
													
													
