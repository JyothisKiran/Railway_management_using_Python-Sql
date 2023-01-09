import csv
import mysql.connector as con
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="52828378Jyo#"
# )
#
# cursor = mydb.cursor()
# cursor.execute("CREATE DATABASE raildb")
# mydb.close()

# """Creating tables"""
# mydb = con.connect(
#   host="localhost",
#   user="root",
#   password="52828378Jyo#",
#   database="raildb"
# )
#
# mycursor = mydb.cursor()
#
# mycursor.execute("CREATE TABLE trainData (train_no VARCHAR(255), stationcode VARCHAR(255), stationname VARCHAR(255), "
#                  "arrivaltime VARCHAR(255), departuretime VARCHAR(255), distance VARCHAR(255), sourcestation VARCHAR(255),sourcestationname VARCHAR(255),"
#                  "destinationstation VARCHAR(255),destinationstationname VARCHAR(255))")
#
# """Inserting values into db"""
# mydb = con.connect(
#   host="localhost",
#   user="root",
#   password="52828378Jyo#",
#   database="raildb"
# )
#
# cur = mydb.cursor()
#
# # Iterating through all the values and insert's them in the table
# # Replace the path below with the absolute path of the file on your computer
# try:
#     with open(r"C:\Users\jyothis\PycharmProjects\ railway mgmt system\Train_details.csv") as csv_data:
#         csv_reader = csv.reader(csv_data, delimiter=",")
#         for row in csv_reader:
#             cur.execute(
#                 'INSERT INTO traindata VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', row)
# except FileNotFoundError:
#     print("Please check whether the file is in the Assets Folder or not and try changing the Location in InsertData.py")
# finally:
#     mydb.commit()  # Important: Committing the Changes
#     cur.close()
#     mydb.close()

#
# """Creating Database for Booking"""
# mydb = con.connect(
#   host="localhost",
#   user="root",
#   password="52828378Jyo#"
# )
#
# cur = mydb.cursor()
# cur.execute("CREATE DATABASE bookingstatus")
#
# cur.execute("CREATE TABLE statustab()")