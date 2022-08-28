import PySimpleGUI as sg


layout = [
    [
        sg.Input(key="-INPUT-"),
        sg.Spin(["km na mile", "kg na funty", "sec na min"],  key="-UNITS-"),
        sg.Button("Konwertuj", key="-CONVERT-"),
    ],
    [sg.Text("Wynik", key="-OUTPUT-")],
]

window = sg.Window("Conventer", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    if event == "-CONVERT-":
        input_value = values['-INPUT-']
        if input_value.isnumeric():
            match values['-UNITS-']:
                case "km na mile":
                    output = round(float(input_value) * 0.06214, 2)
                    output_str = f"{input_value} km to {output} mili."
                case "kg na funty":
                    output = round(float(input_value) * 2.20462, 2)
                    output_str = f"{input_value} kilogramów to {output} funtów."
                case "sec na min":
                    output = round(float(input_value) / 60, 2)
                    output_str = f"{input_value} sekund to {output} minut."

            window['-OUTPUT-'].update(output_str)
        else:
            window['-OUTPUT-'].update("Proszę pisać liczbę.")


window.close()
