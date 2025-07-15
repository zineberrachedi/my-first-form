import sqlite3

db=sqlite3.connect('myDataBase.db')
db.cursor().execute("CREATE TABLE USERS(" \
                       "Id INTEGER PRIMARY KEY AUTOINCREMENT," \
                       " name Text not null," \
                       "username text not null unique," \
                       "email text not null," \
                       "password text not null," \
                       "gender text," \
                       "tel text," \
                       "country text," \
                       "photo text)")
db.commit()
db.close()
