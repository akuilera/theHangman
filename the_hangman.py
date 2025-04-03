# -*- coding: utf-8 -*-

"""
# Game Preparation

## Console

### Imports
"""

#!pip install wonderwords
from IPython.display import clear_output
import os

from time import sleep
import wonderwords
from wonderwords import RandomWord
import random

# https://raw.githubusercontent.com/first20hours/google-10000-english/refs/heads/master/google-10000-english.txt

"""### GUI Generation"""

hanged = [
    '\n\n\t\t\t ➖➖➖➖➖➖\t🌞\n\t\t\t 🪵        🪝\n\t\t\t 🪵\n\t\t\t 🪵\n\t\t\t 🪵\n\t\t\t 🪵\n\t\t\t 🪵\n\t\t\t 🪵\t\t\t⛰️\n',
    '\n\n\t\t\t ➖➖➖➖➖➖\t🌤️\n\t\t\t 🪵        🪝\n\t\t\t 🪵        😐️\n\t\t\t 🪵\n\t\t\t 🪵\n\t\t\t 🪵\n\t\t\t 🪵\n\t\t\t 🪵\t\t\t⛰️\n',
    '\n\n\t\t\t ➖➖➖➖➖➖\t⛅️\n\t\t\t 🪵        🪝\n\t\t\t 🪵        😥\n\t\t\t 🪵        👕\n\t\t\t 🪵\n\t\t\t 🪵\n\t\t\t 🪵\n\t\t\t 🪵\t\t\t⛰️\n',
    '\n\n\t\t\t ➖➖➖➖➖➖\t☁️\n\t\t\t 🪵        🪝\n\t\t\t 🪵        😩\n\t\t\t 🪵      🫲👕\n\t\t\t 🪵\n\t\t\t 🪵\n\t\t\t 🪵\n\t\t\t 🪵\t\t\t⛰️\n',
    '\n\n\t\t\t ➖➖➖➖➖➖\t🌦️\n\t\t\t 🪵        🪝\n\t\t\t 🪵        😰\n\t\t\t 🪵      🫲👕🫱\n\t\t\t 🪵\n\t\t\t 🪵\n\t\t\t 🪵\n\t\t\t 🪵\t\t\t⛰️\n',
    '\n\n\t\t\t ➖➖➖➖➖➖\t🌧️\n\t\t\t 🪵        🪝\n\t\t\t 🪵        😵\n\t\t\t 🪵      🫲👕🫱\n\t\t\t 🪵        👖\n\t\t\t 🪵\n\t\t\t 🪵\n\t\t\t 🪵\t\t\t⛰️\n',
    '\n\n\t\t\t ➖➖➖➖➖➖\t⛈️⛈️⛈️\n\t\t\t 🪵        🪝\n\t\t\t 🪵        💀\n\t\t\t 🪵      🫲👕🫱\n\t\t\t 🪵        👖\n\t\t\t 🪵        🧦\n\t\t\t 🪵\n\t\t\t 🪵\t\t\t🌋\n'
    ]

success = '\n\n\t\t\t ➖➖➖➖➖➖\t🌞\n\t\t\t 🪵        🪝\n\t\t\t 🪵\n\t\t\t 🪵\n\t\t\t 🪵\n\t\t\t 🪵\n\t\t\t 🪵\t\t\t🤸🏽‍♂️\n\t\t\t 🪵\t\t\t⛰️\n'
base = '🌱🌱🌱🌱🌻🌱🌱🌱🌱☘️🌱🌱🪵🌱🌱🌷🌱🌱🌱🌱🍄🌱🌱🌱🌱🍀🌱🌱🌱🌱\n🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨🪨'

# print(hanged[0] + base)
# print(hanged[1] + base)
# print(hanged[2] + base)
# print(hanged[3] + base)
# print(hanged[4] + base)
# print(hanged[5] + base)
# print(hanged[6] + base)
# print(won + base)

"""#### Colors"""

Black = "\033[0;30;47m"
Red = "\033[0;31;47m"
Green = "\033[0;32;47m"
Brown = "\033[0;33;47m"
Blue = "\033[0;34;47m"
Magenta = "\033[0;35;47m"
Cyan = "\033[0;36;47m"
LightGrey = "\033[0;37;40m"
BOLD = "\033[1m"
RESET = "\033[0m"

"""## Game!

### Word or Phrase Generation
"""

# To check if the generated secret contains only letters
def checkValidity(generated):
  valid = True

  for character in generated:
    if (character.isalpha() == False) and (character != ' '):
      valid = False

  return valid

# Generate word or phrase
def generate(mode='word', generated='*'):

  valid = checkValidity(generated)
  possibilities = ['word', 'w', 'phrase', 'p']

  while mode not in possibilities:
    mode = input(f'Only words ("word" or "w") or phrases ("phrase" or "p") can be generated. Please select one of those! ').lower()

  r = RandomWord()

  while valid == False:
    # Generate word or phrase
    if mode == 'word' or mode ==  'w':
      generated = r.word()
    elif mode == 'phrase' or mode == 'p':
      word1 = r.word(include_parts_of_speech=["adjectives"])
      word2 = r.word(include_parts_of_speech=["nouns"])
      generated = word1 + ' ' + word2
    valid = checkValidity(generated)

  return generated

"""#### Word Hidding"""

# Hide the secret
def hide(secret='example', veil='_'):
  hidden = ''
  for letter in secret:
    if letter == ' ':
      hidden += letter
    else:
      hidden += veil

  return hidden

# Make the secret clearer
def clearHide(hidden='example', veil='_'):
  clearHidden = ''
  length = len(hidden)

  for character in hidden:
    if character != ' ':
      clearHidden += character
    else:
      clearHidden += '+  +'
    length -= 1

    if length == 0:
      return clearHidden
    else:
      clearHidden += ' '

"""### Input Check

#### Input Validation
"""

# Check if input is valid
def inputValidation(guess='-', guesses=[], test=False):

  validity = [False,'',guesses,guess]

  # Ask for input
  print(f'{Cyan}\nPick a letter!{RESET}\n{Green}Or enter {BOLD}{Red}"?"{RESET}{Green} for a hint (it costs 1 life!).\n')
  if guesses != []:
    print(f'\nGuesses made so far: {Green}{guesses}{RESET}')
  guess = input().lower()
  validity[3] = guess

  if guess == '?':
    validity = ['hint', f'{Green}🧩 You asked for a hint! 🪧{RESET}', guesses, guess]

  # Enter pressed without input
  elif guess == '':
    print(f'{Magenta}Upsi! No input!{RESET}')
    return validity

  # Not a letter
  elif (len(guess) == 1) and (guess.isalpha() == False):
    print(f'{Red}{guess} is not a letter{RESET}. Please try with a letter!')
    return validity

  # More than 1 character
  elif (len(guess) != 1) and (guess not in guesses):
    validity[0] = False
    validity[1] = input(f'"{guess}" is not a single character. Are you trying to unveil the whole mistery? Y/n: ').lower()

    # Check if player is trying to guess the whole secret at once
    while ((validity[1] != 'y') and (validity[1] != '')) and (validity[1] != 'n'):
      validity[1] = input('Only "Y" or "N" accepted!  Are you trying to unveil the whole mistery? Y/n: ').lower()
    if (validity[1] =='y') or (validity[1] ==''):
      validity[0] = 'whole'
      validity[1] = "Very brave of you!"
      guesses.append(guess)
    else:
      print(f'{Green}OK! Then try again!{RESET}')
      return validity

  # Value not tried
  elif guess not in guesses:
    validity[0] = 'new'
    validity[1] = 'Nice try!'
    guesses.append(guess)

  # Value already tried
  elif guess in guesses:
    validity[0] = 'tried'
    validity[1] = 'You already tried that!'

  # Error
  else:
    validity[0] = False
    validity[1] = 'Logical error! Try again.'

  validity[2] = guesses

  # Clean the console
  if (test == False) and (guess != '?'):
    clear_output()
    os.system('clear')
    print(f'\t{Blue}⏳️ Thinking ⏱️\n------------------------------{RESET}\n\n')
    sleep(2)
  else:
    print(f'{Red}CLEANING CONSOLE\n\t{Blue}⏳️ Thinking ⏱️\n--{RESET}\n\n')

  return validity

"""#### Get a hint"""

def getHint(secret, hidden, test=False):
  secrets = []

  # Look for unveiled letters
  for i in range(len(secret)):
    if (secret[i] != hidden[i]) and (secret[i] != ' '):
      secrets.append(secret[i])

  # Select a letter to unveil
  hint = random.choice(secrets)
  if test == True:
    print(f'Secrets: {secrets}')

  return hint

"""#### Sucess Checking"""

def unvail(secret, guess, hidden, test=False):
  hits = 0
  settled = ''
  hint = False

  # Get a hint
  if guess == '?':
    hint = True
    guess = getHint(secret, hidden, test=test)
    # Clean the console
    if test == False:
      clear_output()
      os.system('clear')
      print(f'{Green}🧩 You asked for a hint! 🪧\n\n\t{Blue}⏳️ Generating Hint ⏱️\n-------------------------------------{RESET}\n\n')
      sleep(2)
    else:
      print(f'{Red}CLEANING CONSOLE\n{Green}🧩 You asked for a hint! 🪧\n\n\t{Blue}⏳️ Generating Hint ⏱️\n--{RESET}\n\n')

  # Unvail hidden letters
  for i in range(len(secret)):
    if guess == secret[i]:
      settled += guess
      if hint == False:
        hits += 1
    else:
      settled += hidden[i]
  hidden = settled

  unvailed = [hidden, hits]

  return unvailed

"""### Hangman"""

def hangman(mode='word', veil='_', chances=6, test=False):
  # Variables declaration
  secret=generate(mode)
  guess = ''
  fails = 0
  hidden = hide(secret)
  left = chances
  guesses = []
  validationMessage = ''

  while fails < chances:
    # for test
    if test == True:
      print(f'Answer: {secret}\n')

    # Declare internal variables
    hits = 0
    clearHidden = clearHide(hidden)
    validInput = False

    # Inform about present standpoint
    print(f"The secret is: \t{Magenta}{clearHidden}{RESET}")
    print(f'\nNumber of mistakes left: {Red}{left}{RESET}')
    print(hanged[fails] + base + "\n\n")

    # Check validity of input
    while validInput == False:
      validInput, validationMessage, guesses, guess = inputValidation(guess='-', guesses=guesses, test=test)
    print(f'{Green}{validationMessage}{RESET}')

    # Check for success
    if (guess == '?') and (left == 1):
        print(f'{Red}🧐 But you don\'t have enough lives to go for a hint! 🤨{RESET}')
        continue
    hidden, hits = unvail(secret=secret, guess=guess, hidden=hidden, test=test)
    # New success
    if (hits != 0) and (validInput == 'new'):
      GUESS = guess.upper()
      if hits == 1:
        print(f'{Cyan}🔮 Correct! 🎯\n\nThe letter "{GUESS}" is contained in the secret!{RESET}\n')
      else:
        print(f'{Cyan}🔮 Correct! 🎯\n\nThe letter "{GUESS}" is contained {hits} times in the secret!{RESET}\n')
    # input already tried
    elif validInput == 'tried':
      continue

    # Whole word comparison
    elif (validInput == 'whole') and (guess == secret):
      hidden = secret
    # Fail
    else:
      fails += 1
      left = chances - fails
      if validInput == 'new':
        print(f'{Red}{BOLD}🙅🏽‍♂️ BUT WRONG! 🤡{RESET}')
      else:
        continue

    # WON!
    if veil not in hidden:
      won = True
      print(f'\n{Green}{BOLD}🎆🎊🎉 YOU WON! 🎉🎊🎆{RESET}')
      print(success + base)
      return won

    # for test
    if test == True:
      print('\nhits: ', hits)
      print('valid input: ', validInput)
      print('guess in guesses: ', guess in guesses)

  # Lost =(
  if veil in hidden:
    won = False
    # Show result
    print(hanged[-1] + base + "\n\n")
    print(f'\t\t\t{Red}{BOLD}🪦⚰️💀 You lost! 💀⚰️🪦{RESET}')

  # Reveal secret
  print(f'\nThe secret was "{Cyan}{secret.upper()}{RESET}"')
  return won

"""### Rematch"""

# Print scores
def printScores(scores={}):
  print(f'\n\n{Green}Leaderboard:{RESET}\n')
  for player, score in scores.items():
    print(f'{Cyan}{player}: {score}{RESET}')

# Loop to start and restart
def play(mode='word', veil='_', chances=6, test=False):
  start = 'y'
  scores = {}

  # Loop to start again
  while start == 'y':

    # Player definition
    if test == True:
      player = ''
    else:
      player = input('How would you like to be named? ')
    clear_output()
    os.system('clear')
    if player != '':
      print(f'{Green}🏟️ Hello, {player}! We are setting the game for you 🕹️\n----------------------------------------------------------------------------\n\n{RESET}')
    else:
      print(f'\t{Green}🏟️ We are setting the game for you 🕹️\n------------------------------------------------------\n\n{RESET}')
    sleep(2)

    # Start game
    won = hangman(mode=mode,veil=veil,chances=chances,test=test)
    if player != '':
      scores[player] = won + scores.get(player, 0)
      # Show scores
      printScores(scores)

    # Restart game
    start = input('\n\nDo you want to play again? Y/n: ').lower()
    if start == '':
      start = 'y'
    while ((start != 'y') and (start != '')) and (start != 'n'):
      start = input('Only "Y" or "N" accepted! Do you want to play again? Y/n: ').lower()
      if start == '':
        start = 'y'

    # End game
    if start == 'n':
      if test == False:
        clear_output()
        os.system('clear')
      else:
        print(f'{Red}CLEANING CONSOLE')
      print(f'{Red}{BOLD}¡BORING!{RESET} But as you wish.\n\tBye!')
      if scores != {}:
        printScores(scores)

"""### For Tests"""

# play(test=True, chances=3)
# play('p',test=True)
# play('v')

"""# Description

Hangman is a guessing game for one or more players. One player (or the computer) thinks of a word, phrase, or sentence and the player(s) tries to guess it by suggesting letters or numbers within a certain number of guesses. Originally a paper-and-pencil game, there are now electronic versions like this one.

If you want to know more about the game, follow [this](https://en.wikipedia.org/wiki/Hangman_(game)) link for a full article!

## Arguments:

- mode: 'word' or 'phrase'
- veil: Default -> '_'
- chances: Default -> 6
- test: Default -> False
- **If you want a hint, you can also input "?"**

**For example:**

`play(mode='phrase',veil='*',chances='3',test=True)`

# Play!
"""

play()