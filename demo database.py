import mysql.connector

mydb = mysql.connector.connect(host='localhost',password='Manoj@2001',user='root',database='information')

mycursor =mydb.cursor()
def option():
        print("\n","1.REGISTER","\n","2.LOGIN","\n")
        choice=int(input("Enter your choice:"))
        if(choice==1):
            registration()
        elif(choice==2):
            login()
        else:
            print("Invalid Entry") 
def registration():
    global Username
    global Password
    global phno
    global upi
    Username=input("User Name: ")
    Password=input("Password: ")
    phno=input("phno: ")
    upi=int(input("UPI pin: "))
    sql='insert into registration_details(name,password,phoneno,upipin) values(%s,%s,%s,%s)'
    t=(Username,Password,phno,upi)
    mycursor.execute(sql,t)
    mydb.commit()
def login():
    global Username
    global Password
    Username=input("User Name: ")
    Password=input("Password: ")
    name='select name from registration_details'
    mycursor.execute(name)
    result=mycursor.fetchall()
    for i in result:
         if i==name:
              print("yes")
    
         
          
              
              
    '''password= 'select password from registration_details'
    mycursor.execute(password)
    if(Username==name and Password==password):
         print('logged in successfully')'''


option()

