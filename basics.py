""" To use sqlite always include the following code in code file
    import sqlite3
    
    To install sqlite 
    pip install sqlite-web

    To run the sqlite database online and view it 
    run the following code
    python -m sqlite_web mydatabase.db"""


from shlex import join
from sqlalchemy import create_engine,MetaData,Table,Column,Integer,Float,String,ForeignKey,func                          #text,insert
import sqlite3
engine = create_engine('sqlite:///mydatabase.db', echo=True)

meta = MetaData()

people = Table(
    "people",
    meta,
    Column("id",Integer,primary_key=True),
    Column('name',String,nullable=False),
    Column('age',Integer)
)

things = Table(
    "things",
    meta,
    Column('id',Integer,primary_key=True),
    Column('description',String,nullable=False),
    Column('value',Float),
    Column('Owner',Integer,ForeignKey('people.id'))
)

meta.create_all(engine)

conn = engine.connect()

insert_people = people.insert().values([
    {'name':'Anjani','age':25},
    {'name':'Padma','age':89},
    {'name':'ARUN','age':20},
    {'name':'Aniket','age':55},
    {'name':'Anika','age':65}
])

insert_things = things.insert().values([
    {'Owner':2,'description':'Mobile','value':900.45},
    {'Owner':2,'description':'Laptop','value':832.72},
    {'Owner':2,'description':'Telephone','value':90.69},
    {'Owner':3,'description':'Lamp','value':9.45},
    {'Owner':4,'description':'Computer','value':1000.00},
    {'Owner':5,'description':'Mouse','value':9.89}
])

# group_by_statement = things.select().with_only_columns(things.c.Owner,func.sum(things.c.value)).group_by(things.c.Owner).having(func.sum(things.c.value) > 50)
# result = conn.execute(group_by_statement)

# for row in result.fetchall():
#     print(row)

# join_statement = people.join(things,people.c.id == things.c.Owner)
# select_statement = people.select().with_only_columns(people.c.name , things.c.description).select_from(join_statement)
# result = conn.execute(select_statement)

# for row in result.fetchall():
#     print(row)

# conn.execute(insert_people)
# conn.commit()

# conn.execute(insert_things)
# conn.commit()

# delete_statement = people.delete().where(people.c.name == 'Aditya')
# result = conn.execute(delete_statement)
# conn.commit()

# update_statement = people.update().where(people.c.name == 'Pavan').values(age=10000)
# result = conn.execute(update_statement)
# conn.commit()



# select_statement = people.select()
# result = conn.execute(select_statement)

# for row in result.fetchall():
#     print(row)


# select_statement = people.select().where(people.c.age < 30)
# result = conn.execute(select_statement)

# for row in result.fetchall():
#     print(row)




# insert_statement = people.insert().values(name='Aditya',age=21)
'''to execute the following line also write this in import statements
    from sqlalchemy import insert'''
# insert_statement = insert(people).values(name='Pavan',age=30)
# result = conn.execute(insert_statement)
# conn.commit()

# conn = engine.connect()

# conn.execute(text("CREATE TABLE IF NOT EXISTS people (name str, age int)"))

# conn.commit()

# from sqlalchemy.orm import Session

# session = Session(engine)

# session.execute(text('INSERT INTO people (name , age) VALUES ("MIKE" , 30);'))

# session.commit()