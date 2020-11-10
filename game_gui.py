import PySimpleGUI as sg
import string

def updateLabel(window, key, value):
    window[key].update(value)


alphabet = string.ascii_lowercase

main_background_color = '#aa4444'

alphabet_button = [[sg.B(alphabet[n],  font=('arial', 11, 'bold'), size=(3, 1), key=alphabet[n]) for n in range(0, 13)],
                   [sg.B(alphabet[n],  font=('arial', 11, 'bold'), size=(3, 1), key=alphabet[n]) for n in range(13, 26)]]

level_and_stage_frame = [[sg.T('Level ', font=('arial', 11, 'bold'), background_color=main_background_color), sg.T('1', font=('arial', 11, 'bold'), key='level_label', background_color=main_background_color), sg.T('Stage', font=('arial', 11, 'bold'), background_color=main_background_color), sg.T('1', font=('arial', 11, 'bold'), key='stage_label', background_color=main_background_color), sg.T('           ', background_color=main_background_color)]]
highscore_and_score_frame = [[sg.T('Highscore ', font=('arial', 11, 'bold'), background_color=main_background_color), sg.T('1000000', font=('arial', 11, 'bold'), background_color=main_background_color, key='highscore_label')],
                             [sg.T('Current Score ', font=('arial', 11, 'bold'), background_color=main_background_color), sg.T('25000', font=('arial', 11, 'bold'), background_color=main_background_color, key='currentscore_label')]]

game_word_frame = [[sg.T('word', font=('times new roman', 50, 'bold'), background_color='black', pad= (20, 5), key='game_word')]]

definition_frame = [[sg.T('Here is the container for the definition of the word that is to \nbe guesse and played\nit has dashes that needs to be replaced by letters \nFrom the word.', font=('arial', 8, 'bold'), background_color=main_background_color)]]

letters_frame = alphabet_button
#letters_frame = [[sg.T('the letters button goes here', font=('arial', 11, 'bold'), background_color=main_background_color)]]

main_layout = [[sg.Frame('Position', layout=level_and_stage_frame, background_color=main_background_color), sg.Frame('Scores', layout=highscore_and_score_frame, background_color=main_background_color)],
                [sg.Frame('', layout=game_word_frame, title_location='n', background_color= 'black',border_width= -1, element_justification='center' )],
                [sg.Frame('Definition/guide', layout=definition_frame, background_color=main_background_color, title_location='n')],
                [sg.Frame('Keys', layout=letters_frame, background_color=main_background_color, title_location='n')],
                [sg.B('Stop Game', key='stop', button_color=('white', '#550000'))]]


game_window = sg.Window('Word Guezz Game', layout=main_layout, element_justification= 'center', use_default_focus=False, no_titlebar=False, background_color=main_background_color, alpha_channel=0.9)



while True:
    events, values = game_window.read()
    if events in (None, 'stop'):
        break
    if events != None:
        pass