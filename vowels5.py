vowels = ['a','e','i','o','u']
word = input('Provide a word tp search for vowels: ')
found ={}

for letter in word:
    if letter in vowels:
        found[letter] =+1

for k,v in sorted(found.items()):
    print(k,v , 'was found', v ,  'times')
print(found)
