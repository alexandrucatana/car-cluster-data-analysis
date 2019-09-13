import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="newpassword",
  database="time_db"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS action_table(id INTEGER NOT NULL, start_Date  DATETIME, action_type  VARCHAR(10))")

mycursor.execute("INSERT INTO action_table VALUES (1, '2005-03-22','visit');")
mycursor.execute("INSERT INTO action_table VALUES (1, '2005-03-23','view');")
mycursor.execute("INSERT INTO action_table VALUES (1, '2005-03-24','purchase');")

mycursor.execute("INSERT INTO action_table VALUES (2, '2005-03-23','visit');")
mycursor.execute("INSERT INTO action_table VALUES (2, '2005-03-24','view');")
mycursor.execute("INSERT INTO action_table VALUES (2, '2005-03-25','purchase');")

mycursor.execute("INSERT INTO action_table VALUES (3, '2005-03-24','visit');")
mycursor.execute("INSERT INTO action_table VALUES (4, '2005-03-25','view');")
mycursor.execute("INSERT INTO action_table VALUES (5, '2005-03-25','purchase');")

mydb.commit()