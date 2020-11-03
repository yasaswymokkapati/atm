class Atm:
    def __init__(self, cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin
    
    def check_balance(self):
        pin = input('Enter your pin')
        print('Your balance is 100/-')
    
    def withdrawal(self, amount):
        new_amount = 100 - amount
        if(new_amount < amount):
            print('You do not have enough balance')
        else:
            print('You have withdrawed ' + str(amount) + '/-')
            print('You currently have ' + str(new_amount) + '/- in your account')

def main():
    card_number = input('Insert your card number')
    pin_num = input('Enter your pin (Do not show this to anyone. Cover it with your hands)')
    new_user = Atm(card_number, pin_num)
    print('Choose the options')
    print('1) Balance Enquiry 2) Withdrawal')
    activity = int(input('Enter activity number'))
    if(activity == 1):
        new_user.check_balance()    
    elif (activity == 2):
        amount = int(input('Enter the amount'))
        new_user.withdrawal(amount)
    else :
        print('Enter a valid number')
main()
Atm = Atm(main().card_number, main().pin_num)

