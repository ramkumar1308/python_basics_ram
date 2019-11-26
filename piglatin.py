"""Pig Latin is a language game, where you move the first letter of the word to the end and add "ay."
So "Python" becomes "ythonpay."
To write a Pig Latin translator in Python, here are the steps we'll need to take:

Ask the user to input a word in English.
Make sure the user entered a valid word.
Convert the word from English to Pig Latin.
Display the translation result."""

piglatin = "python"
print(piglatin)


third = "ay"
original = input("Enter the name : ")
if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = piglatin[0]
    new_word = word + first + third
    print(new_word[1:len(new_word)])
else:
    print(' WRONG')


