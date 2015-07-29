from peewee import *

database = MySQLDatabase('studentdb', **{'password': 'fuckpasswords', 'user': 'siddhanthgupta'})

class UnknownField(object):
    pass

class BaseModel(Model):
    class Meta:
        database = database

class Student(BaseModel):
    address = TextField(null=True)
    alt_phone = CharField(null=True)
    batch_passing_year = IntegerField(null=True)
    board10 = CharField(null=True)
    board12 = CharField(null=True)
    course = CharField(null=True)
    department = CharField(null=True)
    dob = DateField(null=True)
    email = CharField(null=True)
    gender = CharField(null=True)
    gpa1 = FloatField(null=True)
    gpa2 = FloatField(null=True)
    gpa3 = FloatField(null=True)
    gpa4 = FloatField(null=True)
    gpa5 = FloatField(null=True)
    gpa6 = FloatField(null=True)
    gpa7 = FloatField(null=True)
    gpa8 = FloatField(null=True)
    marks10 = FloatField(null=True)
    marks12 = FloatField(null=True)
    name = CharField()
    phone = CharField(null=True)
    reg_no = CharField(null=True)
    reg_year = CharField(null=True)
    roll = CharField(primary_key=True)
    wbjee_rank = IntegerField(null=True)
    job_offer = CharField(null=True)
    cgpa = FloatField(null=True)
    city = CharField(null=True)
    pin_code = CharField(null=True)
    school10 = TextField(null=True)
    school12 = TextField(null=True)
    passing_year_10 = IntegerField(null=True)
    passing_year_12 = IntegerField(null=True)
    guardian = CharField(null=True)
    
    class Meta:
        db_table = 'student'