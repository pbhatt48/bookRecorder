import sqlite3


def create_table():
    conn = sqlite3.connect("lite.db")
    cur =conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


def insert(item, quantity, price):
    conn = sqlite3.connect("lite.db")
    cur =conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()

# insert("Water Glass", 10, 5 )
# insert("Coffee Cup", 10, 7.5 )
# insert("Wine Glass", 10, 3.5 )

def view():
    conn =sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

print(view())

def delete(value):
    conn = sqlite3.connect("lite.db")
    cur =conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(value,))
    conn.commit()
    conn.close()

# delete("Water Glass")
# delete("Coffee Cup")
# delete("Wine Glass")

def update(quantity, price, item):
    conn = sqlite3.connect("lite.db")
    cur =conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity,price,item))
    conn.commit()
    conn.close()

update(5,5,'Coffee Cup')

print(view())
