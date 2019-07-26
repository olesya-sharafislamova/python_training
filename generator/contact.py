import getopt
import sys
from model.contact import Contact
import string
import random
import os.path
import jsonpickle

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    print(err)
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n=int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_string_for_phone(prefix, maxlen):
    symbols = string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_string_for_email(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])+ "@ya.ru"


testdata = [
    Contact(firstname=random_string("firstname", 5),
            middlename=random_string("middlename", 10),
            lastname=random_string("lastname", 10),
            nickname=random_string("nickname", 10),
            company=random_string("company", 10),
            address=random_string("address", 20),
            homephone=random_string_for_phone("+495", 7),
            mobilephone=random_string_for_phone("+7", 10),
            workphone=random_string_for_phone("+495", 7),
            fax=random_string_for_phone("+495", 7),
            email=random_string_for_email("email", 10),
            email2=random_string_for_email("email2", 10),
            email3=random_string_for_email("email3", 10),
            address2=random_string("address2", 10),
            phone2=random_string_for_phone("+7", 10),
            notes=random_string("notes", 20))
    for i in range(5)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent = 2)
    out.write(jsonpickle.encode(testdata))