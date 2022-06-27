import PySimpleGUI as sg
import random

TITLE = "Diplomacy Nation Picker"

def get_player_name(player_number):
    prompt = "Player {0} name".format(player_number)
    layout = [[sg.Text(prompt), sg.Push(), sg.InputText(focus=True)], [sg.VPush()], [sg.Push(), sg.Exit(), sg.OK()]]
    window = sg.Window(TITLE, layout, size=(300,100))
    values = manage_window(window)
    return values[0]

def get_player_names(player_count):
    names = []
    for player_number in range(1, player_count + 1):
        names.append(get_player_name(player_number))
    return random.shuffle(names)

def get_player_count():
    prompt = "Number of players"
    options = ["1", "2", "3", "4", "5", "6", "7"]
    layout = [[sg.Text(prompt), sg.Push(), sg.Combo(options, size=(10, 0), readonly=True)], [sg.VPush()], [sg.Push(), sg.Exit(), sg.OK()]]
    window = sg.Window(TITLE, layout, size=(300,100))    
    values = manage_window(window)
    return int(values[0])

def manage_window(window):   
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            quit()
        if event == 'OK':
            break
    window.close()
    return values

def main():
    while True:
        player_count = get_player_count()
        names = get_player_names(player_count)
        break

if __name__ == "__main__":
    main()