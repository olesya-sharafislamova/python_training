
from fixture.orm import ORMFixture
from model.group import Group
import pymysql.cursors
from fixture.db import DbFixture

db = ORMFixture(host='127.0.0.1', name = 'addressbook', user = 'root', password='')
#db = DbFixture (host='127.0.0.1', name = 'addressbook', user = 'root', password='')

try:
    l = db.get_contact_list()
    for item in l:
       print(item)
    print(len(l))
finally:
    pass #db.destroy()