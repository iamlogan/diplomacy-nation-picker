import PySimpleGUI as sg

TITLE = "Diplomacy Nation Picker"

def build_results_dict(nations):
    player_names = sorted(nations.keys())
    pattern = "• {0} will play as {1}"
    results = [""] * 7
    for i in range(0, len(player_names)):
        results[i] = pattern.format(player_names[i], nations[player_names[i]])
    return results

def show_results(nations):
    results = build_results_dict(nations)
    desc = "Results"
    layout = [[sg.Text(desc)], [sg.VPush()],
    [sg.Text(results[0])], [sg.Text(results[1])], [sg.Text(results[2])], [sg.Text(results[3])], [sg.Text(results[4])], [sg.Text(results[5])], [sg.Text(results[6])],
    [sg.VPush()], [sg.Push(), sg.Exit()]]
    window = sg.Window(TITLE, layout, size=(300,300))
    values = manage_window(window)
    return values[0]

def get_player_name(player_number):
    prompt = "Player {0} name".format(player_number)
    layout = [[sg.Text(prompt), sg.Push(), sg.InputText(focus=True)], [sg.VPush()], [sg.Push(), sg.Exit(), sg.OK()]]
    window = sg.Window(TITLE, layout, size=(300,100))
    values = manage_window(window)
    return values[0].strip().capitalize()

def get_player_count():
    prompt = "Number of players"
    options = ["2", "3", "4", "5", "6", "7"]
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