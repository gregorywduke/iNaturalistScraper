import urllib.request
import PySimpleGUI as sg

sg.theme('DarkAmber')

# GUI layout
layout = [[sg.Text("Select iNaturalist export (.csv)")],
          [sg.FileBrowse("Select File", key="csv"), sg.Text("",key="fb" )],
          [sg.Text("Select folder to store downloaded files")],
          [sg.FolderBrowse("Select Folder", key="dir"), sg.Text("",key="folb" )],
          [sg.Button("Start Download"), sg.Text("Idle...", key="out")]]

window = sg.Window("iNaturalistScraper", layout)

# Event Loop
while True:
    event, values = window.read()
    # If USER exits window
    if event == sg.WIN_CLOSED:
        break
    if event == "Select File":
        # Updates value to display file selected by user
        window["fb"].update(values["csv"])
    if event == "Select Folder":
        # Updates value to display folder selected by user
        window["folb"].update(values["dir"])
    if event == "Start Download":
        source = values["csv"]
        dir = values["dir"]
        window["out"].update("Downloading...")

        # Open .CSV file
        file = open(source)
        count = 0

        # Read and download each URL in .CSV
        for x in file:
            count+=1
            fname = dir + "/" + str(count) + ".jpg"
            urllib.request.urlretrieve(x, fname)

        window["out"].update("Downloaded.")
        file.close()

