"""
Tic-Tac-Toe.
Script for the Prove: Developer activity of week two.
Author: Miguel López.
"""

# Functions.
def main():
    # Starts the game.
    player = next_player( "" )

    # Create board.
    board = create_board()

    print( player )

def create_board():
    """Create a list called board.
    Return: Board.
    """
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def display_board(board):
    """Display the board in terminal.
    Parameters
        Board: The board to be displayed.
    Return: Nothing.
    """
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()

def next_player(current):
    """Determine which one is the next player.
    Parameters
        current: The current player in the turn.
    Return: The next player, should be "x" or "o".
    """
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

def make_move(player, board):
    """Make a move for a player.
    Parameters
        player: The current player to make the move.
        board: The board were the move is going to be done.
    Return: Nothing.
    """
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[square - 1] = player

if __name__ == "__main__":
    main()