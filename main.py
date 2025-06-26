import random
from time import sleep

def number_of_players():
    print("Elige jugar solo o contra alguien:")
    print("1. Singleplayer")
    print("2. Multiplayer")
    sleep(1)
    while True:
        choice = input()
        if choice in ["1", "2"]:
            return choice
        else:
            continue

def number_of_rounds():
    print("Elige número de rondas")
    print("1. al mejor de 3 ")
    print("2. al mejor de 5")
    game = 0
    sleep(1)
    while True:
        games = input()
        if games in ["1", "2"]:
            if games == "1":
                game = 3
            else:
                game = 5
            return game
        else:
            continue

def create_player(choice):
    print("Creando jugador(s)")
    if choice == "1":
        print("Introduzca su nombre:")
        player = input()
        sleep(1)
        print(f"Jugador creado: {player}")
        return player
    else:
        print("introduzca el nombre de los jugadores:")
        print("Jugador 1:")
        player_1 = input()
        print("Jugador 2:")
        player_2 = input()
        sleep(1)
        print(f"Jugadorescreados: {player_1} vs {player_2}")
        return player_1, player_2