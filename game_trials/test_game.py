

word = 'beauty'

dashed = None

display_word = ''

over = False

stages = []

level = []

def findPositions(word,letter):
    if letter not in word:
        return False
    else:
        pos = []
        for i in range(0,len(word)):
            if word[i] == letter:
                pos.append(i)
    return pos

def cleanComma(word):
    return word.replace(' ', '')

def wordToDisplay(word):
    return word.replace(',', '_')



def replaceLetter(word, letter,position, dashed = ''):
    if not dashed:
        lst_word = ['_' for i in range(len(word))]  
    else:
        lst_word = dashed.split(' ')
    for i in position:
        lst_word[i] = letter
    return ' '.join(lst_word)

    

while not over:
    letter = input('Guess>> ')
    positions = findPositions(word, letter)
    if not positions:
        print('Invalid Choice')
        print(dashed)
        continue
    dashed = replaceLetter(word, letter, positions, dashed=dashed )
    print(dashed)
    display_word = cleanComma(dashed)
    if display_word == word:
        over = True


print(display_word)
