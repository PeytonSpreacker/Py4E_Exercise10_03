#Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency. Your program should convert all the input to lower case and only count the letters a-z. Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.

letters = dict()
total = 0

#open text file to analyze
while True:
    try:
        fhandle = open(input('Enter file name:'))
        break
    except:
        print('File does not exist.')
        continue

#make the file lowercase
lines = [line.lower() for line in fhandle]

#parse file by lines and split into individual words/characters
for line in lines :
    line.strip()
    line.split()
    for words in line :
        for char in words :
            if char.isalpha():
                letters[char] = letters.get(char, 0) + 1
                total = total + 1
#print frequency of letters in the given text file key sorted
for key, val in sorted(letters.items()):
    print('Key Sorted:', key, ': ', round(val/total*100, 2), '%')