import user_functions
con_in = "y"

"""User interface"""

while con_in == "y" or con_in =="Y":
    print("\t\t\t\t\t\t\t\t\t\t\t\t\tINDIAN RAILWAY TICKET RESERVATION SYSTEM")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t****************************************")
    print("\n\n\t\t1. Ticket Booking")
    print("\t\t2. Ticket Canceling")
    print("\t\t3. Booked ticket Status")
    print("\t\t4. Exit")
    input1 = int(input("\n\n\t\tEnter your choice :"))

#checking user input
    if input1 == 1:
        user_functions.book_ticket()
        #passing to booking function

        # check = input("To exit press n.:")
        # if check == "n":
        #     exit()
    elif input1 == 2:
        ticket_no = int(input("\t\t\tEnter the Ticket No: "))
        user_functions.cancel_ticket(ticket_no)
        #passing to Cancel function
    elif input1 ==3 :
        ticket_no = input("\t\t\tEnter the Ticket No: ")
        user_functions.ticket_status(ticket_no)
        #passing to ticket status viewing function
    elif input1 == 4:
        exit()
    else:
        print("\t\t\tInvalid Operation")
        con_in = input("\t\t\tDo you wish to continue,press y.\n\t\t\tpress any other key to exit :")
