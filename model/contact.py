
from sys import maxsize

class Contact:

    def __init__(self, firstname = None, middlename = None, lastname= None, nickname= None, company = None,
                 address= None, homephone= None, mobilephone= None, mail= None, mail2= None, mail3= None,
                 address2= None, notes=None, id = None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.mail = mail
        self.mail2 = mail2
        self.mail3 = mail3
        self.address2 = address2
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and (self.firstname is None or other.firstname is None or self.firstname == other.firstname) \
               and (self.lastname is None or other.lastname is None or self.lastname == other.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
