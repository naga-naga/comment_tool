import PySimpleGUI as sg

screen_size = sg.Window.get_screen_size()

graph_elem = sg.Graph(canvas_size=screen_size, graph_bottom_left=(0, screen_size[1]), graph_top_right=(screen_size[0], 0), key="-GRAPH-", background_color="green")
layout1 = [[graph_elem]]
window1 = sg.Window("Flowing Comments", layout1, location=(0, 0), keep_on_top=True, element_padding=(0, 0), margins=(0, 0), no_titlebar=True, finalize=True, transparent_color="green")

layout2 = [
    [sg.Text("コメント"), sg.Input(key="-INPUT-"), sg.Button("Send")],
    [sg.Button("Exit")],
]
window2 = sg.Window("controller", layout2, keep_on_top=True, grab_anywhere=True, no_titlebar=True, finalize=True)

while True:
    window, event, values = sg.read_all_windows(timeout=0)
    if event in (sg.WINDOW_CLOSED, "Exit"):
        break

window1.close()
window2.close()
