import random

def start_game():
  # Display an intro/welcome message to the player. print the name of game in bold.
  print()
  bold = "\033[1m"
  reset = "\033[0;0m"
  print("==========> Welcome to the " + bold + "Number Guessing Games" + reset + " <==========")
  print()
  
  play_again = 'iZni'
  
  while True:
    try:
    
      nums =[] # list for entered numbers
      trial = [] # list for number of trials (len(nums))
      answer_num = int(random.randint(1,10)) #Store a random number as the answer/solution.
      pick_num = input("Pick a number between 1 and 10: ")
      
      while True:
        nums.append(pick_num) # add the entered values to the nums list
        if int(pick_num)>10:
          print("Please, pick a number between 1 and 10 (including)")
        elif answer_num>int(pick_num):
          print("It is higher")
        elif answer_num<int(pick_num):
          print("It is lower")
        
          
          #Continuously prompt the player for a guess.
          #a.If the guess greater than the solution, display to the player "It's lower".
          #b. If the guess is less than the solution, display to the player "It's higher".
          
        elif answer_num == int(pick_num):
          print("You got it, congrats! It took",len(nums),"tries")
          #Once the guess is correct, stop looping, inform the user they "Got it"
          #and show how many attempts it took them to get the correct number.
          
          trial.append(int(len(nums))) #add the length of list(nums) to find the highest score
          print()
          
          answer_num = int(random.randint(1,10)) # we need a new random value
          play_again = input("Would you like to play again? [y]es/[n]o ")  # ask if the player wants to play again
          print("The HIGHEST SCORE is", min(trial))  # displaying the highest score by finding the smallest value of trials
          del nums[:] # delete the list nums so that we could insert new values
          
          while play_again != "n":
            
            pick_num = input("Pick a number between 1 and 10: ")
            nums.append(pick_num)
            if int(pick_num)>10:
              print("Please, pick a number between 1 and 10 (including)")
            elif answer_num>int(pick_num):
              print("It is higher")
            elif answer_num<int(pick_num):
              print("It is lower")
            
            elif answer_num == int(pick_num):
              print("You got it, congrats! It took",len(nums),"tries")
              trial.append(int(len(nums)))
              print("The HIGHEST SCORE is", min(trial))
              del nums[:]
              print()
              answer_num = int(random.randint(1,10))
              play_again = input("Would you like to play again? [y]es/[n]o ")
          if play_again == "n":  # if the player enter n, while loop stops and the game ends
        
            print("Closing game, see you next time!")
            break
        pick_num = input("Pick a number between 1 and 10: ")
          
    except ValueError:
      print("You have to choose a number between 1 and 10")
        
    if play_again == "n":
      break
    
    
if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
  start_game()
