import PySimpleGUI as sg

#フォルダの表示
""" loadname = sg.popup_get_file("テキストファイルを選択してください。")
print(loadname) """

#ファイルの保存(GUIのみ・処理無し)
savename = sg.popup_get_file("名前をつけて保存してください。",
           default_path = "test.txt", save_as = True)
print(savename)