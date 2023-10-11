import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CRUDFBVProject.settings')
import django

django.setup()
from MyApps1.models import *          #cmd\DBModelProject> py manage.py shell
from faker import Faker
from random import *
faker = Faker()                         # >>> from faker import Faker
                                       # >>> help(Faker)
                                         #   (or)
                                        #>>> dir(Faker)




def populate(n):
    for i in range(n):
        feno =faker.randint(1001, 9999)
        fename = faker.name()
        fesal = faker.randint(10000, 20000)
        feaddr = faker.city()
    emp_record = Employee.objects.get_or_create(eno=feno,ename=fename,esal=fesal,eaddr=feaddr)
    print(emp_record)
    populate(10)
