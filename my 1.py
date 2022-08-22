totel_amount=0
x = True
while x is True:

    
    ex = True
    while ex is True:                  
        try:                             
            balance = int(input('add the amount\n  '))
            totel_amount += balance                
            ex = False                                            
        except ValueError:
            print('please try again with some integer value')
            ex= True                       
        print('your totel amount is', totel_amount)

        while True:
            ans = input('do you want to add more? yes or no\n')
            if ans.lower() == 'yes':
                
                ex = True
            
                x = True
                break
            elif ans.lower()== 'no':
                
                x= False
                break
            else:
                print('please enter a valid choice')
    print('this is your totel amount in hand ', totel_amount)

    while True:
        de = input('do you want to decrease the amount\n')
        if de.lower() == 'yes':
            try:
                deq =int(input('how much you want to decrease ?\n'))
                totel_amount -= deq
                print('this is the decreased amount', totel_amount)
            except ValueError:
                
                print('please try again with some integer value')
                True
                
        elif de.lower() == 'no':
            print(f'{totel_amount} balance available' )
            x= False
            break
            
        
        else:
            print('please enter a valid choice')
            
            

