class BankAccount:  
    account_number = 1000
    def __init__(self,name , curr_balance):
      self.name = name
      self.curr_balance = curr_balance
      BankAccount.account_number +=1
      self.account_number = BankAccount.account_number


    def deposit(self,amount):
     self.amount = amount
     if amount >0:
        self.curr_balance +=amount
     else:
        print("not valid amount")

    def withdraw(self,amount):
     self.amount = amount
     if amount<=self.curr_balance:
      self.curr_balance -=amount
     else :
        print("insufficent balance")
    
    def show(self):
        return print(f"{self.curr_balance}")





class Bank:
       def __init__(self):
          self.accounts = []

       def create_account(self,name,balance):
          account = BankAccount(name,balance)

          self.accounts.append(account)
          print(f"your account is created {BankAccount.account_number}")
          return account

       def find_account(self,account_no):
          
          for acc in self.accounts:
               if acc.account_number == account_no:
                  return acc
               else:
                     print("not found")

       def transfer(self,from_acc , to_acc, amount):
          sender = self.find_account(from_acc)
          reciver = self.find_account(to_acc)
       
          if sender and reciver :
            if sender.curr_balance >= amount:
                sender.curr_balance -=amount
                reciver.curr_balance +=amount
                print("sussecfully transfer")
          else:
            
            print("insufficent balance")
 


b = BankAccount("deepanshu" , 1000)
b.show()
b.deposit(500)
b.show()


bank = Bank()
c = bank.create_account("himanshu" , 10000)

c.show()
bank.accounts.append(b)
bank.transfer(c.account_number,b.account_number,5000)

c.show()