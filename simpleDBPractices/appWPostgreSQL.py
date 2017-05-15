import psycopg2


def create_table():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='password123' host='localhost' port='5432'")
    cur =conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='password123' host='localhost' port='5432'")
    cur =conn.cursor()
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)",(item,quantity,price))
    conn.commit()
    conn.close()

def view():
    conn =psycopg2.connect("dbname='database1' user='postgres' password='password123' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(value):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='password123' host='localhost' port='5432'")
    cur =conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(value,))
    conn.commit()
    conn.close()


def update(quantity, price, item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='password123' host='localhost' port='5432'")
    cur =conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quantity,price,item))
    conn.commit()
    conn.close()

create_table()
#insert("Banana", 10, 5 )
# insert("Coffee Cup", 10, 7.5 )
# insert("Wine Glass", 10, 3.5 )
#delete("Banana")
# delete("Coffee Cup")
# delete("Wine Glass")
update(100,5,'Orange')
print(view())

#print(view())
