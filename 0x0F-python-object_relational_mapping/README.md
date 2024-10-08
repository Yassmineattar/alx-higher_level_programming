from my_models import Base, State  # assuming my_models.py defines Base and State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import MySQLdb
0x0F - python - object_relational_mapping
# Project Overview

In this project, you will link two amazing worlds: Databases and Python!

# Background Context

In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module SQLAlchemy(don’t ask me how to pronounce it…) as an Object Relational Mapper(ORM).

The biggest difference is : no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and “How is not this object stored? Where? When?”. You won’t write any SQL queries, only Python code. Lastly, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

# Without ORM:

```python

conn = MySQLdb.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="root",
    db="my_db",
    charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
# HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()

# With an ORM:

```python

engine = create_engine(
    'mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(
        State).order_by(State.id).all():  # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
