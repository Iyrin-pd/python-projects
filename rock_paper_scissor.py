import random

print("               WELCOME TO THE GAME                    ")
print("             ROCK - PAPER - SCISSORS                  ")
print("____________________________________________________")
print("                                                     ")
print("Game Rules are as follows : ")
print(" ")
print("Rock - Scissors ---> Rock Wins")
print("Scissors - Paper ---> Scissors Wins")
print("Paper - Rock ---> Paper Wims")
print(" ")
while True:
  print("Your Choices are as follows")
  print("1 for Rock")
  print("2 for Paper")
  print("3 for Scissors")
  print(" ")
  Your_Choice=int(input("Enter your choice : "))

  if Your_Choice==1:
    print("Rock")
  elif Your_Choice==2:
    print("Paper")
  else:
    print("Scissors")

  print(" ")

  Computer_Choice=random.randint(1,3)

  print(" ")

  print("Now its computer's turn...")
  print("Computer's Choice : ",Computer_Choice)

  if Computer_Choice==1:
    print("Rock")
  elif Computer_Choice==2:
    print("Paper")
  else:
    print("Scissors")

  print(" ")
  
  if Your_Choice==Computer_Choice:
    print("It's a DRAW MATCH")
  elif (Your_Choice==1 and Computer_Choice==2) or (Your_Choice==3 and Computer_Choice==1) or (Your_Choice==2 and Computer_Choice==3):
    print("Computer WON !!!")
  elif (Your_Choice==2 and Computer_Choice==1) or (Your_Choice==1 and Computer_Choice==3) or (Your_Choice==3 and Computer_Choice==2):
    print("You WON !!!")
 
  print(" ")
  print("Do you want to play again?(yes/no) ")
  ans=input("Answer please : ")
  if ans=="no":
     break

print(" ")
print("Thanks for playing , See you next time !!")