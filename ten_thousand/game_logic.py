import random 

class GameLogic: 
    '''
    This is class contain the logic of roll dice 10,000
    '''
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
        
        if dice_roll.count(1) == 6: # this if statement used to check the counts of (1) is equal 6 repetition
            score += 4000

        elif counts[1] >= 3: # if above condition not true, elif statement will check the counts of (1) is grater than or equal 3 repetition
            score += 1000

        else:  # if above condition not true elif statement will be excuted
            score += counts[1] * 100

        if counts[5] < 3: #this if statement used to check the counts of (5) is less than 3 repetition
            score += counts[5] * 50
        
        for i in range(len(dice_roll)): # this for loop used to add scores in specific conditions
            if dice_roll[i] > 1: # this if statement used to check value is grater than 1
                if counts[dice_roll[i]] == 3: # if above condition true if statement will if the counts is equal 3 repetition
                    score +=(dice_roll[i]*100)
                    return score
                elif counts[dice_roll[i]] >3: # if above condition not true elif statement will check if the counts is greater 3 repetition
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

    