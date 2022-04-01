#Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency. Your program should convert all the input to lower case and only count the letters a-z. Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.

letters = dict()
words = list()
char = list()
#open text file to analyze
try:
    fhandle = open(input('Enter file name:'))
except:
    print('File does not exist.')
    quit()
#parse file by lines
for line in fhandle :
    line.lower()
    line.strip()
    words = line.split()
    print(words)
    