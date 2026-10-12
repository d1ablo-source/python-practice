import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()
cur.execute("CREATE TABLE authors (id INTEGER PRIMARY KEY, name TEXT)")
cur.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, author_id INTEGER, title TEXT)")
cur.executemany("INSERT INTO authors VALUES (?, ?)",
                [(1, "tolstoy"), (2, "chekhov"), (3, "gogol")])
cur.executemany("INSERT INTO books VALUES (?, ?, ?)",
                [(1, 1, "war"), (2, 1, "anna"), (3, 2, "cherry")])

def q(sql):
    cur.execute(sql)
    print(cur.fetchall())

q("""SELECT authors.name, books.title
     FROM books JOIN authors ON books.author_id = authors.id
     ORDER BY books.id""")
# [('tolstoy', 'war'), ('tolstoy', 'anna'), ('chekhov', 'cherry')]
q("""SELECT authors.name, COUNT(books.id)
     FROM authors LEFT JOIN books ON books.author_id = authors.id
     GROUP BY authors.name
     ORDER BY authors.name""")