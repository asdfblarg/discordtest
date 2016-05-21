# -*- coding: ascii -*-

# import random
# HANGMANPICS = ['''
#
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========''', '''
#
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========''', '''
#
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========''', '''
#
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========''', '''
#
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========''', '''
#
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========''']
# words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()
#
# def getRandomWord(wordList):
#     # This function returns a random string from the passed list of strings.
#     wordIndex = random.randint(0, len(wordList) - 1)
#     return wordList[wordIndex]
#
# def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
#     print(HANGMANPICS[len(missedLetters)])
#     print()
#
#     print('Missed letters:', end=' ')
#     for letter in missedLetters:
#         print(letter, end=' ')
#     print()
#
#     blanks = '_' * len(secretWord)
#
#     for i in range(len(secretWord)): # replace blanks with correctly guessed letters
#         if secretWord[i] in correctLetters:
#             blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
#
#     for letter in blanks: # show the secret word with spaces in between each letter
#         print(letter, end=' ')
#     print()
#
# def getGuess(alreadyGuessed):
#     # Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
#     while True:
#         print('Guess a letter.')
#         guess = input()
#         guess = guess.lower()
#         if len(guess) != 1:
#             print('Please enter a single letter.')
#         elif guess in alreadyGuessed:
#             print('You have already guessed that letter. Choose again.')
#         elif guess not in 'abcdefghijklmnopqrstuvwxyz':
#             print('Please enter a LETTER.')
#         else:
#             return guess
#
# def playAgain():
#     # This function returns True if the player wants to play again, otherwise it returns False.
#     print('Do you want to play again? (yes or no)')
#     return input().lower().startswith('y')
#
# def hangman():
#     print('H A N G M A N')
#     missedLetters = ''
#     correctLetters = ''
#     secretWord = getRandomWord(words)
#     gameIsDone = False
#
#     while True:
#         displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
#
#         # Let the player type in a letter.
#         guess = getGuess(missedLetters + correctLetters)
#
#         if guess in secretWord:
#             correctLetters = correctLetters + guess
#
#             # Check if the player has won
#             foundAllLetters = True
#             for i in range(len(secretWord)):
#                 if secretWord[i] not in correctLetters:
#                     foundAllLetters = False
#                     break
#             if foundAllLetters:
#                 print('Yes! The secret word is "' + secretWord + '"! You have won!')
#                 gameIsDone = True
#         else:
#             missedLetters = missedLetters + guess
#
#             # Check if player has guessed too many times and lost
#             if len(missedLetters) == len(HANGMANPICS) - 1:
#                 displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
#                 print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
#                 gameIsDone = True
#
#         # Ask the player if they want to play again (but only if the game is done).
#         if gameIsDone:
#             if playAgain():
#                 missedLetters = ''
#                 correctLetters = ''
#                 gameIsDone = False
#                 secretWord = getRandomWord(words)
#             else:
#                 # break
#                 return
# # hangman()


# import re
# import requests
# import random
# from bs4 import BeautifulSoup
#
# urls = (
#     "http://danbooru.donmai.us/posts/random/?tags=cat_ears+nude",
#     "http://danbooru.donmai.us/posts/random/?tags=cat_ears+ass",
# )
# def is_tag(tag):
#     tagsearch = requests.get("https://danbooru.donmai.us/posts?tags="+str(tag))
#     tagcontent = tagsearch.content
#     tagsoup = BeautifulSoup(tagcontent, "html.parser")
#     search = tagsoup.find('img')
#     if search == None:
#         return False
#     else:
#         return True
# def check_tagsearch(tag1,tag2):
#     tagsearch = requests.get("https://danbooru.donmai.us/posts?tags="+str(tag1)+"+"+str(tag2))
#     tagcontent = tagsearch.content
#     tagsoup = BeautifulSoup(tagcontent, "html.parser")
#     search = tagsoup.find('img')
#     if search == None:
#         return False
#     else:
#         return True
#
# def default(args):
#     while True:
#         if len(args) == 1:
#             choice = random.choice(urls)
#         elif len(args) == 2:
#             #print(check_tag(args[1]))
#             if is_tag(args[1]) == False:
#                 return("\""+str(args[1])+"\" is not a tag!")
#             choice = "http://danbooru.donmai.us/posts/random/?tags="+str(args[1])
#         elif len(args) == 3:
#             if is_tag(args[1]) == False:
#                 return("\""+str(args[1])+"\" is not a tag!")
#             if is_tag(args[2]) == False:
#                 return("\""+str(args[2])+"\" is not a tag!")
#             if check_tagsearch(args[1],args[2]) == False:
#                 return("No images with both tags found!")
#             choice = "http://danbooru.donmai.us/posts/random/?tags=" + str(args[1]) + "+" + str(args[2])
#         else:
#             return('Too many inputs! No more than 2!\nhttp://puu.sh/otAFk/4ddf396335.jpg')
#         response = requests.get(choice)
#         html = response.content
#         soup = BeautifulSoup(html, "html.parser")
#         imagelink = soup.find(id="image-container")
#         if imagelink:
#             break
#
#     return "<"+str(response.url)+">\nhttp://danbooru.donmai.us"+imagelink.get('data-file-url')
#
# # args = ['!test','tits']
# # args = ['!lewd','1boy', 'nude']
# # print(default(args))

# import sys
# sys.stdout
# sys.stdout.encoding
# string = '''? ( ?? ? ?)?/???/??? ?#'''
#
# print(string.encode("utf-8"))


# string = "strongtestgg</strong>"
# print(string.rstrip('</strong>'))


# import calendar
# from datetime import date
# print(calendar.month(date.today().year,date.today().month))
# # c = calendar.TextCalendar(calendar.SUNDAY)
# # c.prmonth(date.today().year,date.today().month)