import PySimpleGUI as sg
sg.theme("DarkBlue4")

layout = [[sg.T("ABCDE",size=(30,1), justification="left")],
          [sg.T("ABCDE",size=(30,1), justification="center")],
          [sg.I("ABCDE",size=(30,2), justification="right")]]
window = sg.Window("文字列レイアウト",layout,
                   font=(None,14),size=(500,240))

e,v = window.read()
window.close()