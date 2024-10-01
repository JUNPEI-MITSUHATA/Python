import PySimpleGUI as sg
sg.theme("DarkBlue4")

layout = [[sg.I("フタバ", k="in")],
          [sg.B("実行", k="btn")],
          [sg.T(k="txt")]]
window = sg.Window("あいさつテスト",layout,
                   font=(None,14),size=(250,120))

def execute():
    txt = "こんにちは、"+v["in"]+"さん！"
    window["txt"].update(txt)

while True:
    e,v = window.read()
    if e == "btn":
        execute()
    if e == None:
        break
window.close()