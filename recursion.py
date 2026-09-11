def countdown(i): #this case of recursion is infinite
    print(i)
    countdown(i-1) 

#countdown(5) # uncomment this section to see the recursion

def countdown2(i): 
    print(i)
    if i <= 0: # base case. it includes where the recursion stops
        return
    else: # recursive case. it says to keep going 
        countdown2(i-1)

countdown2(12)