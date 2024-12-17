class Board:
    def __init__(self):
        # Initialize empty board
        self.board = [[' ']*3 for _ in range(3)] # 3x3 board
    
    def print_board(self):
        # Print board
        for row in self.board:
            # Print row separator and cells 
            print("|", end=" ")
            for cell in row:
                # Print cell and separator
                print(cell," | ", end = " ")
            print("\n")

    def isvalidmove(self,row,col):
        # Check if position is within board bounds and cell is empty
        if 0 <= row <=2 and 0 <= col <= 2:
            # Check if cell is empty
            return self.board[row][col] == ' '
        # Return False if position is out of bounds
        return False
    
    def get_board(self):
        return self.board
    

class BoardState:
    def __init__(self, board):
        self.board = board

    def check_winner(self):
        # rows for winner
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]
        # columns for winner
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]
            
        # diagonals for winner
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        
        return None
    
    def is_full(self):
        # Check if board is full
        return all(cell != " " for row in self.board for cell in row)
    
    def get_status(self):
        # Check if game is over
        winner = self.check_winner()
        # Check if board is won or full
        if winner:
            print(f"Player {winner} wins!")
            return "stopped"
        elif self.is_full():
            print("Game is a draw!")
            return "stopped"
        # Return ongoing state if game is not over
        return "ongoing"

class Player:
    def __init__(self, symbol):
        self.symbol = symbol
    
    def get_symbol(self):
        return self.symbol
    
    def make_move(self, board,row,col):
        # Check if move is valid
        if board.isvalidmove(row,col):
            # Make move if valid
            board.get_board()[row][col] = self.symbol
            return True
        else:
            print("Invalid move! Try again.")
            # Return False if move is invalid
            self.make_move(board)
            return False
        
def main():
    # Initialize game
    board = Board()
    playerx = Player("X")
    playero = Player("O")
    current_player = playerx
    boardstate = BoardState(board.board)

    # Play game until game is stopped
    while True:
        board.print_board()
        # Print current player
        print("Player", current_player.get_symbol(), "turn")

        # Get player move and check if game is stopped after move
        try:
            # Get player move
            row = int(input("Enter row: "))
            col = int(input("Enter column: "))

            # Check if move is within bounds
            if not(0 <= row <= 2 and 0 <= col <= 2):
                print("Invalid move! Try again.")
                continue

            # check if move is available
            if not current_player.make_move(board,row,col):
                print("Invalid move! Try again.")
                continue

            # Check if game is stopped
            if boardstate.get_status() == "stopped":
                board.print_board()
                break

            # Switch player after move
            current_player = (playero if current_player == playerx else playerx)

        # Handle invalid input exception
        except ValueError:
            print("Invalid input! Try again.")
            continue


if __name__ == "__main__":
    main()