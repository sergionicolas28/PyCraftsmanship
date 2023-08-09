import random

options = ('piedra', 'papel', 'tijera')

computer_wins = 0
user_wins = 0
rounds = 1

while True:
  
  print('*' * 10)
  print('ROUND', rounds)
  print('*' * 10)
  
  user_option = input("¿piedra, papel o tijera? Escoja una => ")
  user_option = user_option.lower()
  
  if not (user_option in options):
    print('Esa opción no es válida')
  
  computer_option = random.choice(options)
  
  print('User option =>', user_option)
  print('Computer option =>', computer_option)
  
  if (user_option == computer_option):
    print("Es un empate, la computadora escogió", computer_option)
  elif (user_option == "papel" and computer_option == "piedra"):
    print("Usted ha ganado, la computadora seleccionó", computer_option)
    user_wins += 1
  elif (user_option == "papel" and computer_option == "tijera"):
    print("Usted perdió, la computadora seleccionó", computer_option)
    computer_wins += 1
  elif (user_option == "piedra" and computer_option == "tijera"):
    print("Usted ha ganado, la computadora seleccionó", computer_option)
    user_wins += 1
  elif (user_option == "piedra" and computer_option == "papel"):
    print("Usted perdió, la computadora seleccionó", computer_option)
    computer_wins += 1
  elif (user_option == "tijera" and computer_option == "papel"):
    print("Usted ha ganado, la computadora seleccionó", computer_option)
    user_wins += 1
  elif (user_option == "tijera" and computer_option == "piedra"):
    print("Usted perdió, la computadora seleccionó", computer_option)
    computer_wins += 1

  rounds += 1
  if (user_wins == 3):
    print('Usted ha ganado el juego, el resultado es', user_wins, 'victorias del usuario y', computer_wins, 'victorias de la computadora')
    break
  elif (computer_wins == 3):
    print('Usted ha perdido el juego, el resultado es', computer_wins, 'victorias de la computadora y', user_wins, 'victorias del usuario')
    break
