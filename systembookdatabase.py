import sqlite3
database = "database2.db"
conn = sqlite3.connect(database)
c = conn.cursor()
c.execute('''CREATE TABLE systembook (Id, Books, Book_checkout, Book_Returned, Days_allowed_to_borrow, Customer_ID, Duration_Days)''')
c.execute("INSERT INTO systembook VALUES ('1', 'Catcher in the Rye', '2023-02-20', '2023-02-25', '2 weeks', '1', '5.0')")
conn.commit()
conn.close()