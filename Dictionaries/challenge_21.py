import random

print('\n Welcome to the thesaurus app')
thesaurus = {
    "hot":['balmy', 'summery', 'tropical', 'boiling', 'scorching'],
    "cold":['chilly', 'cool', 'freezing', 'frigid', 'polar'],
    "happy":['content', 'cheery', 'merry', 'jovial', 'jocular'],
    "sad":['unhappy', 'downcast', 'miserable', 'glum', 'melancholy'],
}

print('\n Here are the words in the thesaurus:')
for key in thesaurus:
    print(f'\n {key}')
word = input('\n Pick a word you want synonym for : ').lower()
random_no = random.randint(0,4)
if word in thesaurus:
    print(f'\n Synonym  for {word} is {thesaurus[word][random_no]}')
    response = input('\n Would you like to see complete thesaurus ? (y/n) ').lower().strip()
    if response == 'y':
        for key, values in thesaurus.items():
            print(f'\n Word {key} is synonym to : ')
            for value in values:
                print(f'\n - {value}')
    else:
        print('\n Goodbye! Have a nice day.')    
else:
    print(f'\n {word} doesn\'t exist!') 