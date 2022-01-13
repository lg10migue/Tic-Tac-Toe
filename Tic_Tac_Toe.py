"""
Tic-Tac-Toe.
Script for the Prove: Developer activity of week two.
Author: Miguel López.
"""
# Global variables

# Color for each player.
CE = '\33[0m' # Default
CB = '\33[34m' # Blue
CY = '\33[33m' # Yellow

# Players with colors.
x = f"{CB}x{CE}"
o = f"{CY}o{CE}"

# Functions.
def main():
    # Start the game.
    player = next_player( "" )

    # Create board.
    board = create_board()

    # Loop to keep the game and check for draw or winner.
    while not ( has_winner( board ) or is_draw( board ) ):
        display_board( board )
        make_move( player, board )
        player = next_player( player )
    display_board( board )

    # The end of the game.
    if has_winner( board ):
        player = next_player( player )
        print( f"Good game player {player}, YOU WIN! Thanks for playing!" )
    elif is_draw( board ):
        print( f"DRAW! Nice game! Thanks for playing!" )

def create_board():
    """Create a list called board.
    Return: Board.
    """
    board = []
    for square in range(9):
        board.append( square + 1 )
    return board

def display_board( board ):
    """Display the board in terminal.
    Parameters
        Board: The board to be displayed.
    Return: Nothing.
    """
    print( f"\n{board[0]}|{board[1]}|{board[2]}" )
    print( "-+-+-" )
    print( f"{board[3]}|{board[4]}|{board[5]}" )
    print( "-+-+-" )
    print( f"{board[6]}|{board[7]}|{board[8]}\n" )

def next_player( current ):
    """Determine which one is the next player.
    Parameters
        current: The current player in the turn.
    Return: The next player, should be "x" or "o".
    """
    # Condition to determine the player.
    if current == "" or current == o:
        return x
    elif current == x:
        return o

def make_move( player, board ):
    """Make a move for a player.
    Parameters
        player: The current player to make the move.
        board: The board were the move is going to be done.
    Return: Nothing.
    """
    square = int( input( f"{player}'s turn to make a move (1-9): " ) )
    board[square - 1] = player

def is_draw( board ):
    """Determine if the game is in draw or not.
    Parameters
        board: The board to check.
    Return: True if the game is in draw or False if not.
    """
    for square in range( 9 ):
        if board[square] != x and board[square] != o:
            return False
    return True 
    
def has_winner( board ):
    """Determine if the game has a winner, comparing the value in every single position of the board.
    Parameters
        board: The board to check.
    Return: True if the game has a winner of False if not.
    """
    return ( board[0] == board[1] == board[2] or board[3] == board[4] == board[5] or board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or board[1] == board[4] == board[7] or board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or board[2] == board[4] == board[6] )

if __name__ == "__main__":
    main()