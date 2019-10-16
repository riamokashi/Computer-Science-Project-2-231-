
###################################################################
# take in code, miles, and days 
#
# convert odometer miles to actual miles 
#
#loop through while statement to keep updating the amount due 
#
#Have a final amount due for the user to easily access 
###################################################################


BANNER = "\nWelcome to car rentals. \
\n\nAt the prompts, please enter the following: \
\n\tCustomer's classification code (a character: BDW) \
\n\tNumber of days the vehicle was rented (int)\
\n\tOdometer reading at the start of the rental period (int)\
\n\tOdometer reading at the end of the rental period (int)" 
PROMPT = '''\nWould you like to continue (Y/N)? '''
print(BANNER)
in_str = input(PROMPT)




while in_str == 'Y':
    CODE = input("\nCustomer code (BDW): ")
    while CODE != 'B' and CODE != 'b' and CODE != 'D' and CODE != 'd' and CODE != 'W' and CODE != 'w':#need to do this in order to have correctr wrong inputs
        print("\n\t*** Invalid customer code. Try again. ***")
        CODE = input("\nCustomer code (BDW): ")
    DAYS = input("\nNumber of days: ")
    DAYS_INT = int(DAYS) # change to int so that the math will be possible (done to all inputs)
    DAYS = str(DAYS)
    O_START = input("Odometer reading at the start: ")
    O_START_INT = int(O_START)
    O_START = str(O_START)
    O_END = input("Odometer reading at the end:   ")
    O_END_INT = int(O_END)
    O_END = str(O_END)
    MILES = ((int(O_END) / 10) - (int(O_START) / 10))
    MILES_INT = round(MILES, 1)
    if CODE == 'B' or CODE == 'b': # calculations for B 
        O_OVER = 1000000 - O_START_INT
        if O_OVER <= 10: # must do this if the ODOMETER is about to reset 
            MILES_OVER = float((O_END_INT + O_OVER)/10)
            BASE_AMOUNT = (40 * DAYS_INT) 
            MILES_AMOUNT = (.25 * MILES_OVER)
        else:
            BASE_AMOUNT = (40 * DAYS_INT) 
            MILES_AMOUNT = (.25 * MILES) 
    elif CODE == 'D' or CODE == 'd': # calculations for D 
        A_MILES = MILES_INT/DAYS_INT
        if A_MILES < 100:
            BASE_AMOUNT = (60*DAYS_INT)  
            MILES_AMOUNT = 0
        else:
            BASE_AMOUNT = (60*DAYS_INT)
            MILES_AMOUNT = (.25*(MILES_INT - (DAYS_INT*100)))
    elif CODE == 'W' or CODE == 'w': # calculations for W
        WEEKS = int((DAYS_INT/7))
        if (DAYS_INT % 7) == 0:
            WEEKS = round(WEEKS) # must round weeks to an integer if it is divisible by 7
        else:
           WEEKS = round(WEEKS) + 1 # must round weeks up if it goes over 7 weeks 
        if (MILES_INT/WEEKS) <= 900: # use the updated value for weeks to complete calculations for W
            BASE_AMOUNT = (190*WEEKS)
            MILES_AMOUNT = 0
        elif (MILES_INT/WEEKS) <= 1500:
            BASE_AMOUNT = ((100)*(WEEKS) + (190*WEEKS))
            MILES_AMOUNT = 0
        else:
            BASE_AMOUNT =  190*(WEEKS)
            MILES_AMOUNT = ((200*(WEEKS)) + (.25*(MILES_INT - ((WEEKS)*1500))))
    AMOUNT_DUE = BASE_AMOUNT + MILES_AMOUNT # the update the amount due based on calculations in the if statement 
    AMOUNT_DUE = round(AMOUNT_DUE, 2) # round the amount so that it is payable in dollars and cents 
    
    # print the customer summary 
    
    print("\nCustomer summary:")
    print("\tclassification code: " + CODE)
    print("\trental period (days): " + DAYS)
    print("\todometer reading at start: " + str(O_START_INT))
    print("\todometer reading at end:   " + str(O_END_INT))
    if CODE == 'B': # if the odometer is about to reset, there are 2 values of the total amount of miles 
        print("\tnumber of miles driven:  " + str(MILES_OVER)) # both values are taken into account in the if statement block 
    else:
       print("\tnumber of miles driven:  " + str(MILES_INT))
    print("\tamount due: $ " + str(float(AMOUNT_DUE)))  
    in_str = input(PROMPT)
else:
    print('Thank you for your loyalty.') # print this if the user inputs N 
    
    
    
    
        






