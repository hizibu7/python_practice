caseTypes = ["scissor", "rock", "paper"]

# Start of Answer
import random 
def GenerateRandomCaseForComputer():
    case = random.randrange(0,3)
    return case

def MakeDecision(a, b):
    if a == 'scissor':
        if b == 'scissor':
            return 'Tie'
        elif b == 'rock':
            return 'computer'
        else:
            return 'User'
        
    if a == 'rock':
        if b == 'scissor':
            return 'User'
        elif b == 'rock':
            return 'Tier'
        else:
            return 'Computer'
        
    if a == 'paper':
        if b == 'scissor':
            return 'Computer'
        elif b == 'rock':
            return 'User'
        else:
            return 'Tie'
            
    
    
# End of Answer

# Below is Execution Example, and can be removed.

userInput = 0
while True:
    userInput = int(input("\nMenu: \n[0] scissor, \n[1] rock, \n[2] paper, \n[3] quit \n\nSelect: "))
    if(userInput != 3):
        valueUser = caseTypes[userInput]
        valueComputer = GenerateRandomCaseForComputer()
        valueDecision = MakeDecision(valueUser, valueComputer)
        print("\nResult: User [{0}] vs Computer [{1}] -> Winner is {2}".format(valueUser, valueComputer, valueDecision))
    else:
        break
