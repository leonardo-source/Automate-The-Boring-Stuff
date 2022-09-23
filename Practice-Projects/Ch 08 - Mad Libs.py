#! python3
# mad_libs.py
"""
Create a Mad Libs program that reads in text files and lets users add their own text anywhere
the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.
"""
import re


# Writes the madlib to a new text file
mad_text = open('madlibs.txt', 'r')
mad_libs = mad_text.read()
print(mad_libs)

# Regex for adjective, noun, adverb, and verb
def madLibTale(argumen1):
    patron = re.compile(r'(ADJETIVE|NOUN|VERB|ADVERB)')
    listOfWords = patron.findall(argumen1)

    for i in range(len(listOfWords)):
        patronToSub = re.compile(listOfWords[i])
        print('Enter a(an) %s:' %(listOfWords[i]))
        word = input()
        argumen1 = patronToSub.sub(word, argumen1, 1)
    print(argumen1)
    return(argumen1)

wroteTale = madLibTale(mad_libs)

# Saves the mad_libs to a new text file
new_text = open('new_mad_lib.txt', 'w')
new_text.write(wroteTale)
new_text.close()
mad_text.close()
print(mad_libs)
