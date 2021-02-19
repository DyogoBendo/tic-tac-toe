import math
import random


class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + "'s turn. Input move (0-8): ")

            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid value")

        return val


class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())  # random choice
        else:
            # use de minimax algorithm
            square = self.minimax(game, self.letter)["position"]

        return square

    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == "X" else "X"

        # The base case: when the match was won in the last move
        if state.current_winner == other_player:
            return {"position": None,
                    "score": (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                         state.num_empty_squares() + 1)
                    }
        elif not state.empty_squares():  # if there are no more blank spaces
            return {"position": None, "score": 0}

        if player == max_player:
            best = {"position": None, "score": -math.inf}  # we look for the biggest number
        else:
            best = {"position": None, "score": math.inf}  # we look for the smallest number

        for possible_move in state.available_moves():
            # Step 1: We make a move
            state.make_move(possible_move, player)

            # Step 2: Using minimax in recursive way, we simulate a game after the choice of that position
            sim_score = self.minimax(state, other_player)  # We alternate the players

            # Step 3: We undo the moves
            state.board[possible_move] = " "
            state.current_winner = None
            sim_score["position"] = possible_move

            # Step 4: We update the best place if it's needed
            if player == max_player:
                if sim_score["score"] > best["score"]:
                    best = sim_score
            else:
                if sim_score["score"] < best["score"]:
                    best = sim_score
        return best
