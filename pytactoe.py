import numpy as np
import json

import colorama
from colorama import Fore
from termcolor import cprint
from pyfiglet import figlet_format

import network as nt


def custom_input(message, input_type, board=[], net=False, num_list=[]):
    """Custom query function for better error handling and cleaner recursion"""
    error = False
    query = input(message)

    if query == "q":
        quit()

    if input_type == "yn":

        if query == "y":
            return True

        elif query == 'n':
            return False

        else:
            error_msg = "\n  ERROR:\n  Please input either y or n."
            error = True

    elif input_type == "int":

        try:
            q = int(query)

        except ValueError:
            error_msg = "\n  ERROR:\n  Please input integer."
            error = True

        else:

            if net:

                try:
                    net[q]
                except IndexError:
                    error_msg = "\n  ERROR:\n  List index out of range."
                    error = True

            else:

                if q <= 0:
                    error_msg = "\n  ERROR:\n  Please input a valid number."
                    error = True

                if board:

                    move = q - 1
                    if move < 0 or move > 8 or board[move] != 0:
                        error_msg = "\n  ERROR:\n  Invalid move."
                        error = True
                    else:
                        return move

                elif num_list:

                    if q not in num_list:
                        error_msg = "\n  ERROR:\n  Please input a valid number."
                        error = True

            if not error:
                return q

    if error:
        print(Fore.RED + error_msg)
        return custom_input(
            message, input_type, board=board, net=net, num_list=num_list
            )


def display_board(board):
    """Displays board to console"""
    b = board.reshape(1, 9)[0].tolist()
    d_board = ["X" if val == 1 else "O" if val == -1 else " " for val in b]

    print(f"\n  {d_board[0]} | {d_board[1]} | {d_board[2]}")
    print("  --+---+--")
    print(f"  {d_board[3]} | {d_board[4]} | {d_board[5]}")
    print("  --+---+--")
    print(f"  {d_board[6]} | {d_board[7]} | {d_board[8]}\n")


def check_win(board):
    """Returns board win condition and game end message"""
    win = nt.check_win(board)
    if win == 1:

        msg = "  The network has won!"
        print(Fore.RED + msg)

    elif win == -1:

        msg = "  You beat the computer! Maybe I should've coded it better... "
        print(Fore.GREEN + msg)

    return win


def play_network(index):
    """Plays game against user"""
    print(Fore.YELLOW + "\n  |The network is trained to go first.   |")
    print(Fore.YELLOW + "  |To move, input the number of the tile.|")

    network = nt.select_network(index)
    board = np.zeros((9, 1))
    win = 0
    turn = 0
    while win == 0 and turn != 9:

        network.network_move(board)
        board[network.net_move] = 1
        print(Fore.YELLOW + "\n  Network's move:")
        display_board(board)
        win = check_win(board)
        turn += 1
        if win == 0 and turn != 9:

            msg = "\n  Your move: ... "
            b = board.reshape(1, 9)[0].tolist()
            move = custom_input(msg, "int", board=b)
            board[move] = -1
            print(Fore.YELLOW + "\n  Your move: ")
            display_board(board)
            win = check_win(board)
            turn += 1

    if win == 0 and turn == 9:
        print(Fore.YELLOW + "\n  It's a draw! (nobody saw that coming)")


colorama.init(autoreset=True)

while True:

    cprint(
        figlet_format("  py  tac toe", font="chunky"),
        "green", attrs=["bold"],
        )
    print("\n  Input q anytime to quit.")
    print(Fore.YELLOW + "\n  |+| What would you like to do? |+|")
    print(Fore.YELLOW + "  (type the number of your choice and hit enter)")

    print("\n  1 - Train your own neural network.")
    print("  2 - Play against the best network.")
    print("  3 - Play against a network of your choice.")
    num_list = [1, 2, 3]
    choice = custom_input("\n  ... ", "int", num_list=num_list)

    if choice == 1:

        warning = "\n  WARNING: \n  This might take a while, the recommended \
values are 50 networks and 800 generations for good results.\
\n  You can exit any time with CTRL-C."
        print(Fore.RED + warning)  # Not sure about the red, might be too much

        msg = "\n  How many networks do you want to train? ... "
        num_net = custom_input(msg, "int")
        msg = "\n  How many generations do you want to train them for? ... "
        gens = custom_input(msg, "int")
        nt.learn(num_net, gens)

        print(Fore.GREEN + "\n  The network has finished training!")
        msg = "\n  Do you want to add a description?(y/n) ... "
        description = custom_input(msg, "yn")
        if description:

            description = input("\n  Write your description here: ... ")
            filename = "best_network.json"
            with open(filename) as f:
                network_list = json.load(f)
            network_list[-1]["description"] = description
            with open(filename, 'w') as f:
                json.dump(network_list, f, indent=4)

        msg = "\n  Do you want to play against the network?(y/n) ... "
        choice = custom_input(msg, "yn")
        if choice:

            play = True
            while play:

                play_network(-1)
                msg = "\n  Do you want to play again?(y/n) ... "
                play = custom_input(msg, "yn")

    elif choice == 2:

        filename = "best_network.json"
        with open(filename) as f:
            network_list = json.load(f)

        sorted_list = sorted(network_list, key=lambda net: net["score"])
        try:
            best_net = sorted_list[-1]

        except IndexError:
            error_msg = "\n  ERROR:\
            \n  It looks like you haven't saved any network yet!"
            print(Fore.RED + error_msg)

        else:

            index = network_list.index(best_net)
            print(Fore.GREEN + "\n  Network description: ")
            print("  ", network_list[index]["description"])
            play = True
            while play:

                play_network(index)
                msg = "\n  Do you want to play again?(y/n) ... "
                play = custom_input(msg, "yn")

    elif choice == 3:

        loop = True
        while loop:

            filename = "best_network.json"
            with open(filename) as f:
                network_list = json.load(f)
            print(Fore.GREEN + "\n  Network description: ")
            for net in network_list:

                index = network_list.index(net)
                print(f"\n  [{index}] Score: {net['score']}")
                print(f"      {net['description']}")

            msg = "\n  |+| Please input the index of your desired network in \
the json file. |+|"
            print(Fore.YELLOW + msg)
            index = custom_input(" ... ", "int", net=network_list)

            play = True
            while play:

                play_network(index)
                msg = "\n  Do you want to switch network?(y/n) ... "
                switch = custom_input(msg, "yn")
                if switch:
                    play = False

                else:
                    msg = "\n Do you want to play again?(y/n) ... "
                    ans = custom_input(msg, "yn")
                    play = ans
                    loop = ans
