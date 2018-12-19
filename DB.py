import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "howard24755469",
    database = "howarddb"
    )

my_cursor = mydb.cursor()

# Create a database
my_cursor.execute("CREATE DATABASE howarddb")

# Create a table
my_cursor.execute("CREATE TABLE users (name VARCHAR(255), email VARCHAR(255), age INTEGER(10), user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")
my_cursor.execute("SHOW DATABASE")

# Insert single record into the table
SQLstuff = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
record1 = ("Howard", "howardsu666@gmail.com", 21 )
my_cursor.execute(SQLstuff, record1)
mydb.commit()

# Insert many records into table
SQLstuff = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
records = [("Hans", "howard512711@gmail.com", 19),
    ("Sam", "slm07111@yahoo.com.tw", 50),
    ("Connie", "fcw529@gmail.com", 45),
    ("Sarah", "kuanhao@sjsu.edu", 18),]
my_cursor.executemany(SQLstuff, records)
mydb.commit()

#pull the data from database, * means everything
my_cursor.execute("SELECT * FROM users")
result = my_cursor.fetchall() # or .fetchone()
print("Name\tEmail\t\t\tAge\tID")
print("____\t_____\t\t\t____\t____")
for row in result:
    #print(row)
    print(row[0] + "\t%s" %row[1] + "\t\t%s" %row[2] + "\t%s" %row[3])

# Search Certain data( Integer )
my_cursor.execute("SELECT * FROM users WHERE age > 30")
age_result = my_cursor.fetchall()
for age in age_result:
    print(age)

# Search certain data (String) % means make database search after %
my_cursor.execute("SELECT * FROM users WHERE name LIKE 'H%'")
name_result = my_cursor.fetchall()
for name in name_result:
    print(name)

my_cursor.execute("SELECT * FROM users WHERE name LIKE '%a%'")
name_result = my_cursor.fetchall()
for name in name_result:
    print(name) # Howard, Hans, Sam, Sarah

# And / Or
my_cursor.execute("SELECT * FROM users WHERE name LIKE '%a%' AND  age = 21")
name_result = my_cursor.fetchall()
for name in name_result: # AND / OR
    print(name) # Howard

# Updataing the record
my_sql = "UPDATE users SET age = 25 WHERE name = 'Howard' AND user_id = 6"
my_cursor.execute(my_sql)
mydb.commit()

# Limit results  OFFSET means exclude that number
my_cursor.execute("SELECT * FROM users LIMIT 3 OFFSET 1")
result = my_cursor.fetchall()
for row in result:
    print(row)

# Limit results    by descending or ascesending
my_cursor.execute("SELECT * FROM users ORDER BY name DESC") # DESC or ASC
result = my_cursor.fetchall()
for row in result:
    print(row)

# Delete the record 
mysql = "DELETE FROM users WHERE user_id = 6"
my_cursor.execute(mysql)
mydb.commit()

# Delete entire table 
my_sql = "DROP TABLE users"
my_cursor.execute(my_sql)







