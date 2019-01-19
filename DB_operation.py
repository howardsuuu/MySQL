import mysql.connector

# open the csv file
data = open(r"/Users/howardsu666/Github/"
            r"Data_analysis/Titanic/test.csv")
datastring = data.read()



# Convert String to the list
datalist = []
# split("\n") means split every a new line
for i in datastring.split("\n"):
    datalist.append(i.split(","))# split according to the comma and put in the list datalist


# Connect to the MySQL
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "howard24755469",
    database = "howarddb"
)

# Preparing the cursor
my_cursor = mydb.cursor()

# Drop table if it's already exists
#my_cursor.execute("CREATE TABLE IF EXISTS users")

# Create the column name for the first line in the list
PassengerID = datalist[0][0]; Pclass = datalist[0][1]; Name = datalist[0][2];
Sex = datalist[0][3]; Age = datalist[0][4]; SibSp = datalist[0][5];
Parch = datalist[0][6]; Ticket = datalist[0][7]; Fare = datalist[0][8];
Cabin = datalist[0][9]; Embarked = datalist[0][10]

# Create the Titanic Table
Titanic_table = """CREATE TABLE test(
    {} INTEGER,
    {} INTEGER,
    {} VARCHAR (255) NOT NULL,
    {} VARCHAR (255) NOT NULL,
    {} INTEGER,
    {} BOOL,
    {} BOOL,
    {} INTEGER,
    {} FLOAT,
    {} VARCHAR (255) NOT NULL,
    {} VARCHAR (255) 
    )""".format(PassengerID, Pclass, Name, Sex, Age, SibSp, Parch,
        Ticket, Fare, Cabin, Embarked)
my_cursor.execute(Titanic_table)

del datalist[0]

rows = ''

for i in range(len(datalist) - 1):
    rows += """('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}'
    )""".format(datalist[i][0], datalist[i][1], datalist[i][2], datalist[i][3],
    datalist[i][4], datalist[i][5], datalist[i][6], datalist[i][7], datalist[i][8],
    datalist[i][9], datalist[i][10])
    if i != len(datalist) - 2:
        rows += ','

datainsert = "INSERT INTO test VALUES" + rows

try: 
    my_cursor.execute(datainsert)
    mydb.commit()
except:
    mydb.rollback()

mydb.close()


