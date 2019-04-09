vowels = ['a','e','i','o','u']
word = input('Provide a word tp search for vowels: ')
found ={}

#Loop and find the vowels present in word which was given as input
for letter in word:
    if letter in vowels:
        found[letter] =+1

for k,v in sorted(found.items()):
    print(k,v , 'was found', v ,  'times')
print(found)
