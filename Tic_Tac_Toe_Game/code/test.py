'''
import os
def clear_screen():
    os.system("cls" if os.name=="nt" else "clear")

#when u want to clear the screen call this func 
#clear_screen()
'''
class Player:
    def __init__(self):
        self.name=""
        self.symbol=""
    
    def choose_name(self):
        while True:
            name = input("please enter a name")
            if name.isalpha():
                self.name = name
                return self.name
                break
            print("invalid name please enter a valid name")
        
    def choose_symbol(self):
        while True:
            symbol=input("please enter a letter")
            if symbol.isalpha() and len(symbol)==1: #and symbol.isdigit()):
                self.symbol = symbol.upper()
                return self.symbol
                break
            print("invalid symbol please enter a valid symbol")
            
        
class Menu:
    def choice_validation(self):
        while True:
            try:
                choice = int(input("Enter your choice (1 or 2): "))
                if choice == 1 or choice == 2:
                    #print(choice)
                    return choice
                else:
                    print("You must type 1 or 2")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    def main_menu(self):
        print("Welcome to Tic Tac Toe game\n" + "1-New Game\n" + "2-Quit Game")
        validation = self.choice_validation()
        return validation

    def end_game_menu(self):
        print("Game over\n" + "1-New Game\n" + "2-Quit Game")
        validation = self.choice_validation()
        return validation 
        

class Board:
    def __init__(self):
        self.board=[str(i) for i in range (1,10)]
        
    def display_board(self):
        for i in range(0, 9, 3):
            row = self.board[i:i+3]
            print(f"{row[0]} | {row[1]} | {row[2]}")
            if i < 6:
                print("-" * 9)
        #return self.display_board
        
    def update_board(self,choice,symbol):
        if self.is_acceptable_move(choice):
            self.board[choice-1]=symbol
            return True
        return False
    
    def is_acceptable_move(self,choice):
        return self.board[choice-1].isdigit()
    
    def reset_board(self):
        self.board=[str(i) for i in range (1,10)]
        
        
class Game:
    def __init__(self):
        self.current_player_index = 0
        self.players=[Player(),Player()]
        self.board=Board()
        self.menu=Menu()
    
    
    #stage 1 in game logic    
    def start_game(self):
        choice=self.menu.main_menu()
        if choice == 1:
            self.store_players_info()
            self.run_game()
        else:
            self.quit_game()
            
            
    def store_players_info(self):
        count=1
        for player in self.players:
            print(f"player{count},enter your info")    
            player.choose_name()
            player.choose_symbol()
            print("-\*/-"*10)
            count+=count
    
    
    #stage 2 in game logic       
    #complex game logic here!!!
    def run_game(self):
        while True:
            self.play_turn()
            if self.check_win():
                print("\ncongratulations!!!!!!\n")
                choice = self.menu.end_game_menu()
                
                if choice == 1:
                    self.restart_game()
                else:
                    self.quit_game()
                    break    
            elif self.check_draw():
                print("draw, no winner here")
                choice = self.menu.end_game_menu()
                if choice == 1:
                    self.restart_game()
                else:
                    self.quit_game()
                    break    
                
    def play_turn(self):
        self.board.display_board()
        print("\n")
        player = self.players[self.current_player_index]
        print(f"{player.name}'s turn ({player.symbol})")
        self.place_index_validation(player)
        #return validation
        self.switch_player()
    #to keep achieving solid principle (SRP)
    # to validate if the user move in a valid place (empty and acceptable)    
    def place_index_validation(self,player):
        while True:
            try:
                player = self.players[self.current_player_index]
                place_choice = int(input("Enter a place from (1-9): "))
                if 1<=place_choice<=9 and self.board.update_board(place_choice,player.symbol):
                    return place_choice
                    #break
                else:
                    print("invalid place, try again")
            except ValueError:
                print("Invalid input. Please enter a number between (1-9)")     
    
    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index
    
    def check_win(self):
        winning_combinations = [
            # Rows
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            # Columns
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            # Diagonals
            [0, 4, 8],
            [2, 4, 6]
        ]
        for comb in winning_combinations:
            if (self.board.board[comb[0]]==self.board.board[comb[1]]==
                self.board.board[comb[2]]):
                self.board.display_board()
                print(f"\nplayer {self.board.board[comb[2]]} win the game")
                return True 
        return False
    
    def check_draw(self):
        draw= all(not cell.isdigit() for cell in self.board.board)
        if draw:  self.board.display_board()
        return draw
        #we use generator expression insteed of list comperhention?
        #to decrease the memor that is stored for this process
    def restart_game(self):
        self.board.reset_board()           
        self.current_player_index=0
        self.run_game()
    def quit_game(self):
        print("good bye,see u soon in another game")       

game=Game()
game.start_game()

#a draw senario for testing:
#player1: 1,2,6,7,9
#player2: 3,4,5,8