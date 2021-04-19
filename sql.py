import mysql.connector as a
con=a.connect(host="localhost",user="your user name",password="*****",database="Bank")


def openAcc():
    name=input("Enter your name:")
    accno=int(input("Enter account number:"))
    dob=input("Enter D.O.B:")
    addr=input("Enter address:")
    phonenum=int(input("Enter your phone number:"))
    openingbal=int(input("Enter opening balance:"))

    data1=(name,accno,dob,addr,phonenum,openingbal)
    data2=(name,accno,openingbal)
    sql1='insert into account values (%s,%s,%s,%s,%s,%s)'
    sql2='insert into ammount values (%s,%s,%s)'
    c=con.cursor()
    c.execute(sql1,data1)
    c.execute(sql2,data2)
    con.commit()
    print("Data entered successfully...")
    main()
    


def depositAcc():
    am=int(input('Enter your amount:'))
    accno=int(input("Enter account number:"))
    a='select balance from ammount where accountno=%s'
    data=(accno,)
    c=con.cursor()
    c.execute(a,data)

    myresult=c.fetchone()
    tam=myresult[0]+am
    sql='update ammount set balance=%s where accountno=%s'
    d=(tam,accno)
    c.execute(sql,d)
    print("Ammount added successfully")
    con.commit()
    main()

def withdrawAcc():
    am=int(input('Enter your amount:'))
    accno=int(input("Enter account number:"))
    a='select balance from ammount where accountno=%s'
    data=(accno,)
    c=con.cursor()
    c.execute(a,data)

    myresult=c.fetchone()
    tam=myresult[0]-am
    sql='update ammount set balance=%s where accountno=%s'
    d=(tam,accno)
    c.execute(sql,d)
    print("Ammount withdrawed successfully")
    con.commit()
    main()
   
def balanceEn():

    accno=int(input("Enter account number:"))
    a='select balance from ammount where accountno=%s'
    data=(accno,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    print("Balace for account:",accno," is",myresult[0])
    main()

def close():
    accno=int(input("Enter account number:"))
    sql1="delete from account where accountno=%s"
    sql2="delete from ammount where accountno=%s"
    data=(accno,)
    c=con.cursor()
    c.execute(sql1,data)
    c.execute(sql2,data)
    con.commit()
    print("Account closed!!!")
    main()

def main():
    print('''
    1. OPEN ACCOUNT
    2. DEPOSIT AMOUNT
    3. WITHDRAW AMOUNT
    4. DISPLAY DETAILS
    5. DELETE ACCOUNT
    ''')
    choice=int(input("Enter your choice:"))
    if (choice==1):
        openAcc()

    elif (choice==2):
        depositAcc()

    elif (choice==3):
        withdrawAcc()

    elif (choice==4):
        balanceEn()

    elif (choice==5):
        close()

    else:
        print("Invalid choice")
        main()

main()
