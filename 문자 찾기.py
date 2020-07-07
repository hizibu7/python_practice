def getResult(status):
    if '_' in status:
        return 'You lose'
    else:
        return 'You win'
        print('You win')

def updateStatus(Word, x, status):
    new_status = status
    if x in Word:

        for i in range(len(Word)):
            position = Word.find(x, i)
            
            if position == -1:
                continue
            
            else:
                new_status = new_status[:position]+Word[position]+new_status[position+1:]
          
    return new_status


def startGame(Word):
    count = len(Word)
    status = '_'*len(Word)
    for j in range(len(Word)):
        x = input('Enter a letter: ')
        count-=1
        print(count, 'chances')
        new_status = updateStatus(Word, x, status)
        print(updateStatus(Word, x, status))
        status = new_status
        if status == Word:
            return getResult(status)
            break
        if count == 0:
            return getResult(status)
            break

Word = 'HIPPOPOTAMUS'    # This cell is for your confirmation, can be removed.
result = startGame(Word) # If correctly implemented, the result should be 
print(result)       
