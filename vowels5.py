vowels = ['a','e','i','o','u']
#Take the word given by the user to search for vowels
word = input('Provide a word tp search for vowels: ')
found ={}

#Loop and find the vowels present in word which was given as input
for letter in word:
    if letter in vowels:
        found[letter] =+1

for k,v in sorted(found.items()):
    print(k,v , 'was found', v ,  'times')
print(found)
