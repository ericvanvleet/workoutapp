import sqlite3
from sqlite3 import Error
import os

# connect to sqlite database
conn = sqlite3.connect("e30x.db")

# create user table
conn.execute("""
    create table user(
        id varchar(36) primary key,
        name varchar(32) not null
    )
""")

# create challenge table
conn.execute("""
    create table challenge(
        id varchar(36) primary key,
        start_date varchar(10) not null,
        end_date varchar(10) not null
        --organizer varchar(36),
        --FOREIGN KEY(organizer) REFERENCES user(id) 
    )
""")

# create bye_trigger table
conn.execute("""
    create table bye_trigger(
        id varchar(36) primary key,
        date varchar(10) not null,
        bye_count integer not null,
        challenge varchar(36),
        FOREIGN KEY(challenge) REFERENCES challenge(id)
    )
""")

# create workout table
conn.execute("""
    create table workout(
        id varchar(36) primary key,
        date varchar(10) not null,
        challenge varchar(36),
        user varchar(36),
        FOREIGN KEY(challenge) REFERENCES challenge(id),
        FOREIGN KEY(user) REFERENCES user(id)
    )
""")

# create bye table
conn.execute("""
    create table bye(
        id varchar(36) primary key,
        date varchar(10) not null,
        challenge varchar(36),
        user varchar(36),
        FOREIGN KEY(challenge) REFERENCES challenge(id)
        FOREIGN KEY(user) REFERENCES user(id)
    )
""")

# a given user can only use one bye in a given challenge on a given date
conn.execute("""
    CREATE UNIQUE INDEX bye_date_challenge_user ON bye(date, challenge, user)
""")

# a given user must have a unique name
conn.execute("""
    CREATE UNIQUE INDEX user_name ON user(name)
""")

# a given challenge can only have one bye triger on a given date
conn.execute("""
    CREATE UNIQUE INDEX bye_trigger_challenge_date ON bye_trigger(challenge, date)
""")

# a given challenge can only have one workout per user on a given date
conn.execute("""
    CREATE UNIQUE INDEX workout_user_challenge_date ON workout(user, challenge, date)
""")

conn.commit()
conn.close()