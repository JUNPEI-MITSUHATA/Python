import PySimpleGUI as sg
sg.theme("DarkBlue4")

layout = [[sg.I("フタバ", k="in"),sg.T("1行2列目")],
          [sg.B("実行", k="btn"),sg.T("2行2列目")],
          [sg.T(k="txt"),sg.T("3行2列目")]]
window = sg.Window("あいさつテスト",layout,
                   font=(None,14),size=(500,240))

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