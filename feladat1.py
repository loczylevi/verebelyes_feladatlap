szo = input("írjon be legfeljeggy egy 11 karakterből álló szöveget: ")


if len(szo) < 12:
  szo = szo.upper()
  szo = szo[::-1]
  print(szo)
else:
  print(f"a(z) {szo} több mint 11 karakter hosszú!")

