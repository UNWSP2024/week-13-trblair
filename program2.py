import sqlite3
#Creates database
connection = sqlite3.connect("phonebook.db")
cursor = connection.cursor()
cursor.execute("drop table if exists Entries")
cursor.execute("create table Entries (name text, number text)")

def createrow(name,number):
    datalist=[name,number]
    cursor.execute("insert into Entries (name, number) values (?,?)",datalist)

#manages deleting rows
def deleterow(value):
    cursor.execute("delete from Entries where name=:c or number =:c ", {"c":value})

#manages viewing rows
def viewrow(value):
    cursor.execute("select * from Entries where number=:c or name=:c", {"c":value})
    output=cursor.fetchall()
    print(output)

#manages updating rows
def updaterow(value,newname,newnumber):
    datalist=[newname,newnumber,value]
    cursor.execute("UPDATE Entries SET name = (?), number= (?) WHERE name or number =(?)", datalist)

#handles user decisionmaking (rounding command is for user error regarding decimals)
def database():
    choice = round(float(input("What command would you like to execute?\n1.View a row\n2.Create a row\n3.Update a row\n4.Delete a row\n5.Close database\n")))
    #basic commands
    if choice == 1:
        inputvalue=input("Please enter either the number or name that you are looking to view:\n")
        viewrow(inputvalue)
        database()
    elif choice == 4:
        inputvalue=input("Please enter either the number or name that you are looking to delete:\n")
        deleterow(inputvalue)
        database()

    #update command
    elif choice == 3:
        inputvalue1=str(input("Please enter either the number or name that you are looking to update:\n"))
        inputvalue2=str(input("Please enter the new name:\n"))
        inputvalue3=str(input("Please enter the new number:\n"))
        updaterow(inputvalue1,inputvalue2,inputvalue3)
        database()
        
    #Create row
    elif choice == 2:
        inputvalue1=input("Please enter the name:\n")
        inputvalue2=input("Please enter the number:\n")
        createrow(inputvalue1,inputvalue2)
        database()

    elif choice == 5:
        connection.close()

    #error handling
    else:
        print("ERROR 0\n PLEASE ENTER AN ACCEPTED VALUE (NUMBER BETWEEN 1-5)")
        database()

#runs program
database()

connection.close()
