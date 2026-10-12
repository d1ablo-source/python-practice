import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("CREATE TABLE orders (id INTEGER PRIMARY KEY, user TEXT, amount REAL, status TEXT)")
cur.executemany(
    "INSERT INTO orders (id, user, amount, status) VALUES (?, ?, ?, ?)",
    [
        (1, "anna", 120.5, "paid"),
        (2, "boris", 80.0, "cancelled"),
        (3, "anna", 40.0, "paid"),
        (4, "clara", 300.0, "paid"),
        (5, "boris", 55.0, "paid"),
    ],
)
conn.commit()

cur.execute("SELECT user, SUM(amount) FROM orders WHERE status = 'paid' GROUP BY user ORDER BY SUM(amount) ASC LIMIT 2")
cur.execute("SELECT status, COUNT(*), SUM(amount) FROM orders GROUP BY status")
print(cur.fetchall())