# import random
# opciones = ["Rock","Paper","Scissors","Lizard","Spock"]
# puntaje_jugador = 0
# puntaje_pc = 0
# print(("Rock,Paper,Scissors,Lizard,Spock!!!"))
# print("Rules :- Scissors cuts Paper\n- Paper covers Rock\n"
#       "- Rock crushes Lizard\n- Lizard poisons Spock\n"
#       "- Spock smashes Scissors\n- Scissors decapitates Lizard\n"
#       "- Lizard eats Paper\n- Paper disproves Spock\n- Spock vaporizes Rock\n"
#       "- Rock crushes Scissors")
# print("\nEl primero en optener 3 puntos es el ganador, PC vs Jugador")
# while True:
#     selecion_pc = random.choice(opciones).lower()
#     selecion_jugador = input(f"\nRock,Paper,Scissors,Lizard,Spock\nJugador: ").lower()
#     if (selecion_jugador == selecion_pc):
#         print(f"Empate\nPC: {selecion_pc}")
#     elif (selecion_jugador == "scissors" and selecion_pc == "paper") or\
#             (selecion_jugador == "paper" and selecion_pc == "rock") or\
#             (selecion_jugador == "rock" and selecion_pc == "lizard") or\
#             (selecion_jugador == "lizard" and selecion_pc == "spock") or\
#             (selecion_jugador == "spock" and selecion_pc == "scissors") or\
#             (selecion_jugador == "scissors" and selecion_pc == "lizard") or\
#             (selecion_jugador == "rock" and selecion_pc == "scissors") or\
#             (selecion_jugador == "lizard" and selecion_pc == "paper") or\
#             (selecion_jugador == "paper" and selecion_pc == "spock") or\
#             (selecion_jugador == "spock" and selecion_pc == "rock") or\
#             (selecion_jugador == "rock" and selecion_pc == "scissors"):
#         print(f"PC: {selecion_pc}")
#         print("Punto a favor del Jugador")
#         puntaje_jugador += 1
#         print(f"PC = {puntaje_pc}, Jugador = {puntaje_jugador}")
#     else:
#         print(f"PC: {selecion_pc}")
#         print("Punto a favor de la PC")
#         puntaje_pc += 1
#         print(f"PC = {puntaje_pc}, Jugador = {puntaje_jugador}")
#     if puntaje_jugador == 3:
#         print(f"Ganaste!!,Obtuviste {puntaje_jugador} puntos")
#         break
#     elif puntaje_pc == 3:
#         print(f"Perdiste!!,La PC obtivo {puntaje_pc} puntos")
#         break

#si una palabra es un palíndromo
palabra_lista = []
palabra_lista_reverse = []
palabra = input("Ingrese una palabra: ").lower()
for i in palabra:
    palabra_lista.append(i)
    palabra_lista_reverse.append(i)
palabra_lista_reverse.reverse()
if palabra_lista == palabra_lista_reverse:
    print(f"La palabra {palabra} es un palíndromo  ")
else:
    print(f"La palabra {palabra} no es un palíndromo ")
print(palabra_lista)
print(palabra_lista_reverse)

# palabra = input("Ingrese una palabra: ").lower()
# if palabra == palabra[::-1]:
#     print(f"La palabra '{palabra}' es un palíndromo.")
# else:
#     print(f"La palabra '{palabra}' no es un palíndromo.")



