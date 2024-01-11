'''
#player class behind the scene
'''
'''
def choose_symbol():
        while True:
            symbol=input("please enter a letter")
            if symbol.isalpha() and len(symbol)==1:
                symbol = symbol.upper()
                print(symbol)
                break
            print("invalid symbol please enter an invalid symbol") 
        
        
print(choose_symbol())
'''
#menu class behind the scene
'''
class Menu:
    def choice_validation(self):
        #choice= int(input("enter your choise  1 or 2"))
        while True:
            self.choice= input("enter your choise  1 or 2")
            if choice != 1 or choice != 2:
                print("You must type 1 or 2")
                choice= int(input("enter your choise  1 or 2"))
            if choice == 1 or choice == 2:
                print(choice)
                return choice
        
    def main_menu(self):
        print("Welcom to Tic Tac Toe game\n"+"1-New Game\n" +"2-Quit Game")
        validation = choice_validation()


    main_menu()            
'''
#menu class best practise  behind the scene
'''
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
'''


# Creating an instance of the Menu class
#menu = Menu()

# Calling the main_menu() and end_game_menu() method
#menu.main_menu()
#menu.end_game_menu()
'''

#board class behind the scene

#class game behined the scene
class Game:
    def __init__(self):
        self.current_player_index = 0
        self.players=[Player(),Player()]
        self.board=Board()
        self.menu=Menu()
        
    
    
    
    def start_game(self):
        choice=self.menu.display_main_menu
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
            count+=count
    
    #another way is to use enumerate()
    #for num,player in enumerate(self.player,start1): 
    #    print(f"player{num},enter your info")
    #    player.choose_name()
    #    player.choose_symbol()       
    
    
    

    #inside the run_game() inside the play_turn
    '''
'''
    def place_index_validation(self):
        while True:
            try:
                place_choice = int(input("Enter a place from (1-9): "))
                if 1<=place_choice<=9 and self.board.update_board(place_choice,player,sympol):
                    #print(place_choice)
                    #return place_choice
                    break
                else:
                    print("invalid place, try again")
            except ValueError:
                print("Invalid input. Please enter a number between (1-9)") 
        
        validation = self.place_index_validation()
        return validation        
    '''
    