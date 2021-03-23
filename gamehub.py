import snake
import tic

n=int(input("Enter input as 1.Hangman 2.TIC TAC TOE"))
if(n==1):
    execfile('snake.py')
elif(n==2):
    execfile('tic.py')
    