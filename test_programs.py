
import random
import db
import time

word_count = db.getRowCount('four')

word_choice_indices = [random.randint(1, word_count) for i in range(4)]

word, dfn = db.getWordDetails('four', word_choice_indices[0])


dashed = None

display_word = ''

over = False

consecutive_correct = 0

score = 0



stages = 1

levels = {1: 'four', 2: 'five', 3: 'six',
          4: 'seven', 5: 'eight', 6: 'nine', 7: 'ten'}
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


def cleanComma(word):
    return word.replace(' ', '')


def wordToDisplay(word):
    return word.replace(',', '_')


def replaceLetter(word, letter, position, dashed=''):
    if not dashed:
        lst_word = ['_' for i in range(len(word))]
    else:
        lst_word = dashed.split(' ')
    for i in position:
        lst_word[i] = letter
    return ' '.join(lst_word)

over = False
starting = True

while not over:
    for letter in word:
        if starting:
            print(' _ ' * len(word))
            print(dfn)
            starting = False
            continue
        #letter = input('Guess>> ')
        positions = findPositions(word, letter)
        if not positions:
            print('Invalid Choice')
            print(dfn)
            print(dashed)
            continue
        dashed = replaceLetter(word, letter, positions, dashed=dashed)

        print(dashed)
        print(dfn)
        display_word = cleanComma(dashed)
        consecutive_correct += 1
        score += 10 * consecutive_correct
        print(f'\n Score is {score} \n')
        if display_word == word:
            stages += 1
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

            word, dfn = db.getWordDetails(
                levels[current_level], word_choice_indices[stages - 1])
            print('Starting stage', stages, '...')
            print(word, dfn)
            print('------------------------------------------------------------------------')
            print()
            dashed = ''
            starting = True


print(display_word)
