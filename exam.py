#Turdiqulov Beknazar
#task 1
import psycopg2
database = 'lesson'
user = 'postgres'
host = 'localhost'
port = 5432
password = '703'


conn = psycopg2.connect(database = 'lesson',user = 'postgres',host = 'localhost',port = 5432,password = '703')
cur = conn.cursor()

create_table_query = """ CREATE TABLE Product (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR (100) NOT NULL,
                        price INT,
                        image TEXT
                        );
"""
cur.execute(create_table_query)
conn.commit()
print('Tabel muofaqiyatli yaratildi bratim😉')

#task 2
def connect(): # this is connect func
    conn = psycopg2.connect(database = 'lesson',user = 'postgres',host = 'localhost',
                            port = 5432,password = '703')

    return conn
# #insert func
def insert_product(name,price,color,image):
    conn = connect()
    cur = conn.cursor()
    insert_query = """ INSERT INTO Product (name,price,color,image)
                        VALUES('Keyboard',29.99,'Balck','Image.jpg')
"""
insert_product('Keyboard',29.99,'Balck','Image.jpg')

# #select func
def select_all_product():
    conn = connect()
    cur = conn.cursor()
    select_query = (""" SELECT * FROM Product """)
    cur.execute(select_query)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

# select_all_product()


# #update func
def update_product(product_id,name,price,color,image):
    conn = connect()
    cur = conn.cursor()
    update_query = """ UPDATE Product SET name = %s,price = %s,color = %s,
                        image = %s where id = %s """
    cur.execute(update_query, (name,price,color,image,product_id))
    conn.commit()
    cur.close()
    conn.close()

update_product(1,name="New Keyboard",price=39.99,color="Silver",image="new_keyboard.jpg")

# #delet_func
def delete_product(product_id):
    conn = connect()
    cur = conn.cursor()
    delete_query = (""" DELETE FROM Product WHERE id = %s""")
    cur.execute(delete_query, (product_id,))
    conn.commit()
    cur.close()
    conn.close()

delete_product(1)

# #task 3
class Alfabet:
    def __init__(self):
        self.alifbe = "abcdefghijklmnopqrstuvwxyz"
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.alifbe):
            result = self.alifbe[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

xarf = Alfabet()

for alifbe in xarf:
    print(alifbe)



# #task 4
import threading
import time

def number(start, end):
    for num in range(start, end + 1):
        print(num)
        time.sleep(1)

def letter():
    letters = 'ABCDEFGHLMNJK'
    for letter in letters:
        print(letter)
        time.sleep(1)

thread_number = threading.Thread(target=number, args=(1, 13))
thread_letter = threading.Thread(target=letter)


thread_number.start()
thread_letter.start()


thread_number.join()
thread_letter.join()
print("O'sha mashxur Tom ni do'sti senmisan u seni nimangni yoqtirib qolgan o'zi 🤨")




# #task 5
import psycopg2

class Product:
    def __init__(self, name, price, color, image):
        self.name = name
        self.price = price
        self.color = color
        self.image = image

    def save(self):
        dbname = 'lesson'
        user = 'postgres'
        password = '703'
        host = 'localhost'
        port = 5432
        conn = psycopg2.connect(dbname=dbname, user=user, 
                password=password, host=host, port=port)
        cur = conn.cursor()
        cur.execute('''
                INSERT INTO Product (name, price, color, image)
                VALUES (%s, %s, %s, %s);
            ''',
            (self.name, self.price, self.color, self.image))
        conn.commit()
        print("Succesfuly saved")          
        if conn is not None:
            cur.close()
            conn.close()

product = Product('Phone',599.99,'Black','Samsung.png')
product.save()




# #task 6
import psycopg2

class DbConnect:
    def __init__(self, dbname='lesson', user='postgres', password='703', host='localhost', port='5432'):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def __enter__(self):
        self.conn = psycopg2.connect(dbname=self.dbname,
                                    user=self.user,
                                    password=self.password,
                                    host=self.host,
                                    port=self.port)
        self.cur = self.conn.cursor()
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cur.close()
        self.conn.close()

with DbConnect(dbname='postgres', user='postgres', password='703', host='localhost', port='5432') as cur:
    cur.execute("SELECT * FROM my_table;")
    rows = cur.fetchall()
    for row in rows:
        print(rows)


# #task 7
import requests
DB_NAME = 'lessonfor'
USER = 'postgres'
PASSWORD = '703'
HOST = 'localhost'
PORT = 5432


url = 'https://dummyjson.com/products/'
response = requests.get(url)
data = response.json()['products']


conn = psycopg2.connect(dbname=DB_NAME, user=USER, password=PASSWORD, host=HOST, port=PORT)
cur = conn.cursor()


create_table_query = """
    CREATE TABLE PRODUCT(
        id SERIAL PRIMARY KEY,
        title VARCHAR(200) NOT NULL,
        price INT,
        discription TEXT
    );
"""

cur.execute(create_table_query)
conn.commit()

insert_query = """
        INSERT INTO PRODUCT (title, price, discription) 
        VALUES (%s, %s, %s);
    """

for product in data:
    
    cur.execute(insert_query, (product['title'], product['price'], product['description']))

conn.commit()

cur.close()
conn.close()