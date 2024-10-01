import PySimpleGUI as sg
sg.theme("DarkBlue4")

layout = [[sg.T("テキスト")],
          [sg.I("入力欄")],
          [sg.ML("複数行テキスト 1行目\n2行", size=(30,3))],
          [sg.Im("./python_2nensei_appli_sample/02app/futaba.png")]]                   
window = sg.Window("入力欄テスト",layout,
                   font=(None,14),size=(500,240))

e,v = window.read()
window.close()