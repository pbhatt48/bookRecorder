import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()


def insert(title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur =conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title, author, year, isbn))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect(("books.db"))
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id=""):
    conn = sqlite3.connect(("books.db"))
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(id, title="", author="", year="", isbn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, author =? , year=? , isbn=? WHERE id=?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()


connect()

# insert( 'The sea', 'John Tablet', 1918, 123456)
# insert('Last Don', 'Mario Puzo', 1940, 456783239)
# insert('Good Father', 'Lucas Romeo', 12345, 453453453)
# insert('Hannibal', 'Mario Puzo', 1900, 123456783239)
# insert('Rakatic', 'James Bond', 1945, 6783239)
#print(search(author="John Tablet"))
#delete(id=2)
update( "Blackkkk Father", "Black Romeo", 656756,8797)
print(search(author="Mario Puzo"))
print(view())

