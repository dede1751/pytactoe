import numpy as np


def opponent_move(board, turn):
    """
    Makes a move that is most likely correct. Guaranteed 10% chance to make
    a mistake. Next step is replacing this with a minmax implementation.
    """
    blocked = np.nonzero(board.reshape(1, 9))
    chance = np.random.randint(1, 11)  # Change this for less variance.
    if chance == 1 or turn == 1:
        while True:
            opp_mov = np.random.randint(0, 8)
            if opp_mov not in blocked[1]:
                break
    elif turn <= 8:
        t_board = board.reshape((3, 3))
        if t_board[0, 0] == -1 and t_board[0, 1] == -1 and t_board[0, 2] == 0:
            opp_mov = 2
        elif t_board[0, 0] == -1 and t_board[0, 2] == -1 and t_board[0, 1] == 0:
            opp_mov = 1
        elif t_board[0, 0] == -1 and t_board[1, 0] == -1 and t_board[2, 0] == 0:
            opp_mov = 6
        elif t_board[0, 0] == -1 and t_board[1, 1] == -1 and t_board[2, 2] == 0:
            opp_mov = 8
        elif t_board[0, 0] == -1 and t_board[2, 0] == -1 and t_board[1, 0] == 0:
            opp_mov = 3
        elif t_board[0, 0] == -1 and t_board[2, 2] == -1 and t_board[1, 1] == 0:
            opp_mov = 4
        elif t_board[0, 1] == -1 and t_board[0, 2] == -1 and t_board[0, 0] == 0:
            opp_mov = 0
        elif t_board[0, 1] == -1 and t_board[1, 1] == -1 and t_board[2, 1] == 0:
            opp_mov = 7
        elif t_board[0, 1] == -1 and t_board[2, 1] == -1 and t_board[1, 1] == 0:
            opp_mov = 4
        elif t_board[1, 0] == -1 and t_board[1, 1] == -1 and t_board[1, 2] == 0:
            opp_mov = 5
        elif t_board[1, 0] == -1 and t_board[1, 2] == -1 and t_board[1, 1] == 0:
            opp_mov = 4
        elif t_board[1, 0] == -1 and t_board[2, 0] == -1 and t_board[0, 0] == 0:
            opp_mov = 0
        elif t_board[0, 2] == -1 and t_board[1, 1] == -1 and t_board[2, 0] == 0:
            opp_mov = 6
        elif t_board[0, 2] == -1 and t_board[1, 2] == -1 and t_board[2, 2] == 0:
            opp_mov = 8
        elif t_board[0, 2] == -1 and t_board[2, 0] == -1 and t_board[1, 1] == 0:
            opp_mov = 4
        elif t_board[0, 2] == -1 and t_board[2, 2] == -1 and t_board[1, 2] == 0:
            opp_mov = 5
        elif t_board[1, 1] == -1 and t_board[1, 2] == -1 and t_board[1, 0] == 0:
            opp_mov = 3
        elif t_board[1, 1] == -1 and t_board[2, 0] == -1 and t_board[0, 2] == 0:
            opp_mov = 2
        elif t_board[1, 1] == -1 and t_board[2, 1] == -1 and t_board[0, 1] == 0:
            opp_mov = 1
        elif t_board[1, 1] == -1 and t_board[2, 2] == -1 and t_board[0, 0] == 0:
            opp_mov = 0
        elif t_board[1, 2] == -1 and t_board[2, 2] == -1 and t_board[0, 2] == 0:
            opp_mov = 2
        elif t_board[2, 0] == -1 and t_board[2, 1] == -1 and t_board[2, 2] == 0:
            opp_mov = 8
        elif t_board[2, 0] == -1 and t_board[2, 2] == -1 and t_board[2, 1] == 0:
            opp_mov = 7
        elif t_board[2, 1] == -1 and t_board[2, 2] == -1 and t_board[2, 0] == 0:
            opp_mov = 6
        elif t_board[0, 0] == 1 and t_board[0, 1] == 1 and t_board[0, 2] == 0:
            opp_mov = 2
        elif t_board[0, 0] == 1 and t_board[0, 2] == 1 and t_board[0, 1] == 0:
            opp_mov = 1
        elif t_board[0, 0] == 1 and t_board[1, 0] == 1 and t_board[2, 0] == 0:
            opp_mov = 6
        elif t_board[0, 0] == 1 and t_board[1, 1] == 1 and t_board[2, 2] == 0:
            opp_mov = 8
        elif t_board[0, 0] == 1 and t_board[2, 0] == 1 and t_board[1, 0] == 0:
            opp_mov = 3
        elif t_board[0, 0] == 1 and t_board[2, 2] == 1 and t_board[1, 1] == 0:
            opp_mov = 4
        elif t_board[0, 1] == 1 and t_board[0, 2] == 1 and t_board[0, 0] == 0:
            opp_mov = 0
        elif t_board[0, 1] == 1 and t_board[1, 1] == 1 and t_board[2, 1] == 0:
            opp_mov = 7
        elif t_board[0, 1] == 1 and t_board[2, 1] == 1 and t_board[1, 1] == 0:
            opp_mov = 4
        elif t_board[1, 0] == 1 and t_board[1, 1] == 1 and t_board[1, 2] == 0:
            opp_mov = 5
        elif t_board[1, 0] == 1 and t_board[1, 2] == 1 and t_board[1, 1] == 0:
            opp_mov = 4
        elif t_board[1, 0] == 1 and t_board[2, 0] == 1 and t_board[0, 0] == 0:
            opp_mov = 0
        elif t_board[0, 2] == 1 and t_board[1, 1] == 1 and t_board[2, 0] == 0:
            opp_mov = 6
        elif t_board[0, 2] == 1 and t_board[1, 2] == 1 and t_board[2, 2] == 0:
            opp_mov = 8
        elif t_board[0, 2] == 1 and t_board[2, 0] == 1 and t_board[1, 1] == 0:
            opp_mov = 4
        elif t_board[0, 2] == 1 and t_board[2, 2] == 1 and t_board[1, 2] == 0:
            opp_mov = 5
        elif t_board[1, 1] == 1 and t_board[1, 2] == 1 and t_board[1, 0] == 0:
            opp_mov = 3
        elif t_board[1, 1] == 1 and t_board[2, 0] == 1 and t_board[0, 2] == 0:
            opp_mov = 2
        elif t_board[1, 1] == 1 and t_board[2, 1] == 1 and t_board[0, 1] == 0:
            opp_mov = 1
        elif t_board[1, 1] == 1 and t_board[2, 2] == 1 and t_board[0, 0] == 0:
            opp_mov = 0
        elif t_board[1, 2] == 1 and t_board[2, 2] == 1 and t_board[0, 2] == 0:
            opp_mov = 2
        elif t_board[2, 0] == 1 and t_board[2, 1] == 1 and t_board[2, 2] == 0:
            opp_mov = 8
        elif t_board[2, 0] == 1 and t_board[2, 2] == 1 and t_board[2, 1] == 0:
            opp_mov = 7
        elif t_board[2, 1] == 1 and t_board[2, 2] == 1 and t_board[2, 0] == 0:
            opp_mov = 6
        elif t_board[0, 0] == 0 and t_board[0, 1] == 0 and t_board[0, 2] == -1:
            if chance <= 5:
                opp_mov = 0
            else:
                opp_mov = 1
        elif t_board[0, 0] == 0 and t_board[0, 2] == 0 and t_board[0, 1] == -1:
            if chance <= 5:
                opp_mov = 0
            else:
                opp_mov = 2
        elif t_board[0, 0] == 0 and t_board[1, 0] == 0 and t_board[2, 0] == -1:
            if chance <= 5:
                opp_mov = 0
            else:
                opp_mov = 3
        elif t_board[0, 0] == 0 and t_board[1, 1] == 0 and t_board[2, 2] == -1:
            if chance <= 5:
                opp_mov = 0
            else:
                opp_mov = 4
        elif t_board[0, 0] == 0 and t_board[2, 0] == 0 and t_board[1, 0] == -1:
            if chance <= 5:
                opp_mov = 0
            else:
                opp_mov = 6
        elif t_board[0, 0] == 0 and t_board[2, 2] == 0 and t_board[1, 1] == -1:
            if chance <= 5:
                opp_mov = 0
            else:
                opp_mov = 8
        elif t_board[0, 1] == 0 and t_board[0, 2] == 0 and t_board[0, 0] == -1:
            if chance <= 5:
                opp_mov = 1
            else:
                opp_mov = 2
        elif t_board[0, 1] == 0 and t_board[1, 1] == 0 and t_board[2, 1] == -1:
            if chance <= 5:
                opp_mov = 1
            else:
                opp_mov = 4
        elif t_board[0, 1] == 0 and t_board[2, 1] == 0 and t_board[1, 1] == -1:
            if chance <= 5:
                opp_mov = 1
            else:
                opp_mov = 7
        elif t_board[1, 0] == 0 and t_board[1, 1] == 0 and t_board[1, 2] == -1:
            if chance <= 5:
                opp_mov = 3
            else:
                opp_mov = 4
        elif t_board[1, 0] == 0 and t_board[1, 2] == 0 and t_board[1, 1] == -1:
            if chance <= 5:
                opp_mov = 3
            else:
                opp_mov = 5
        elif t_board[1, 0] == 0 and t_board[2, 0] == 0 and t_board[0, 0] == -1:
            if chance <= 5:
                opp_mov = 3
            else:
                opp_mov = 6
        elif t_board[0, 2] == 0 and t_board[1, 1] == 0 and t_board[2, 0] == -1:
            if chance <= 5:
                opp_mov = 2
            else:
                opp_mov = 4
        elif t_board[0, 2] == 0 and t_board[1, 2] == 0 and t_board[2, 2] == -1:
            if chance <= 5:
                opp_mov = 2
            else:
                opp_mov = 5
        elif t_board[0, 2] == 0 and t_board[2, 0] == 0 and t_board[1, 1] == -1:
            if chance <= 5:
                opp_mov = 2
            else:
                opp_mov = 6
        elif t_board[0, 2] == 0 and t_board[2, 2] == 0 and t_board[1, 2] == -1:
            if chance <= 5:
                opp_mov = 2
            else:
                opp_mov = 8
        elif t_board[1, 1] == 0 and t_board[1, 2] == 0 and t_board[1, 0] == -1:
            if chance <= 5:
                opp_mov = 4
            else:
                opp_mov = 5
        elif t_board[1, 1] == 0 and t_board[2, 0] == 0 and t_board[0, 2] == -1:
            if chance <= 5:
                opp_mov = 4
            else:
                opp_mov = 6
        elif t_board[1, 1] == 0 and t_board[2, 1] == 0 and t_board[0, 1] == -1:
            if chance <= 5:
                opp_mov = 4
            else:
                opp_mov = 7
        elif t_board[1, 1] == 0 and t_board[2, 2] == 0 and t_board[0, 0] == -1:
            if chance <= 5:
                opp_mov = 4
            else:
                opp_mov = 8
        elif t_board[1, 2] == 0 and t_board[2, 2] == 0 and t_board[0, 2] == -1:
            if chance <= 5:
                opp_mov = 5
            else:
                opp_mov = 8
        elif t_board[2, 0] == 0 and t_board[2, 1] == 0 and t_board[2, 2] == -1:
            if chance <= 5:
                opp_mov = 6
            else:
                opp_mov = 7
        elif t_board[2, 0] == 0 and t_board[2, 2] == 0 and t_board[2, 1] == -1:
            if chance <= 5:
                opp_mov = 6
            else:
                opp_mov = 8
        elif t_board[2, 1] == 0 and t_board[2, 2] == 0 and t_board[2, 0] == -1:
            if chance <= 5:
                opp_mov = 7
            else:
                opp_mov = 8
        else:
            while True:
                opp_mov = np.random.randint(0, 8)
                if opp_mov not in blocked[1]:
                    break
    return opp_mov
