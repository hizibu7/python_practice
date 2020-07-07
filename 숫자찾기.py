import random
rand = random.randrange(0,101)
list1 = []
list2 = []
while True:
    print(rand)
    ans = int(input())
    
    if ans == 2:
        list1.append(rand)
        
        if len(list2)<2:
            rand = random.randrange(0, min(list1))

        else:
            rand = random.randrange(max(list2), min(list1))
            
    
    elif ans == 0:
        list2.append(rand)

        if len(list1)<2:
            rand = random.randrange(max(list2), 101)
        else:
            rand = random.randrange(max(list2), min(list1))

        
    elif ans == 1:
        print("Correct")
        break
