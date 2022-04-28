from wordfile import words
from hangman_pics import pics
import random

chances=5
correctGuess=0

print("************************************************************")
print("Welcome to Hangman Game!!")
print("You have 5 chances to guess the correct word!!")
print("************************************************************")

wordToGuess=random.choice(words)
print(wordToGuess)

wordLength=len(wordToGuess)

uniqueWord="".join(set(wordToGuess))
print(uniqueWord)

uniqueLength=len(uniqueWord)

display="-" * wordLength
print(display)
guess1 =""

print("You have "+str(wordLength)+" long letter to guess!!")
print("************************************************************")
while chances>0 and correctGuess!=uniqueLength:
    guess=input("Enter your guess character: ")
    pword = wordToGuess[:]
    if guess in wordToGuess and guess not in guess1:
        correctGuess=correctGuess+1
        
        p=0
        s=0
        while guess in pword:
            index=pword.index(guess)
            p=p+index+s
            display=display[:p]+guess+display[p+1:]
            s=1
            pword = pword[index+1:]
        print(display)
        print("Awesome!!You have "+str(chances)+" chances left!!")
        print("************************************************************")
        
    elif guess in guess1:
        print("You have already guessed this letter. You still have " +str(chances)+" chances left!!")
        print("************************************************************")
    else:
        chances=chances-1
        print(pics[5-chances])
        print("Oh no!!You have "+str(chances)+" chances left!!")
        print("************************************************************")
    guess1 =guess1+ guess

if correctGuess==uniqueLength:
    print("Congratulations!!You win!!")
    print("The word was "+wordToGuess+".")
else:
    print("Sorry!!You lost!!")
    print("The word was "+wordToGuess+".")

