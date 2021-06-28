import sys
from getpass import getpass
from datetime import date
withdrawal_amount = 0.0
name = input('Please type your full name: ')
title = input('Type your title: ')
password = getpass('Please type a 4 digits password: ')

class Atm_operations:
    def __init__(self, name, title, password):
        self.name = name
        self.bank = 'Zenith Bank'
        self.title = title
        self.password = password
        self.balance = 10000.0
    
    

    def welcome_message(self):
        print(f'Welcome to {self.bank} {self.title} {self.name}')
        self.card_validity()


    def validate_password(self):
        password_validate = getpass('Please type your password: ')
        while password_validate != self.password:
            password_validate = getpass('Please type your password: ')
        print('You are succesfully logged in')
        self.operation_type()

    def card_validity(self):
        import datetime
        card_expiry_year = int(input('Input card expiry year: '))
        card_expiry_month = int(input('Input card expiry month: '))
        card_expiry_day = int(input('Input expiry day: '))
        current_date = date.today()
        card_date = datetime.date(card_expiry_year, card_expiry_month, card_expiry_day)
        if current_date < card_date:
            card_pin = input('Input your card pin: ')
            if card_pin[0] == '4' and len(card_pin) == 5:
                print('Your Verve card is valid')
                self.validate_password()
            elif card_pin[0] == '4' and len(card_pin) == 4:
                print('Your Visa card is valid')
                self.validate_password()
            elif card_pin[0] == '5' and len(card_pin) == 16:
                print('Your Visa card is valid')
                self.validate_password()

            else:
                print('Invalid input')
            retry = input('Type Yes to retry or No to exit: ')
            if retry == 'Yes':
                self.card_validity()
            else:
                 sys.exit('Thank you!')
        else:
            sys.exit('Sorry your card has expired!')
        

    def operation_type(self):
        import time
        print('Select 1 to check balance \n')
        print('Select 2 to withdraw cash \n')
        print('Select 3 to transfer fund \n')
        print('Select 4 to deposit cash \n')
        selected = input('Select here: ')
        if int(selected) == 1:
            print(f'Your account balance is: {self.balance-withdrawal_amount}')
            print('Select Yes to performanother transaction or No to quit')
            transaction_prompt = input('Yes/No')
            if transaction_prompt.casefold() == 'Yes':
                self.operation_type()
            else:
                print('Thank you, please take your card!')
                sys.exit()
        elif int(selected) == 2:
            withdraw = float(input('Input amount: '))
            if self.balance >= withdraw:
                print('processing, please wait...')
                time.sleep(3)
                print(f'N{withdraw} dispensed\n')
                print(f'Your balance is {self.balance-withdraw} \n')
                print('please take your card \n') 
            else:
                print('Insufficient fund')
                print('Select Yes to perform another transaction or No to quit')
                transaction_prompt = input('Yes/No')
                if transaction_prompt.casefold() == 'Yes':
                    self.operation_type()
                else:
                    print('Thank you, please take your card!')
                    sys.exit()

        elif selected == 3:
            print('Selected not available yet')
            print('Select Yes to perform another transaction or No to quit')
            transaction_prompt = input('Yes/No')
            if transaction_prompt.casefold() == 'Yes':
                self.operation_type()
            else:
                print('Thank you, please take your card!')
                sys.exit()
        elif selected == 4:
            print('Selected not available yet')
            print('Select Yes to perform another transaction or No to quit')
            transaction_prompt = input('Yes/No')
            if transaction_prompt.casefold() == 'Yes':
                self.operation_type()
            else:
                print('Thank you, please take your card!')
                sys.exit()

        else:
            print('Invalid input')
            print('Select Yes to retry and No to quit')
            transaction_prompt = input('Yes/No')
            if transaction_prompt.casefold() == 'Yes':
                self.operation_type()
            else:
                print('Thank you, please take your card!')
                sys.exit()

    #def acn_balance():


        