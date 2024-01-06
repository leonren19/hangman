# 10.1 Hangman
# L Ren
# Apr 9, 2021
# https://replit.com/@LeonRen2/final-101-Hangman#main.py

# import module
from os import system, name
import random

# global variables
word_list = ["wolves", "python", "compsci", "future", "computer"]
users_word = "" # rep correct guessed letters
given_word = [] # rep num of hyphens for the letter count in word
given_word_space = "" 
guessed_letters = [] # rep the letters the user has guessed 
word_choice = "" # rep the word choice 
number_of_guesses_left = 8 # rep the num of guesses left 

# functions
def clear_the_screen(): # clears the screen
  if name == "nt":
    _ = system("cls")
  else:
    _ = system("clear")

def title(): # decorative title and says hangman game  
  print("---------------- HANGMAN GAME ----------------")
  print()

def instructions(): # describes the instructions and rules to the user 
  title()
  print("welcome my to hangman game! the objective is to guess the hidden word by guessing letters.")
  print()
  input("press enter key to proceed: ")

def feedback(): # what is given to the user after input like num of guesses left 
  global word_choice
  global given_word
  global given_word_space
  for letter in (word_choice):
    if len(given_word) == len(word_choice):
      break
    else:
      "\n"
      given_word.append("_")
      given_word_space += ("_ ")
  print()
  print ("the word has", len(word_choice), "letters")
  print ("you have", number_of_guesses_left, "guesses")
  print()
  print(given_word_space)
  print()
  print("________________________________________")
  print()
  game()

def game(): # the game itself in which it ultimately decides if the users input correlates to the given word 
  global users_word # make global
  global word_choice # make global
  global guesssed_letters # make global
  global guess_letter # make global
  global number_of_guesses_left # make global
  global given_word # make global
  global given_word_space # make global
  while (users_word != word_choice and number_of_guesses_left > 0):
    print() 
    guess_letter = input("guess a letter: ") # asks the user to guess a letter 
    # checks for constraints
    if (guess_letter.isalpha() == False): # describes if the input is not a letter
      print ("please choose a letter")
      continue
    elif (guess_letter in guessed_letters):
      print()
      print ("you've already guessed that letter")
      continue
    elif (len(guess_letter) > 1):
      guess_letter = guess_letter.lower()
      if (guess_letter == word_choice): # if guess letter is equal to the word choice 
        users_word = word_choice
        break
      else:
        print("that isn't the word, try again.")
        number_of_guesses_left -= 1
        print("you have", number_of_guesses_left, "guesses left")
        continue
    else:
      # start of game
      guess_letter = guess_letter.lower()
      guessed_letters.append(guess_letter)
      if (guess_letter not in word_choice):
        number_of_guesses_left -= 1
        print()
        print("that letter's not part of the word")
        print()
        print("the guessed Letters: ")
        print(", ".join(guessed_letters))
        print()
        print ("you have", number_of_guesses_left, "guesses left")
        print()
        print("________________________________________")
        continue
      for i in range(len(word_choice)):
        if (guess_letter == word_choice[i]): 
          given_word[i] = guess_letter
          users_word = "".join(given_word)
          given_word_space = " ".join(given_word)
      print (given_word_space)
      print()
      print("the guessed Letters: ")
      print(", ".join(guessed_letters))
      print()
      number_of_guesses_left -= 1
      print()
      print("you have", number_of_guesses_left, "guesses left")
      print()
      print("________________________________________")    
  if (users_word == word_choice): # talks about when the user wins from having the user word be the same as word choice 
    print()
    print("the word is: " + word_choice)
    print ("YAY! YOU WIN! :) ")
  else: # ralks about when the user loses is anything else other than user word being the same as word choice 
    print()
    print("the word is: " + word_choice)
    print("you lost. you didn't guess the word. play again. :(")

def play_the_game(): # starts the game and is what is actually run 
  instructions()
  global word_choice # make globa; 
  clear_the_screen()
  title()
  num = int(input("first, choose a number (1-6): "))
  if num < 1 or num > 6: # in case the input number is out of bounds 
    print("error: not a valid input. press enter to try again.")
    input()
    clear_the_screen() # all of the funds being in one place 
    play_the_game()
  word_choice = word_list[num-1]
  feedback()

# start here 
play_the_game()