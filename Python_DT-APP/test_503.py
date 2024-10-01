from pathlib import Path
import chardet

def savetext(filename):
    with open(filename, "rb") as f:
        p = Path(filename)
        txt = "書き出しテストの用データです。"
        print(f"{filename}:{txt}")
        p.write_text(txt, encoding="UTF-8") 
savetext("./python_2nensei_appli_sample/05file/output.txt")