"""
Tic-Tac-Toe.
Script for the Prove: Developer activity of week two.
Author: Miguel López.
"""

# Functions.
def main():
    # Create board.
    board = create_board()

    print ( board )

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

if __name__ == "__main__":
    main()