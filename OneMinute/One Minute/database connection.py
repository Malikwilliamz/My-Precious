import sqlite3 as sq

connecting = sq.connect('Member_Info.db')
connecting_cursor = connecting.cursor()

connecting_cursor.execute("""CREATE TABLE info(
                          Name text,
                          House_Number text,
                          Phone_Number text)
""")

connecting.commit()
connecting.close()



