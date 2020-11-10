import sys
import PySimpleGUI as sg
import string
import random
import db

word_count = db.getRowCount('four')

word_choice_indices = [random.randint(1, word_count) for i in range(4)]

word, dfn = db.getWordDetails('four', word_choice_indices[0])

dashed = ' _ ' * len(word)

display_word = ''

over = False

stages = 1

consecutive_correct = 0

score = 0

selected_letters = []

levels = {1: 'four', 2: 'five', 3: 'six',
          4: 'seven', 5: 'eight', 6: 'nine', 7: 'ten'}

current_level = 1


retry = 40

highscore = db.getHighscore()
print(highscore)

player_id = 0

after_stage_retry_increase = 10

after_level_retry_increase = 20


def formattedHighscoreList():
    h_list_unformatted = db.getTopTen()
    h_list_formatted = ''
    for i in h_list_unformatted:
        h_list_formatted += i[0] + '  +++++++>>  ' + str(i[1]) + '\n'
    return h_list_formatted


player_name = sg.popup_get_text('Enter your player name', no_titlebar= True, background_color= 'green', font=('arial', 12, 'bold'))
if player_name == None:
    sys.exit()
player_id = db.getPlayerId(player_name)


if not player_id:
    db.addPlayer(player_name)
    player_id = db.getPlayerId(player_name)

db.createScore(player_id, score)



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


def updateLabel(window, key, value):
    window[key].update(value)


alphabet = string.ascii_lowercase

main_background_color = '#aa4444'

alphabet_button = [[sg.B(alphabet[n],  font=('arial', 11, 'bold'), size=(3, 1), key=alphabet[n]) for n in range(0, 13)],
                   [sg.B(alphabet[n],  font=('arial', 11, 'bold'), size=(3, 1), key=alphabet[n]) for n in range(13, 26)]]

level_and_stage_frame = [[sg.T('Level ', font=('arial', 11, 'bold'), background_color=main_background_color), sg.T('1', font=('arial', 11, 'bold'), key='level_label', background_color=main_background_color), sg.T('Stage', font=(
    'arial', 11, 'bold'), background_color=main_background_color), sg.T('1', font=('arial', 11, 'bold'), key='stage_label', background_color=main_background_color)]]
retry_frame = [[sg.T(retry, font=('arial', 11, 'bold'), key='retry_label', size=(5,1), background_color=main_background_color)]]
highscore_and_score_frame = [[sg.T('Highscore ', size=(15, 1), font=('arial', 11, 'bold'), background_color=main_background_color), sg.T(highscore, size=(10, 1), font=('arial', 11, 'bold'), background_color=main_background_color, key='highscore_label')],
                             [sg.T('Current Score ', size=(15, 1), font=('arial', 11, 'bold'), background_color=main_background_color), sg.T('0', size=(10, 1), font=('arial', 11, 'bold'), background_color=main_background_color, key='currentscore_label')]]

game_word_frame = [[sg.T(dashed, font=('times new roman', 30, 'bold'),
                         background_color='black', pad=(20, 5), key='game_word', size=(20,1))]]

definition_frame = [[sg.T(dfn, font=(
    'arial', 8, 'bold'), background_color=main_background_color, key="definition", size=(70, 10))]]

letters_frame = alphabet_button
#letters_frame = [[sg.T('the letters button goes here', font=('arial', 11, 'bold'), background_color=main_background_color)]]

main_layout = [[sg.T('Player ', font=('arial', 11, 'bold'), background_color=main_background_color), sg.T(player_name, font=('arial', 11, 'bold'), background_color=main_background_color, key='player_name')],
               [sg.Frame('Position', layout=level_and_stage_frame, title_location='n', background_color=main_background_color), sg.Frame('Guess Left', layout=retry_frame, background_color=main_background_color, title_location='n', element_justification='center'), sg.Frame('Scores', layout=highscore_and_score_frame, title_location='n', background_color=main_background_color, )],
               [sg.Frame('', layout=game_word_frame, title_location='n',
                         background_color='black', border_width=-1)],
               [sg.Frame('Definition/guide', layout=definition_frame,
                         background_color=main_background_color, title_location='n', element_justification='left')],
               [sg.Frame('Keys', layout=letters_frame,
                         background_color=main_background_color, title_location='n')],
               [sg.B('Top 10 Players', key='top10', button_color=('white', '#005500')), sg.B('Stop Game', key='stop', button_color=('white', '#550000'))]]


game_window = sg.Window('Word Guezz Game', layout=main_layout, element_justification='center',
                        use_default_focus=False, no_titlebar=False, background_color=main_background_color, alpha_channel=0.9, text_justification='center')

print(word)
player_name = ''
set_name = True


while True:
    events, values = game_window.read()
    if starting:
        print(player_id, score)
        updateLabel(game_window, 'highscore_label', highscore)
        print(' _ ' * len(word))
        updateLabel(game_window, 'game_word', dashed)
        updateLabel(game_window, 'definition', dfn)
        print(dfn)
        print('Starting Column')
        starting = False
    if events in (None, 'stop'):
        break
    if events == 'top10':
        sg.popup_no_buttons(formattedHighscoreList(), auto_close=True, auto_close_duration=2, background_color='#116611',
                            text_color='white', font=('arial', 14, 'bold'), no_titlebar=True,)
    if events in alphabet:
        letter = events
        positions = findPositions(word, letter)
        if not positions:
            print('Invalid Choice')
            sg.popup_no_buttons('INVALID CHOICE', auto_close=True, auto_close_duration=1, background_color='red',
                                text_color='white', font=('arial', 14, 'bold'), no_titlebar=True)
            consecutive_correct = 0
            retry -= 1
            updateLabel(game_window, 'retry_label', retry)
            continue
        if letter not in selected_letters:
            selected_letters.append(letter)
            consecutive_correct += 1
            score += 150 * consecutive_correct
            if score > highscore:
                highscore = score
                updateLabel(game_window, 'highscore_label', highscore)
            db.updateScore(score)
        print(f'\n Score is {score} \n')
        updateLabel(game_window, 'currentscore_label', score)
        dashed = replaceLetter(word, letter, positions, dashed=dashed)
        updateLabel(game_window, 'game_word', dashed)
        print(dashed)
        print(dfn)
        display_word = cleanSpace(dashed)
        if display_word == word:
            stages += 1
            selected_letters = []
            retry += after_stage_retry_increase
            updateLabel(game_window, 'retry_label', retry)
            if stages > len(word_choice_indices):
                current_level += 1
                retry += after_level_retry_increase
                updateLabel(game_window, 'retry_label', retry)
                updateLabel(game_window, 'level_label', current_level)
                if current_level > len(levels):
                    print("""       CONGRATULATIONS  YOU  WIN!!!!        """)
                    over = True
                    break
                stages = 1
                print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
                print('LEVEL ', current_level)
                print('+++++++++++++++++++++++++++++++++++++++++++++++++++')
            sg.popup_no_buttons(f'\t{word.upper()}\n-----------------------------------------\nNext ==>  Level {current_level} Stage {stages} ', auto_close=True, auto_close_duration=2, background_color='#116611',
                                text_color='white', font=('arial', 14, 'bold'), no_titlebar=True,)
            updateLabel(game_window, 'stage_label', stages)
            word, dfn = db.getWordDetails(
                levels[current_level], word_choice_indices[stages - 1])
            print(word,dfn)
            dashed = ' _ ' * len(word)
            updateLabel(game_window, 'game_word', dashed)
            updateLabel(game_window, 'definition', dfn)
            print('Starting stage', stages, '...')
            print('------------------------------------------------------------------------')
            print()
            starting = True

