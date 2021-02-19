from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer
import time


class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]  # represents the board
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:  # return   the groups os rows: 0, 1, 2 / 3, 4, 5...
            print("| " + " | ".join(row) + " |")

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]  # List comprehension

        """moves = []
        for (i, spot) in enumerate(self.board):
            if spot == " ":
                moves.append(i)

        return moves"""

    def empty_squares(self):
        return " " in self.board

    def num_empty_squares(self):
        return self.board.count(" ")

    def make_move(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check the line
        row_index = square // 3
        row = self.board[row_index*3: (row_index + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        # check de column
        column_index = square % 3
        column = [self.board[column_index + i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # check diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all(spot == letter for spot in diagonal1):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all(spot == letter for spot in diagonal2):
                return True

        return False


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = "X"

    while game.empty_squares():
        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):
            if print_game:
                print(letter + f" makes a move to square {square}")
                game.print_board()
                print("")

            if game.current_winner:
                if print_game:
                    print("Winner of the game was: " + letter)
                return letter

            letter = "X" if letter == "O" else "O"

            if print_game:
                time.sleep(0.5)
    if print_game:
        print("It's a tie!")


if __name__ == '__main__':
    while True:
        type = input("Que tipo de jogo você deseja?\nA - Humano x Humano\nB - Humano - Computador"
                     "\nC - Computador - Computador\n").capitalize()

        if type == "A":
            x_player = HumanPlayer("X")
            o_player = HumanPlayer("O")
        elif type == "B":
            dificuldade = input("Qual nível de computador você quer enfrentar?\nA - Fácil\nB - Difícil\n").capitalize()

            if dificuldade == "A":
                x_player = HumanPlayer("X")
                o_player = RandomComputerPlayer("O")
            else:
                x_player = HumanPlayer("X")
                o_player = GeniusComputerPlayer("O")
        else:
            nivel_pc1 = input("Qual nível do computador 1?\nA - Fácil\nB - Difícil\n").capitalize()
            nivel_pc2 = input("Qual nível do computador 2?\nA - Fácil\nB - Difícil\n").capitalize()

            x_player = RandomComputerPlayer("X") if nivel_pc1 == "A" else GeniusComputerPlayer("X")
            o_player = RandomComputerPlayer("O") if nivel_pc2 == "A" else GeniusComputerPlayer("O")

        t = TicTacToe()
        play(t, x_player, o_player, print_game=True)
