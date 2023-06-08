import csv
import re
class home:
    def __init__(self):
        pass
    def option(self):
        print("\n","1.REGISTER","\n","2.LOGIN","\n")
        choice=int(input("Enter your choice:"))
        if(choice==1):
            obj_home.register()
        elif(choice==2):
            obj_home.login()
        else:
            print("Invalid Entry") 
    def register(self):
        print("\n","----Registration Details----")
        Name=input("User Name: ")
        password=input("Password: ")
        '''condition="^(?=.[a-z])(?=.[A-Z])(?=.\d)(?=.[@$!%#?&])[A-Za-z\d@$!#%?&]{8,11}$"
        check=re.findall(condition,password)
        if check!=None:
            print("Enter a strong password of minimum 8 characters with capital letters and special characters")
            password=input("Password: ")'''
        r=re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', password)
        if r==None:
            print("Enter a strong password of minimum 8 characters with capital letters and special characters")
            password=input("Password: ")
        global user
        flag=True
        with open('User_details.csv','r') as file:
            user=csv.reader(file)
            for line in user:
             if(line[0]==Name and line[1]==password):
                print("\nOops!! User name or password already exsist.Please try again")
                obj_home.register() 
                flag=False 
        if flag==True:
            phone_no=(input("Phone number: "))
        r=re.fullmatch('[6-9][0-9]{9}',phone_no)
        if r==None:
            print("\nInvalid Phone No. Enter a valid Phone No")
            phone_no=(input("Phone number: "))
        Accnt_no=(input("Account number: "))
        r=re.fullmatch('[1-9][0-9]{9,18}',Accnt_no)
        if r==None:
            print("\nInvalid Account No. Enter a valid Account No")
            Accnt_no=(input("Account number: "))
        UPI_Pin=(input("Set UPI PIN(6 digits): "))
        r=re.fullmatch('[0-9][0-9]{5}',UPI_Pin)
        if r==None:
            print("\nInvalid UPI PIN. Enter a valid UPI PIN")
            UPI_Pin=(input("Set UPI PIN(6 digits): "))
        print("\nRegistration successful")
        l=[]
        l.append(Name)
        l.append(password)
        l.append(phone_no)
        l.append(Accnt_no)
        l.append(UPI_Pin)
        with open('User_details.csv','a',newline="") as file:
            user= csv.writer(file)
            user.writerow(l)
        obj_home.login()     
    def login(self):
        print("\n","----Login details----")
        Username=input("User Name: ")
        Password=input("Password: ")
        flag=True
        with open('User_details.csv','r') as file:
            user=csv.reader(file)
            for line in user:
                if(line[0]==Username and line[1]==Password):
                    print("\nLogged in sucessfully as",Username,"\n--------WELCOME TO EASY PAY--------")
                    flag=False
            if flag==True:
                print("\n","Invalid User name or Password Tryagain","\n")
                obj_home.login()
obj_home=home()
obj_home.option()


