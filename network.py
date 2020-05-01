import numpy as np
import json
import unittest

from opponent_move import opponent_move

"""
This is based on a paper titled 'Using Evolutionary Programming to Create
Neural Networks that are Capable of Playing Tic-Tac-Toe'.
The values and algorithms used in this project are taken from the paper,
except for the propagation function which isn't discussed as strictly and
which consequently ended up being a complete mess due to it being left up
to my own discretion.
"""


def sigmoid(arr_in):
    """Returns column array of m = sigmoid(n) for n in array"""
    arr_len = len(arr_in)
    arr_out = np.zeros((arr_len, 1))
    for i in range(arr_len):
        arr_out[i] = 1 / (1 + np.exp(-arr_in[i]))

    return arr_out


def check_win(board):
    """
    Returns 1, -1 for winning player, 0 for drawing position.
    """
    win = 0
    r_board = board.reshape((3, 3))
    row_sum = np.absolute(np.sum(r_board, axis=1))
    col_sum = np.absolute(np.sum(r_board, axis=0))
    winning_row = np.nonzero(row_sum == 3)[0]
    winning_col = np.nonzero(col_sum == 3)[0]

    if abs(r_board[0, 0] + r_board[1, 1] + r_board[2, 2]) == 3:

        if r_board[0, 0] == 1:
            win = 1
        else:
            win = -1

    elif abs(r_board[2, 0] + r_board[1, 1] + r_board[0, 2]) == 3:

        if r_board[2, 0] == 1:
            win = 1
        else:
            win = -1

    elif winning_row.size > 0:

        if r_board[winning_row[0], 0] == 1:
            win = 1
        else:
            win = -1

    elif winning_col.size > 0:

        if r_board[0, winning_col[0]] == 1:
            win = 1
        else:
            win = -1

    return win


class Network():

    def __init__(self, net_dict=False):
        """
        If a dict is passed, network is initialized with dict values.
        Else, random values are used.
        """
        if net_dict:

            self.n2 = net_dict["n2"]
            self.w2 = np.array(net_dict["w2"])
            self.w3 = np.array(net_dict["w3"])
            self.b2 = np.array(net_dict["b2"])
            self.b3 = np.array(net_dict["b3"])

        else:

            self.n2 = np.random.randint(1, 10)
            self.w2 = np.random.uniform(-0.5, 0.5, (self.n2, 9))
            self.w3 = np.random.uniform(-0.5, 0.5, (9, self.n2))
            self.b2 = np.random.uniform(-0.5, 0.5, (self.n2, 1))
            self.b3 = np.random.uniform(-0.5, 0.5, (9, 1))

    def dict(self):
        """Creates dict with net values"""
        net_dict = {}
        net_dict["n2"] = self.n2
        net_dict["w2"] = self.w2.tolist()
        net_dict["w3"] = self.w3.tolist()
        net_dict["b2"] = self.b2.tolist()
        net_dict["b3"] = self.b3.tolist()

        return net_dict

    def network_move(self, board):
        """Sets net_move based on network and board array."""
        layer_2 = sigmoid(self.w2.dot(board) - self.b2)
        layer_3 = sigmoid(self.w3.dot(layer_2) - self.b3)

        for n in range(len(layer_3)):
            if board[n, 0] == 1 or board[n, 0] == -1:
                layer_3[n, 0] = -1000
        self.net_move = np.nonzero(layer_3 == np.amax(layer_3))[0][0]

    @staticmethod
    def get_turn(board):
        """Returns turn based on input board."""
        board = board.reshape((3, 3))
        used_squares = np.nonzero(board)[0]
        return len(used_squares)

    def play_game(self, board):
        """Plays game between heuristic AI and network."""
        self.win = 0
        turn = self.get_turn(board)
        while self.win == 0 and turn != 9:

            self.network_move(board)
            board[self.net_move, 0] = 1
            self.win = check_win(board)
            turn += 1
            if self.win == 0 and turn <= 8:

                opp_move = opponent_move(board, turn)
                board[opp_move] = -1
                self.win = check_win(board)
                turn += 1

    @staticmethod
    def setup_board(first_move, second_move):
        """Creates empty board and adds 2 moves"""
        board = np.zeros((9, 1))
        board[first_move, 0] = 1
        board[second_move, 0] = -1
        return board

    def net_payoff(self):
        """
        Makes network play against ai with first 2 moves fixed, 4 games for
        each possible response to the first move. (change number of games to
        offset variance due to randomness in opponent's play)
        """
        board = np.zeros((9, 1))
        self.network_move(board)
        first_move = self.net_move

        self.score = 0
        pos = 0
        while pos <= 8:

            if first_move == pos:
                pos += 1

            for _ in range(4):

                board = self.setup_board(first_move, pos)
                self.play_game(board)

                if self.win == 1:
                    self.score += 1

                elif self.win == -1:
                    self.score -= 10

            pos += 1
            if first_move == 8 and pos == 8:
                pos += 1

    def normrand(self, mean):
        """Varies all network values by mean with normal distribution"""
        self.w2 += np.random.normal(0.0, mean, (self.n2, 9))
        self.w3 += np.random.normal(0.0, mean, (9, self.n2))
        self.b2 += np.random.normal(0.0, mean, (self.n2, 1))
        self.b3 += np.random.normal(0.0, mean, (9, 1))

    def modify_layer(self):
        """Chance to change number of neurons in hidden layer"""
        chance = np.random.randint(4)

        if chance == 0 and self.n2 < 10:

            self.n2 += 1
            self.w2 = np.concatenate((self.w2, np.zeros((1, 9))))
            self.w3 = np.concatenate((self.w3, np.zeros((9, 1))), axis=1)
            self.b2 = np.concatenate((self.b2, np.array([[0]])))

        elif chance == 1 and self.n2 > 1:

            self.n2 -= 1
            self.w2 = self.w2[:-1]
            self.w3 = self.w3[:, :-1]
            self.b2 = self.b2[:-1]

    def evolve(self, parent_score):
        """Randomly modifies network values and checks for improvement"""
        n2_parent = self.n2
        w2_parent = self.w2
        w3_parent = self.w3
        b2_parent = self.b2
        b3_parent = self.b3

        self.normrand(0.05)
        self.modify_layer()
        self.net_payoff()

        if self.score > parent_score:

            self.improved = True

        else:

            self.improved = False
            self.w2 = w2_parent
            self.w3 = w3_parent
            self.b2 = b2_parent
            self.b3 = b3_parent
            self.n2 = n2_parent


def select_network(index):
    """Initializes network based on network list"""
    filename = "best_network.json"
    with open(filename) as f:
        net_list = json.load(f)

    net_dict = net_list[index]
    network = Network(net_dict)

    return network


def propagate(scores):
    """
    Outputs string of indices for the score list such that the frequency
    of each index is exponentially proportional to its score.
    """
    score_arr = np.array(scores)
    score_arr += abs(np.amin(score_arr))
    score_arr = 50 * score_arr / np.sum(score_arr)
    polarized_scores = np.power(score_arr, 3)
    polarized_scores = np.around(polarized_scores, 4)

    edges = np.cumsum(polarized_scores)
    size = len(edges)
    x_values = np.random.uniform(0, np.sum(polarized_scores), (1, size))[0]
    distribution = np.histogram(x_values, edges)

    bins = distribution[0].tolist()
    propagate = []
    index = 0
    for n in bins:
        for _ in range(n):
            propagate.append(index)
        index += 1
    while len(propagate) < len(scores):  # lazy fix
        index = np.random.randint(0, 50)
        propagate.append(index)

    return propagate


def save_to_json(score, net):
    """Dumps network to json file"""
    filename = "best_network.json"
    try:
        with open(filename) as f:
            score_list = json.load(f)

    except FileNotFoundError:
        print("Creating new file to store the best network ...")
        score_list = []

    net_dict = net.dict()
    net_dict['score'] = score
    net_dict['description'] = ""
    score_list.append(net_dict)

    with open(filename, 'w') as f:
        json.dump(score_list, f, indent=4)


def learn(networks, generations):
    """
    Creates list of Networks, for each generation calls the evolve method
    and feeds score list to propagate function to generate children list.
    """
    net_list = []
    for _ in range(networks):

        net = Network()
        net_list.append(net)

    scores = np.zeros((1, networks))[0]
    best_score = -1000
    count = 0

    for gen in range(generations):

        if networks > 1:
            for net in range(networks):

                n = net_list[net]
                if gen > 0:
                    n.net_payoff()
                    parent_score = n.score
                else:
                    parent_score = -640

                n.evolve(parent_score)
                if n.improved:
                    scores[net] = n.score
                else:
                    scores[net] = parent_score

                if scores[net] >= best_score:

                    best_score = scores[net]
                    best_net = n

            parents = propagate(scores)
            for net in range(networks):

                parent = parents[net]
                if scores[net] < scores[parent]:

                    n = net_list[parent]
                    net_dict = n.dict()
                    net_list[net] = Network(net_dict)

        elif networks == 1:  # Just in case

            if gen == 0:
                score = 0
            n = net_list[0]
            n.evolve(score)
            if n.improved:
                score = n.score

            if score >= best_score:

                best_score = score
                best_net = n

        count += 1
        print(f"  Generation {count}. Best score: {best_score}")

    save_to_json(best_score, best_net)
