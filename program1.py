import sqlite3
#List of cities
citylist=[
(1,'Tokyo',38001000),
(2,'Delhi',25703168),
(3,'Shanghai',23740778),
(4,'Sao Paulo',21066245),
(5,'Mumbai',21042538),
(6,'Mexico City',20998543),
(7,'Beijing',20383994),
(8,'Osaka',20237645),
(9,'Cairo',18771769),
(10,'New York',18593220),
(11,'Dhaka',17598228),
(12,'Karachi',16617644),
(13,'Buenos Aires',15180176),
(14,'Kolkata',14864919),
(15,'Istanbul',14163989),
(16,'Chongqing',13331579),
(17,'Lagos',13122829),
(18,'Manila',12946263),
(19,'Rio de Janeiro',12902306),
(20,'Guangzhou',12458130)]

#Creates database
connection = sqlite3.connect("city.db")
cursor = connection.cursor()
cursor.execute("drop table if exists Cities")
cursor.execute("create table Cities (CityId integer,CityName text,Population real)")

#Adds the information from the list into the database
cursor.executemany("insert into Cities values (?,?,?)", citylist)
def viewdatabase():
    value=round(int(input("Please enter the ID of the city you would like to view:\n")))
    if 1<= value <= 20:
        cursor.execute("select * from Cities where CityId=:c", {"c":value})
        search=cursor.fetchall()
        print(search)
    else:
        print("Error, please input a valid ID")
viewdatabase()

connection.close()
