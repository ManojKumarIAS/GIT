import csv
import re
class moneytransfer:
    def __init__ (self):
        pass
    def Transcation(self):
        print("Transfer fund:","\n","1.via Mobile number","\n","2.via User name","\n","3.via Accnt number","\n")
        option=int(input("Enter the choice:"))
        if (option==1):
            obj_transfer.mobile_number()
        elif(option==2):
            obj_transfer.User_name()    
        elif(option==3):
            obj_transfer.Accnt_no()
        else:
            print("Invalid Entry")
    def mobile_number(self):
        global upi_pin
        global sender_uname
        global amount
        mobile_number=(input("Receiver's Mobile no: "))
        for r in range(10):
            r=re.fullmatch('[6-9][0-9]{9}',mobile_number)
            if r==None:
                print("\nInvalid Phone No. Enter a valid Phone No")
                mobile_number=(input("Receiver's Mobile no: "))
        amount=input("Amount: ")
        obj_transfer.amount()
        upi_pin=input("Enter UPI Pin: ")
        sender_uname=input("Enter User name: ")
        obj_transfer.check()
    def User_name(self):
        global upi_pin
        global sender_uname
        global amount
        user_name=(input("Receiver's User name: "))
        amount=(input("Amount: "))
        obj_transfer.amount()
        upi_pin=input("Enter UPI Pin: ")
        sender_uname=input("Enter User name: ")
        obj_transfer.check()
    def Accnt_no(self):
        global upi_pin
        global sender_uname
        global amount
        Accnt_no=(input("Receiver's Accnt no: "))
        for r in range(10):
            r=re.fullmatch('[1-9][0-9]{9,18}',Accnt_no)
            if r==None:
                print("\nInvalid Account No. Enter a valid Account No")
                Accnt_no=(input("Account number: ")) 
        amount=(input("Amount: "))
        obj_transfer.amount()
        upi_pin=input("Enter UPI Pin: ") 
        sender_uname=input("Enter User name: ")
        obj_transfer.check() 
    def amount(self):
        global amount
        for r in range(10):
            r=re.fullmatch('[1-9][0-9]{1,3}',amount)
            if r==None:
                print("\nExceeding the limit")
                amount=(input("Amount: "))
    def check(self):
        with open('user_details.csv','r') as file:
            user=csv.reader(file)
            flag=True
            for line in user:
                if (upi_pin == line[4] and sender_uname==line[0] ):
                    print("\nAmount transfered successfully!!")
                    print("\n1.Transfer money again","\n2.Log out")
                    option=int(input("\nEnter the choice:"))
                    if(option==1):
                       obj_transfer.Transcation() 
                    elif(option==2):
                        print("\nLogged out","\nThank you for using Easy Pay")
                        exit()
                    flag=False
            if flag==True:
                print("\nInvalid upi pin or user name\n")
                obj_transfer.Transcation()
obj_transfer=moneytransfer()
