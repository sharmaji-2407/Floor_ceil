

tag = 'Y'
while True:
    x=0                                                                     #removing stored values in buffer
    if(tag=='Y' or tag=="YES"):
        
            try:
                x = float(input("Please enter a float value :"))            #trying to get a value from user. If values is any thing else from a floating value. We throw a msg.
                
                print('you entered =',x)
            except Exception:
                print("Enter only floating value")
                    
            
            if(0.6 <= (x-x//1) and x <= (x//1)+1):
                print("The value =",int(x//1+1))
            if(0.0 < (x-x//1) and x-x//1<0.3999999999):
                print("The value =",int(x//1))
                
            if(0.3999999999 < x-x//1 and x-x//1 < 0.5999999):
                print("The value entered lies in mid range,\nYou can can decide which value to consider or you can let Computer to decide. \nChoose b/w \n Let Computer Decide : 1 \n Let Me decide : 2")
                
                while True:  
                    n=0     
                    try:                                       #comp user while block
                        n = int(input("Enter Your Choice : "))              #choice b/t computer and user
                    except Exception:
                        print("Enter an int only")

                    if(n==1):
                        if(0.1<(x-x//1) and (x-x//1)<0.5):
                            print("The value",int(x))
                        if(0.5<=(x-x//1) and (x-x//1)<x//1+1):
                            print("The value",int(x//1 + 1))
                        break
                    if(n==2):
                        print('\tType "min" for floor value \n\tType "max" for ceil value') 
                        
                        while True:                                             #max min while block
                            m = str(input("Enter your choice :\t"))   
                            m=m.upper()         #choice b/w max or min
                            if(m=='MIN'):
                                print("The value :",int(x//1))
                                break
                            if(m=='MAX'):
                                print("The value :",int(x//1 + 1))
                                break
                            else:                                                          #else part of max min
                                print("Enter a valid option ex: (min or max)")
                                
                        break
                    else:                                                               #else part for user comp
                        print("Enter a valid option ex: '1' to let Computer Decide or '2' to let You Decide")
                        
            

    tag = str(input("Would You like to repeat ? (Y/N) :"))
    tag=tag.upper()
    if(tag=='N' or tag=='NO'):
        break
    else:
        print("Not valid option Try again")            
            
            

