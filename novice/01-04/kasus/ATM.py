class Deposit:
    deposit = 0
    def __init__(self):
        print()

    def setDeposit(self, d):
        Deposit.deposit = d
    
    def getDeposit(self):
        return deposit
    
class Withdraw:
    withdraw = 0 
    def __init__(self):
        print()  

    def setWithdraw(self, w):
        Withdraw.withdraw = w
    
    def getWithdraw(self):
        return withdraw


class BalanceInquiry:

    balance = 0
    def __init__(self):
        print()

    def setBalance(self, b):
        BalanceInquiry.balance = b
    
    def getBalance(self):
        return balance


class ATMMachine(Deposit, Withdraw, BalanceInquiry):
    # saldo = 10000
    def checkBalance(self):
    
        print("\tYour current balance is " + BalanceInquiry.getBalance())
    
   
    def withdrawMoney(self):
    
        if BalanceInquiry.balance == 0:
        
            print("\tYour current balance is zero.")
            print("\tYou cannot withdraw!")
            print("\tYou need to deposit money first.")

        elif BalanceInquiry.balance <= 500:
        
            print("\tYou do not have sufficient money to withdraw")
            print("\tChecked your balance to see your money in the bank.")
        
        elif Withdraw.withdraw > BalanceInquiry.balance:
        
            print("\tThe amount you withdraw is greater than to your balance")
            print("\tPlease check the amount you entered.")
    
                   
    def depositMoney(self):
    
        print("\tYou deposited the amount of " + Deposit.getDeposit())
    
   
    def __init__(self):
    
        
        select = 0
        choice = 0
       
        print("====================================================")
        print("\tWelcome to this simple ATM machine")
        print("====================================================")
        print()

        
        while select <= 4:
            try :
                    print("\tPlease select ATM Transactions")
                    print("\tPress [1] Deposit")
                    print("\tPress [2] Withdraw")
                    print("\tPress [3] Balance Inquiry")
                    print("\tPress [4] Exit")
               
                    print("\n\tWhat would you like to do? ")

                    select = int(input("select your choice "))
   
                    if select == 1:
                        print("\n\tEnter the amount of money to deposit: ")                        
                        Deposit.deposit = int(input(""))                        
                        BalanceInquiry.balance = Deposit.deposit + BalanceInquiry.balance                    
                        print("Your Balance :",BalanceInquiry.balance)
                               
                    elif select == 2:         
                        print("\n\tTo withdraw, make sure that you have sufficient balance in your account.")
                        print()
                        print("\tEnter amount of money to withdraw: ")
                        Withdraw.withdraw = int(input(""))
                        ATMMachine.withdrawMoney(Withdraw.withdraw)
                        balance = BalanceInquiry.balance - Withdraw.withdraw
                        print("Your Balance :",balance)
                               
                    elif select == 3:
                        print("Your Balance :",BalanceInquiry.balance)

                    elif select == 4:
                        print("\n\tTransaction exited.")
                        break
                    
                    elif select > 4:
                        print("\n\tPlease select correct transaction.")
                                
                 
                    try:
                        print("\n\tWould you like to try another transaction?")
                        print("\n\tPress [1] Yes \n\tPress [2] No")
                        print("\tEnter choice: ")
                        choice = int(input("Enter Your Transaction :"))

                        if choice == 1:
                            print("Please Enter Your Transaction")
                        
                        elif choice == 2:
                            print("Thank You, Have A Nice Day")
                            break
                        else:
                            print("\n\tPlease select correct choice.")
                        
                    
                   
                    except:
                        print("\tError Input! Please enter a number only.")
                        choice = int(input(""))
                        print("\tEnter yout choice:",choice)
                        
                    
            except:
                print("Enter your correct choice")
                

       
atm1 = ATMMachine()

print("\n\tThank you for using this ATM")