def collatz(number):
    if (int(number) % 2) == 0:
        return (int(number) // 2)
    if (int(number) % 2) != 0:
        return (3 * int(number) + 1)
    

print ('Enter a number.')
number = input()
while True:
    if collatz(number) != 1:
        print (collatz(number))
        number = collatz(number)
    elif collatz(number) == 1:
        print (collatz(number))
        break
    
        
    
    
    
   
    
    
    
        

    
