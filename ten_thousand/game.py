from ten_thousand.game_logic import GameLogic

rolls=[] # specific input values as final test case
def specific_input(x): #this function used to insert these specific numbers to make output same the final case test
    return rolls.pop(0) if rolls else GameLogic.roll_dice(x)

class Game():
    def welcome():
        # Print a welcome message
        print("Welcome to Ten Thousand")
    def play_or_decline():
        # Prompt the user to play or decline
        print("(y)es to play or (n)o to decline")
        play = input("> ")
        if play.lower() == "n":
            # If the user declines, print a message and exit the program
            print("OK. Maybe another time")
            exit()
        elif play.lower() == "y":
            pass
    
    @staticmethod
    def play():
        '''
        this method to play the game
        '''
        Game.welcome()
        Game.play_or_decline()
    # Start round 1
        print("Starting round 1")
        round_score = 0
        total_score = 0
        round_num = 1
        remaining_dices=6
        while True:
             # Roll 6 dice
            print(f"Rolling {remaining_dices} dice...")
            dice_roll = specific_input(remaining_dices)
            var1=(" ".join(str(dice) for dice in dice_roll))
            print(f"*** {var1} ***")
            if GameLogic.is_zilch(dice_roll):
                print("****************************************")
                print("**        Zilch!!! Round over         **")
                print("****************************************")
                print(f"You banked 0 points in round {round_num}")
                print(f"Total score is {total_score} points")
                round_num += 1
                round_score = 0
                print(f"Starting round {round_num}")
                remaining_dices = 6
                continue
            while True:
                print("Enter dice to keep, or (q)uit:")
                keep_dice = input("> ").replace(" ", "")
                if keep_dice.lower() == "q" or round_num > 20:
                    print(f"Thanks for playing. You earned {total_score} points")
                    exit()
                dice_to_keep = [int(die) for die in keep_dice if die.isdigit()]
                if not GameLogic.validate_keepers(dice_roll, dice_to_keep):
                    print("Cheater!!! Or possibly made a typo...")
                    var2=(" ".join(str(dice) for dice in dice_roll))
                    print(f"*** {var2} ***")
                    continue
                break
            # Convert the user's input to integers and keep only the digits
            dice_to_keep = [int(die) for die in keep_dice if die.isdigit()]
            if len(dice_to_keep)==6:
                round_score += GameLogic.calculate_score(dice_to_keep)
                remaining_dices = 6
            else:
                round_score += GameLogic.calculate_score(dice_to_keep)
                remaining_dices -= len(dice_to_keep)
            if GameLogic.calculate_score(dice_to_keep)!=0:
                # Print the current round score and the number of remaining dice
                print(f"You have {round_score} unbanked points and {remaining_dices} dice remaining")
                # Prompt the user for the next action: roll again, bank points, or quit
                print("(r)oll again, (b)ank your points or (q)uit:")
                action = input("> ")
            if action.lower() == "b":
                # If the user chooses to bank points
                total_score += round_score
                print(f"You banked {round_score} points in round {round_num}")
                print(f"Total score is {total_score} points")
                remaining_dices = 6
                round_num += 1
                round_score = 0
                print(f"Starting round {round_num}")
                # Start the next round
            elif action.lower() == "q":
                # If the user chooses to quit, print the total score and exit the program
                print(f"Thanks for playing. You earned {total_score} points")
                exit()


if __name__ == "__main__":
    Game.play()