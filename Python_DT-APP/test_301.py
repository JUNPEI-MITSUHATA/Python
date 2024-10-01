a = "富士山"
b = "3776"
txt = f"{a}の高さは{b}mです"
print(txt) 

c = 1
d = 2
print(f"c = {c} d = {d}")
print(f"{c}+{d}={c+d}")

e = 12
f = 1234567
print(f"桁区切り:e={e:,} f={f:,} ")
print(f"5桁未満は0埋め:e={e:05} f={f:05}")

g = 123.4
h = 123.456789
print(f"小数点以下3桁:g={g:.3f} h={h:.3f}")
print(f"小数点以下5桁:g={g:.5f} h={h:.5f}")

a = 123
b = 255
c = 65535
print(f"2進数:a={a:#b} b={b:#b} c={c:#b}")
print(f"2進数:a={a:#x} b={b:#x} c={c:#x}")

in1 = 1000
in2 = 4
txt = f"{in1/in2:.2f}円です。"
print(txt)

