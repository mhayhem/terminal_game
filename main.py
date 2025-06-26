import random
import time

def number_of_players():
    print("Elige jugar solo o contra alguien:")
    print("1. Singleplayer")
    print("2. Multiplayer")
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

        