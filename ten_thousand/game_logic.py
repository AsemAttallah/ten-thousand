import random 

class GameLogic: 
    '''
    This is class contain the logic of roll dice 10,000
    '''
    @staticmethod
    def get_scorers(dice):
        all_dice_score = GameLogic.calculate_score(dice)
        if all_dice_score == 0:
            return tuple()
        scorers = []
        for i, val in enumerate(dice):
            sub_roll = dice[:i] + dice[i+1:]
            sub_score = GameLogic.calculate_score(sub_roll)
            if sub_score != all_dice_score:
                scorers.append(val)
        return tuple(scorers)
    
    @staticmethod # this command use to make the calculate_score method just accessible from GameLogic class
    def calculate_score(dice_roll): # this method used to calculate the score in the game 
        '''
        This method to calculate the scores
        '''
        score = 0  # initial value for score in the game
        counts = [0] * 7  # Initialize counts for each dice value
        
        for dice in dice_roll: # this for loop used calculate count of each random number in dice_roll tuple
            counts[dice] += 1  # this command used to add one count for each repeated value
            
        if all(counts[dice] == 1 for dice in range(1, 7)): # this if statement used to check if all values have one repetition                               
            score += 1500
            return score
        
        elif len(set(dice_roll)) == 3 and all(dice_roll.count(dice) == 2 for dice in set(dice_roll)): # this line of code used to check if we have 3 pairs of values if true will add 1500 score
            score += 1500 
            return score

        elif counts[1] >= 3: # if above condition not true, elif statement will check the counts of (1) is grater than or equal 3 repetition
            score += (counts[1]-2)*1000

        else:  # if above condition not true elif statement will be excuted
            score += counts[1] * 100

        if counts[5] < 3: #this if statement used to check the counts of (5) is less than 3 repetition
            score += counts[5] * 50
        
        for i in range(len(dice_roll)): # this for loop used to add scores in specific conditions
            if dice_roll[i] > 1: # this if statement used to check value is grater than 1
                if counts[dice_roll[i]] >=3: # if above condition not true elif statement will check if the counts is greater than or equal 3  repetition
                    score +=(counts[dice_roll[i]]-2)*(dice_roll[i]*100)
                    return score

        return score # this command to return the value that calculate_score method find it
    @staticmethod  # this command used to make the roll_dice method just accessible from GameLogic class
    def roll_dice(num_dice):
        '''
        This method to calculate random number 
        '''
        dice_roll = tuple(random.randint(1, 6) for _ in range(num_dice)) # In this variable we calculate 6 random number and add it to tuple 
        return dice_roll
    
    @staticmethod
    def validate_keepers(roll, keepers):
        '''
        this method help us to check ther is a cheating or not by checking if all selected value is include the random dices or not
        '''
        roll_counts = {die: roll.count(die) for die in set(roll)}
        keepers_counts = {die: keepers.count(die) for die in set(keepers)}
        for die, count in keepers_counts.items():
            if count > roll_counts.get(die, 0):
                return False
        return True
    
    
    def is_zilch(keepers):
        '''
        this method help us to check if score equal zero to appear a zilch message
        '''
        return GameLogic.calculate_score(keepers) == 0
    
    

