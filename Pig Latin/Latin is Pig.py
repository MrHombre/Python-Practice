print('Welcome to the Pig Latin Translator!')

# Created a variable named pyg that has the string "ay" that is added to every word.
pyg = 'ay'

# Asking the user to input a word to be translated.
original = input("Enter a Word:")

# If statement checks the the user entered a string also that this string doesn't contain numbers
if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:]
    print(new_word)
elif not original.isalpha():
    print("The word mustn't contain any numbers.")
else:
    print("Please print a word.")
