# logica de cachipum
import random 

def cachipum(jugador):
    # validar si ingresas datos correcto 
    if jugador == "piedra" and jugador == "papel" and jugador == "tijeras":
        print(f"ingresaste {jugador} ")
        # jugada de computador
        bot = random.choice(["piedra", "papel", "tijeras"])
        print(f"el computador jugo {bot}")

        # todas las opciones para que gane el jugador 
        if ((jugador == "piedra" and bot == "tijera") or (jugador == "papel" and bot == "piedra" ) or (jugador == "tijeras" and bot == "papel")):
            print("el jugador gana")


    else:
        print("solo se permite piedra, papel o tijeras")
