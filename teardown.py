import sqlite3
from sqlite3 import Error
import os

# connect to sqlite database
conn = sqlite3.connect("e30x.db")

# delete bye table
conn.execute("""
    drop table bye; 
""")

# delete workout table
conn.execute("""
    drop table workout; 
""")

# delete bye_trigger table
conn.execute("""
    drop table bye_trigger; 
""")

# delete challenge table
conn.execute("""
    drop table challenge;
""")

# delete user table
conn.execute("""
    drop table user; 
""")

conn.commit()
conn.close()