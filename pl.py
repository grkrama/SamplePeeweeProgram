from peewee import *


db = SqliteDatabase("people.db")

#table Model
class People(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db

db.connect()

#create table only if it doesn't exists.
db.create_tables([People])

peopleList = People.create(name="hi",
              birthday = '01/01/2020')

peopleList.save()

print(peopleList.name)

peopleQuery = (People
               .select())

print(peopleQuery)

for sample in peopleQuery:
    print (sample.name, sample.id)
    
print(peopleQuery.execute())

db.close()
