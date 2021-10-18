#Giles_lab6c.py 
#Created by Kaitlin Giles, 10/13/2021 
#Craps Game: Total of 7 or 11 on first roll wins
#Total of 2, 3, or 12 on first roll loses
#If neither scenario occurs on first roll, roll total becomes player's "point"
#To win, player must re-roll a total that matches the "point"
#If at any point after first roll player rolls 7, they lose
import random

d1 = 0
d2 = 0
total = 0

def rollDice(d1, d2):
	d1 = random.randint(1,6)
	d2 = random.randint(1,6)
	total = d1 + d2
	print 'your roll is: ', d1, ' and ', d2, ' for a total of ', total 
	return d1, d2, total

def getPoint(d1, d2):
	point = d1 + d2
	print 'Your point is ', point
	return point

def checkWin(total):
	if total == point: 
		print 'You win!'
		return True
	if total == 7:
		print 'You lose.'
		return True
	return False

d1, d2, total = rollDice(d1, d2)

if(total == 2 or total == 3 or total == 12): print 'You lose.'

if(total == 7 or total == 11): print 'You win!'

else: 
	point = getPoint(d1, d2)
	d1, d2, total = rollDice(d1, d2)
	boolWin = checkWin(total)
	
	while boolWin == False:
		d1, d2, total = rollDice(d1, d2)
		boolWin = checkWin(total)

		
