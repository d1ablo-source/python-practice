import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute("CREATE TABLE purchases (id INTEGER PRIMARY KEY, fruit TEXT, price REAL, shop TEXT)")
cur.executemany(
    "INSERT INTO purchases (fruit, price, shop) VALUES (?, ?, ?)",
    [("apple", 3.0, "A"), ("pear", 5.0, "A"), ("apple", 4.0, "B"),
     ("plum", 2.0, "B"), ("pear", 6.0, "B"), ("apple", 3.5, "A")],
)

def q(sql):
    cur.execute(sql)
    print(cur.fetchall())

q("SELECT * FROM purchases")
q("SELECT fruit, shop FROM purchases")
q("SELECT fruit, price FROM purchases WHERE price >= 3.5")
q("SELECT * FROM purchases WHERE fruit = 'pear'")
q("SELECT fruit, shop FROM purchases ORDER BY price DESC")
q("SELECT * FROM purchases ORDER BY price DESC LIMIT 3")#DESC это по убыванию (без него по возрастанию). LIMIT 2 это срез [:2].
q("SELECT COUNT(*), SUM(price) FROM purchases")#COUNT(*) считает строки, SUM(price) складывает значения колонки.
q("SELECT fruit, COUNT(*), SUM(price) FROM purchases GROUP BY fruit")

q("SELECT fruit, SUM(price) FROM purchases WHERE shop = 'A' GROUP BY fruit")
q("SELECT fruit, SUM(price) FROM purchases GROUP BY fruit ORDER BY SUM(price) DESC LIMIT 3")


q("SELECT fruit, price FROM purchases WHERE shop = 'B'")
q("SELECT shop, COUNT(*) FROM purchases GROUP BY shop")
q("SELECT fruit, COUNT(*) FROM purchases GROUP BY fruit ORDER BY COUNT(*) DESC LIMIT 1")