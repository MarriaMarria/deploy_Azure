import psycopg2
import logging
# postgres connection
logging.basicConfig(filename='db.log', 
                    level=logging.INFO, 
                    format=f'%(asctime)s - %(name)s - %(threadName)s - %(message)s')

# connecting to Azure's postgres with psycopg2 library 
logging.info("connecting to postgresql: start")

connection = psycopg2.connect(
    host="localhost", \
    dbname="postgres", \
    user="postgres",\
    password="pw")

logging.info("connecting to postgresql: end")

print("connection established")
cursor = connection.cursor()

def create_table():
    # cursor.execute("DROP TABLE maria_db")
    cursor.execute("CREATE TABLE IF NOT EXISTS maria_db (id INT PRIMARY KEY, name VARCHAR(50), occupation VARCHAR(50), city VARCHAR(50))")
    connection.commit()
    print("table created")

# create_table()

def insert_to(): 
    cursor.execute("INSERT INTO maria_db VALUES (%s, %s, %s, %s)", ("1", "Maria", "forever student", "Paris"))
    connection.commit()
    print('inserted')

# insert_to()