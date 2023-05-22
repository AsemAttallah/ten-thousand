from game_logic import GameLogic
# rolls=[(1,2,5,1,2,1)] # specific input values as final test case
# def specific_input(x): #this function used to insert these specific numbers to make output same the final case test
#     return rolls.pop(0) if rolls else GameLogic.roll_dice(x)

def welcome():
        # Print a welcome message
    print("Welcome to Ten Thousand")

def play_or_decline():
    # Prompt the user to play or decline
    play = input("(y)es to play or (n)o to decline\n > ")

    if play.lower() == "n":
        # If the user declines, print a message and exit the program
        print("OK. Maybe another time")
        exit()
    elif play.lower() == "y":
        pass

def play_game():
    # Start round 1
    print("Starting round 1")
    round_score = 0
    total_score = 0
    round_num = 1
    remaining_dice=6 
    while True:
        # Roll 6 dice
        print(f"Rolling {remaining_dice} dice...")
        dice_roll = GameLogic.roll_dice(remaining_dice)
        print("***", " ".join(str(dice) for dice in dice_roll), "***")
    

        # Prompt the user to keep dice or quit and for avoid cheating
        while True:
            keep_dice = input("Enter dice to keep, or (q)uit:\n > ").replace(" ", "")
            if keep_dice.lower() == "q":
                print(f"Thanks for playing. You earned {total_score} points")
                exit()
            dice_to_keep = [int(die) for die in keep_dice if die.isdigit()]
            
            if not GameLogic.validate_keepers(dice_roll, dice_to_keep):
                print("Cheater!!! Or possibly made a typo...")
                print("***", " ".join(str(dice) for dice in dice_roll), "***")
                continue
            break

        # Convert the user's input to integers and keep only the digits
        dice_to_keep = [int(die) for die in keep_dice if die.isdigit()]
        
        if len(dice_to_keep)==6:
            round_score += GameLogic.calculate_score(dice_to_keep)
            remaining_dice = 6
        else: 
            round_score += GameLogic.calculate_score(dice_to_keep)
            remaining_dice -= len(dice_to_keep)

        
        if GameLogic.calculate_score(dice_to_keep)!=0:
            # Print the current round score and the number of remaining dice
            print(f"You have {round_score} unbanked points and {remaining_dice} dice remaining")

            # Prompt the user for the next action: roll again, bank points, or quit
            action = input("(r)oll again, (b)ank your points or (q)uit:\n > ")
      
            
            
        if action.lower() == "b":
            # If the user chooses to bank points
            total_score += round_score
            print(f"You banked {round_score} points in round {round_num}")
            print(f"Total score is {total_score} points")
            
            remaining_dice = 6

            round_num += 1
            round_score = 0
        
            if total_score >= 10000:
                # If the total score reaches or exceeds 10000, the game is won
                print(f"Congratulations! You reached {total_score} points. You won!")
                exit()
            print(f"Starting round {round_num}")
        elif action.lower() == "r" and GameLogic.calculate_score(dice_roll) == 0:
            print("****************************************")
            print("**        Zilch!!! Round over         **")
            print("****************************************")
            print(f"You banked 0 points in round {round_num}")
            print(f"Total score is {total_score} points")
            round_num += 1
            round_score = 0
            print(f"Starting round {round_num}")
            remaining_dice = 6
            continue
            # Start the next round
        
        elif action.lower() == "q":
            # If the user chooses to quit, print the total score and exit the program
            print(f"Thanks for playing. You earned {total_score} points")
            exit()

if __name__ == "__main__":
    welcome()
    play_or_decline()
    play_game()

