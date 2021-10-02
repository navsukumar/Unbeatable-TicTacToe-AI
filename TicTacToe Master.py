import math
class board2():
    def __init__(self):
        self.tiles = [" " for i in range(9)]
    
    def print_State(self):
        [print("|" + self.tiles[i * 3] + "|" + self.tiles[i * 3 + 1] + "|" + self.tiles[i * 3 + 2] + "|") for i in range(3)]
    
    def print_Nums(self):
        [print("|" + str(i * 3) + "|" + str(i * 3 + 1) + "|" + str(i * 3 + 2) + "|") for i in range(3)]
    
    def diagonal_Helper(self,letter):
        lDiagonal = [self.tiles[i] for i in [0,4,8]]
        rDiagonal = [self.tiles[i] for i in [2,4,6]]
        return all([i == letter for i in lDiagonal]) or all([i == letter for i in rDiagonal])

    def check_Win(self,spot,letter):
        #check row
        row = [self.tiles[i] for i in range((spot//3) * 3, (spot//3) * 3 + 3)]
        col = [self.tiles[spot % 3 + i*3] for i in range(3)]
        if all([j == letter for j in row]) or all([j == letter for j in col]) or self.diagonal_Helper(letter):
            return True
    
    def drawCheck(self,tiles):
        return all([i != " " for i in tiles])
    
    def remaining_Tiles(self,tiles):
        return [i for i in range(9) if tiles[i] == " "]
    
    def minimax(self,spot, char):
        if self.check_Win(spot, char) and char == self.computer:
            return {"position": spot,"value":len(self.remaining_Tiles(self.tiles)) + 1}
        elif self.check_Win(spot, char) and char == self.player:
            return {"position": spot,"value":-(len(self.remaining_Tiles(self.tiles)) + 1)}
        elif self.drawCheck(self.tiles):
            return {"position": spot, "value": 0}
        else:
            if char == self.computer:
                best = {"position": spot,"value": -math.inf}
            else:
                best = {"position": spot,"value": math.inf}
            for i in self.remaining_Tiles(self.tiles):
                if char == self.player:
                    other_letter = self.computer
                else:
                    other_letter = self.player
                self.tiles[i] = other_letter
                other_score = self.minimax(i,other_letter)
                self.tiles[i] = " "
                other_score["position"] = i

                if char == self.computer and other_score["value"] > best["value"]:
                    best = other_score
                elif char == self.player and other_score["value"] < best["value"]:
                    best = other_score
            return best


    def play(self):
        choices = [i for i in range(9)]
        print("Welcome to TicTacToe")
        self.player = input("Would you like to be O or X?")
        print()
        if self.player == "O":
            self.computer = "X"
        else:
            self.computer = "O"
        print("These are the tiles and their positions")
        print()
        self.print_Nums()
        while True:
            spot = int(input("Pick a spot"))
            print()
            if spot < 0 or spot > 8 or self.tiles[spot] != " ":
                print("Invalid Output, Please try again")
                continue
            self.tiles[spot] = self.player
            if self.check_Win(spot, self.player):
                self.print_State()
                print("You win!")
                exit()
            if self.drawCheck(self.tiles):
                self.print_State()
                print("It is a draw!")
                exit()
            computer_spot = self.minimax(spot,self.player)["position"]
            self.tiles[computer_spot] = self.computer
            if self.check_Win(computer_spot, self.computer):
                print("You lose!")
                exit()
            print("The computer has chosen " + str(computer_spot))
            print()
            self.print_Nums()
            print()
            self.print_State()






board2().play()
