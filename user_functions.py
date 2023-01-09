import mysql.connector as con
import random

"""Inserting Booking details into status table"""

def confirm_Book_ticket(no,name,source,dest,cost,count,key):
    mydb = con.connect(
        host="localhost",
        user="root",
        password="52828378Jyo#",
        database="raildb"
    )
    cur = mydb.cursor()

    #inserting user inputs into bookstatus table
    sql ="INSERT INTO bookstatus(trainno,trainname,sourcestation,destinationstation,cost,seats,ticketno) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    val = (no,name,source,dest,cost,count,key)
    cur.execute(sql,val)
    mydb.commit()
    mydb.close()
    print("\t\t\tTicket Booking Confirmed")
    print("\n\n\n")

"""Bokking a railway Ticket"""

def book_ticket():
    global tr_cost, tr_name, tr_no, tr_source, tr_dest, totalcost
    stationlist = ["Trivandrum","Kollam Jn","Pathanamthitta","Kottayam","Alappuzha","Ernakulam Jn","Thrissur","Shornnur","Malappuram","Kozhikkode","Kannur","Kasargod"]
    print("\nList of trains")
    print("*******[",end= "")
    for x in stationlist:
        print(x, end= "---")
    print("]*******")
    source = input("\n\n\t\t\tEnter the the source station :")
    destination = input("\t\t\tEnter the destination station: ")
    mydb = con.connect(
      host="localhost",
      user="root",
      password="52828378Jyo#",
      database="raildb"
    )

    cur = mydb.cursor()
    sql = "Select trainno, trainname, departuretime, arrivaltime, cost from traindata WHERE sourcestation = %s and destinationstation = %s "
    sour = (source,destination)
    cur.execute(sql,sour)
    result = cur.fetchall()

    for x in result:
        print("\n\n\t\t\t|******************************|")
        print(f"\t\t\t|Train No:                {x[0]}|\n\t\t\t|Train Name:{x[1]}   |\n\t\t\t|  {x[2]}-----------------{x[3]} | \n\t\t\t|    Ticket Price :{x[4]}          |\n\t\t\t|******************************|")
        tr_no = x[0]
        tr_name= x[1]
        tr_source = x[2]
        tr_dest = x[3]
        tr_cost = x[4]
    mydb.close()

    count = int(input("\n\n\t\t\tHow many tickets you want : "))
    p = int(input("\n\t\t\tWhich one do you prefer \n\n\t\t\t1.General 2.Chaircar 3.Sleeper 4.AC coach \n\t\t\tEnter your choice : "))
    print()
    if p == 1:
        print(f"\t\t\tTicket price: {tr_cost}\n")
        totalcost = tr_cost * count
        print("\t\t\tTotal charges for ",count," seats is ",totalcost)
    elif p == 2:
        print(f"\t\t\tTicket price: {tr_cost + 10}\n")
        totalcost = (tr_cost + 10) * count
        print("\t\t\tTotal charges for ",count," seats is ",totalcost)
    elif p ==3 :
        print(f"\t\t\tTicket price: {tr_cost + 20}\n")
        totalcost = (tr_cost+ 20) * count
        print("\t\t\tTotal charges for ",count," seats is ",totalcost)
    elif p ==4 :
        print(f"\t\t\tTicket price: {tr_cost + 50}\n")
        totalcost = (tr_cost + 50 )* count
        print("\t\t\tTotal charges for ",count," seats is ",totalcost)
    else:
        pass

    user_prompt = input("\t\t\tDo you wish to continue?Press y \n\t\t\tPress n to exit:")
    if user_prompt == "n" or user_prompt =="N":
        print("\n\t\t\tProcess Terminated")
        print("\n\n\n")
    elif user_prompt == "y" or user_prompt =="Y":
        ticket_no = random.randint(10000,99999)
        print("\n\n\t\t\tTicket no : ",ticket_no)
        print()
        confirm_Book_ticket(tr_no,tr_name,tr_source,tr_dest,totalcost,count,ticket_no)

"""Cancelling the ticket"""

def cancel_ticket(no):
    mydb = con.connect(
        host="localhost",
        user="root",
        password="52828378Jyo#",
        database="raildb"
    )

    cur = mydb.cursor()
    sql = ("DELETE FROM bookstatus WHERE ticketno = %s")
    val = (no,)
    cur.execute(sql,val)
    mydb.commit()
    print("\t\t\tThe ticket has been cancelled!!")
    print("\n\n\n")

"""Viewing ticket status"""

def ticket_status(no):
    mydb = con.connect(
        host="localhost",
        user="root",
        password="52828378Jyo#",
        database="raildb"
    )

    cur = mydb.cursor()
    cur.execute(f"SELECT trainno,trainname,sourcestation,destinationstation,cost,seats,ticketno FROM bookstatus WHERE ticketno = {no}")
    val = cur.fetchall()
    for x in val:
        print("\t\t\t|***************************************************|")
        print(f"\t\t\t|Train no: {x[0]}\t\t Train Name:{x[1]}|\n\t\t\t|Start Time: {x[2]}\t\t\tEnd Time :{x[3]}\t\t\t|\n\t\t\t|Ticket Price : {x[4]}\t\t\t  Seats: {x[5]}\t\t\t\t|\n\t\t\t|Ticket No: : {x[6]}\t\t\t\t\t\t\t\t\t|")
        print("\t\t\t|***************************************************|")
        print("\n\n\n")
    mydb.close()






