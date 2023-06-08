import csv
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
        mobile_number=(input("Receiver's Mobile no: "))
        amount=input("Amount: ")
        upi_pin=input("Enter UPI Pin: ")
        sender_uname=input("Enter User name: ")
        obj_transfer.check()
    def User_name(self):
        global upi_pin
        global sender_uname
        user_name=(input("Receiver's User name: "))
        amount=(input("Amount: "))
        upi_pin=input("Enter UPI Pin: ")
        sender_uname=input("Enter User name: ")
        obj_transfer.check()
    def Accnt_no(self):
        global upi_pin
        global sender_uname
        Accnt_no=(input("Receiver's Accnt no: "))
        amount=(input("Amount: "))
        upi_pin=input("Enter UPI Pin: ") 
        sender_uname=input("Enter User name: ")
        obj_transfer.check() 
    def check(self):
        with open('User_details.csv','r') as file:
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
                    flag=False
            if flag==True:
                print("\nInvalid upi pin or user name\n")
                obj_transfer.Transcation()

obj_transfer=moneytransfer()
obj_transfer.Transcation()