# TicTacToe

tahta = {'7': ' ' , '8': ' ' , '9': ' ' ,
         '4': ' ' , '5': ' ' , '6': ' ' ,
         '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []
for key in tahta:
    board_keys.append(key)

def livegame(tahta):
    print(tahta['7'] + '|' + tahta['8'] + '|' + tahta['9'])
    print('-+-+-')
    print(tahta['4'] + '|' + tahta['5'] + '|' + tahta['6'])
    print('-+-+-')
    print(tahta['1'] + '|' + tahta['2'] + '|' + tahta['3'])

def tictactoe():
  count=0
  
  sira = "X"

  for i in range(10):
    livegame(tahta)
    print(f"{sira} in sirasi.Numpaddeki yerini belirtin.")
    slatt = input()

    if tahta[slatt] == " ":
      tahta[slatt] = sira
      count+=1
    else:
      print("This place is not empty")
      continue
    if tahta['7'] == tahta['8'] == tahta['9'] != ' ':
      print(f"{sira} kazandi")
      break
    elif tahta['4'] == tahta['5'] == tahta['6'] != ' ':
      print(f"{sira} kazandi")
      break
    elif tahta['1'] == tahta['2'] == tahta['3'] != ' ':
      print(f"{sira} kazandi")
      break
    elif tahta['1'] == tahta['4'] == tahta['7'] != ' ':
      print(f"{sira} kazandi")
      break
    elif tahta['2'] == tahta['5'] == tahta['8'] != ' ':
      print(f"{sira} kazandi")
      break
    elif tahta['3'] == tahta['6'] == tahta['9'] != ' ':
      print(f"{sira} kazandi")
      break
    elif tahta['7'] == tahta['5'] == tahta['3'] != ' ':
      print(f"{sira} kazandi")
      break
    elif tahta['1'] == tahta['5'] == tahta['9'] != ' ':
      print(f"{sira} kazandi")
      break
    if sira =="X":
      sira = "O"
    else:
      sira = "X"
  if count >8:
    print("oyun bitti kazanan yok")

          
tictactoe()
