
import random
import db


word_count = db.getRowCount('four')

word_choice_indices = [random.randint(1, word_count) for i in range(4)]

word, dfn = db.getWordDetails('four', word_choice_indices[0])


dashed = None

display_word = ''

over = False

stages = 1

consecutive_correct = 0

score = 0

selected_letters = []

levels = {1:'four', 2:'five', 3:'six', 4:'seven', 5:'eight', 6:'nine', 7:'ten'} 
current_level = 1

def findPositions(word, letter):
    if letter not in word:
        return False
    else:
        pos = []
        for i in range(0, len(word)):
            if word[i] == letter:
                pos.append(i)
    return pos


def cleanSpace(word):
    return word.replace(' ', '')


def wordToDisplay(word):
    return word.replace(',', '_')


def replaceLetter(word, letter, position, dashed=''):
    if not dashed or dashed.count('_') == len(word):
        lst_word = ['_' for i in range(len(word))]
    else:
        lst_word = dashed.split(' ')
    for i in position:
        lst_word[i] = letter
    return ' '.join(lst_word)

starting = True

dashed = ' _ ' * len(word)

while not over:
    if starting:
        print(' _ ' * len(word))
        print(dfn)
        print('Starting Column')
        starting = False
        continue
    letter = input('Guess>> ')
    positions = findPositions(word, letter)
    if not positions:
        print('Invalid Choice')
        if dashed.count('_') == len(word):
            print(' _ ' * len(word))
        else:
            print(dashed)
        print(dfn)
        consecutive_correct = 0
        print('NO POSITION')
        continue
    if letter not in selected_letters:
        selected_letters.append(letter)
        consecutive_correct += 1
        score += 150 * consecutive_correct
    print(f'\n Score is {score} \n')
    dashed = replaceLetter(word, letter, positions, dashed=dashed)
    print(dashed)
    print(dfn)
    display_word = cleanSpace(dashed)
    if display_word == word:
        stages += 1
        selected_letters = []
        if stages > len(word_choice_indices):
            current_level += 1
            if current_level > len(levels):
                print("""       CONGRATULATIONS  YOU  WIN!!!!        """)
                over = True
                break
            stages = 1
            print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
            print('LEVEL ', current_level)
            print('+++++++++++++++++++++++++++++++++++++++++++++++++++')

        word, dfn = db.getWordDetails(levels[current_level], word_choice_indices[stages - 1])
        dashed = ' _ ' * len(word)
        print('Starting stage', stages, '...')
        print('------------------------------------------------------------------------')
        print()
        starting = True


print(display_word)
