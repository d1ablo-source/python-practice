import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)")
cur.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, user_id INTEGER, amount REAL, status TEXT)")
cur.executemany("INSERT INTO users VALUES (?, ?)",
                [(1, "anna"), (2, "boris"), (3, "clara"), (4, "dima")])
cur.executemany("INSERT INTO orders VALUES (?, ?, ?, ?)",
                [(1, 1, 120.5, "paid"), (2, 2, 80.0, "cancelled"), (3, 1, 40.0, "paid"),
                 (4, 3, 300.0, "paid"), (5, 2, 55.0, "paid")])

def q(sql):
    cur.execute(sql)
    print(cur.fetchall())
q("""SELECT orders.id, users.name, orders.amount
    FROM users JOIN orders ON orders.user_id = users.id
    ORDER BY orders.id
""")
q("""SELECT users.name, COUNT(orders.id)
    FROM users JOIN orders ON orders.user_id = users.id
    GROUP BY users.id, users.name
    ORDER BY users.name
""")
