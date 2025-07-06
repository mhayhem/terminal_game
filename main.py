from player_class import Player as P
import random
import getpass # hidden inputs in muliplayer mode
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
        sleep(0.5)
        player_1= P(player, 0)
        player_2 = None
        print(f"Jugador creado: {player_1.name}")
        return player_1, player_2
    elif choice == "2":
        print("introduzca el nombre de los jugadores:")
        print("Jugador 1:")
        player_1 = input()
        player_1 = P(player_1, 0)
        sleep(0.5)
        print("Jugador 2:")
        player_2 = input()
        player_2 = P(player_2, 0)
        sleep(1)
        print(f"Jugadorescreados: {player_1.name} vs {player_2.name}")
        return player_1, player_2
    
def checking_is_multiplayer(player_1, player_2):
    if player_2 is None:
        player_2 = P("Orión", 0)
        single_mode = True
    else:
        single_mode = False
    return single_mode, player_1, player_2

def movents(player_1_move, player_2_move):
    winner = None
    choices = ["piedra", "papel", "tijeras"]
    print(f"{player_1_move} - {player_2_move}")
    if player_1_move == player_2_move:
        print("Empate, no hay ganador en esta ronda")
        return winner
    if player_1_move not in choices or player_2_move not in choices:
        print("Movimiento no válido, por favor elige entre piedra, papel o tijeras")
        return None
    if player_1_move == choices[0] and player_2_move == choices[2] or \
        player_1_move == choices[1] and player_2_move == choices[0] or \
            player_1_move == choices[2] and  player_2_move == choices[1]:
        winner = "player_1"
    else:
        winner = "player_2"
    return winner

def update_winner(player_1, player_2, winner):
    if winner == None:
        return None
    elif winner == "player_1":
        print(f"{player_1.name} gana esta ronda")
        player_1.wins += 1
    else:
        print(f"{player_2.name} gana esta ronda")
        player_2.wins += 1
    
                

def play_round(player_1, player_2, single_mode, game):
    print("Juguemos a piedra, papel o tijeras")
    print(f"{player_1.name} vs {player_2.name}")
    choices = ["piedra", "papel", "tijeras"]
    rounds = 1
    winner = ""
    sleep(1)
    while player_1.wins < game and player_2.wins < game:
        if single_mode:
            
            print(f"Ronda {rounds}")
            print(f"{player_1.name} elige movimiento:")
            player_2_move = random.choice(choices)
            player_1_move = input().lower()
            winner = movents(player_1_move, player_2_move)
            update_winner(player_1, player_2, winner)
            rounds += 1
            
        else:
            print(f"Ronda {rounds}")
            player_1_move = getpass.getpass(f"{player_1.name} elige movimiento: ").lower()
            sleep(0.2)
            player_2_move = getpass.getpass(f"{player_2.name} elige movimiento: ").lower()
            sleep(0.2)
            winner = movents(player_1_move, player_2_move)
            update_winner(player_1, player_2, winner)
            rounds += 1
        result = f"{player_1.wins} - {player_2.wins}"
        if player_1.wins > player_2.wins:
            winner = player_1.name
        else:
            winner = player_2.name
    print(f"Partida terminada, {winner} ha ganado, el resultado final es: {result}")
    print("¡Gracias por jugar, hasta la proxima!")
    
def main():
    choice = number_of_players()
    game = number_of_rounds()
    player_1, player_2 = create_player(choice)
    single_mode, player_1, player_2 = checking_is_multiplayer(player_1, player_2)
    play_round(player_1, player_2, single_mode, game)

    
if __name__ == "__main__":
    main()