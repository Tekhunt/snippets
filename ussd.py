"""
Scope of work:
    USSD self service assignment
    Requirements
    Buy airtime
    Check balance
    Transfer fund between Nigeria numbers
    Constaints
    Collect only Nigeria numbers
    Balance must reflect the correct value after each operation.
"""

import sys
purchase_amount = 0
transfer_amount = 0
initial_amount = 5000
airtime_balance =  initial_amount + purchase_amount - transfer_amount
def welcome():
    print('Hi decadev! Welcome to Decagon USSD self-service\n')
    t_code()

def t_code():
    option = input('Please dial *128# to access your self service options: ')
    if option == '0':
        sys.exit('Thank you for choosing Decagon!')
    while option != '*128#':
        print('Please type correct values')
        option = input('Please dial *128# to access your self service options: ')
    ussd_services()


def ussd_services():
    print('Select 1 to buy airtime \n')
    print('Select 2 to check airtime balance \n')
    print('Select 3 to transfer airtime \n')
    services = input('Select here: ')

    if services =='1':
        buy_airtime()
    elif services == '2':
        checkBalance()
    elif services == '3':
        transfer_airtime()
    else:
        print('Invalid input! Type Yes to retry or No to quit')
        loop = input(':')
        if loop == 'Yes':
            ussd_services()
        else: 
            sys.exit('Thank you for choosing Decagon!')

purchase_amount = 0
def buy_airtime():
    global airtime_balance
    global purchase_amount
    purchase_amount = int(input('Input amount: '))
    print(f'Congratulations! Your account has been credited with N{purchase_amount}')
    airtime_balance =  initial_amount + purchase_amount - transfer_amount
    loop2 = input('Select 4 to perform another or press any other key to exit: ')
    if loop2 == '4':
        ussd_services()
    else:
        sys.exit('Thank you for choosing Decagon!')

#airtime_balance =  initial_amount + purchase_amount - transfer_amount

def checkBalance():
    global airtime_balance
    #airtime_balance =  initial_amount + purchase_amount - transfer_amount
    airtime_balance =  initial_amount + purchase_amount - transfer_amount
    print(f'Your airtime balance is: {airtime_balance}')
    loop3 = input('Select 5 to perform another or press any other key to exit: ')
    if loop3 == '5':
        ussd_services()
    else:
        sys.exit('Thank you for choosing Decagon!')

def transfer_airtime():
    global transfer_amount
    global airtime_balance
    transfer_amount = int(input('Please type amount: '))
    recipient_number = input("Please type reciever's number: ")
    while type(transfer_amount) != int:
        print('Please input correct amount')
        transfer_amount = int(input('Please type amount: '))
    if ((recipient_number[:4] == '+234' or len(recipient_number) == 14) or (len('+234' + str(recipient_number[1:])) == 14) and [i for i in ['080', '081', '070', '090', '091'] if i == recipient_number[0:3]]) and transfer_amount <= airtime_balance:
        print(f'{transfer_amount} has been transfered to {recipient_number}') 
        airtime_balance =  initial_amount + purchase_amount - transfer_amount
        # additional code
        loop4 = input('Select 6 to perform another or press any other key to exit: ')
        if loop4 == '6':
            ussd_services()
        else:
            sys.exit('Thank you for choosing Decagon!')
    else:
        print('Input not recognised')
        loop5 = input('type 7 to retry and type any other key to exit quit: ')
        if loop5 == '7':
            ussd_services()
        else:
            sys.exit('Thank you for choosing Decagon')

