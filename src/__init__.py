import datetime
csv_read_filename = "/tmp/mca_prefinal.csv"
read_date_format = "%d-%m-%Y"
csv_write_filename = "/home/siddhanthgupta/Databases/student_database_" + str(datetime.datetime.now()) +".csv"
fieldnames_read = ['roll', 'name', 'reg_no', 'gpa1', 'gpa2', 'gpa3', 'reg_year']
fieldnames_all = ['roll', 'name', 'dob', 'email', 'reg_no', 'phone', 'alt_phone', 'address', 
                    'wbjee_rank', 'gender', 'board10', 'marks10', 'board12', 'marks12', 'gpa1',
                    'gpa2', 'gpa3', 'gpa4', 'gpa5', 'gpa6', 'gpa7', 'gpa8', 'reg_year', 
                    'batch_passing_year', 'course', 'department', 'job_offer', 'cgpa', 'city', 'pin_code', 'school10', 'school12',
                    'passing_year_10', 'passing_year_12', 'guardian']
fieldnames_write = fieldnames_all
read_flag = False
write_flag = True
copy_read_write = False
if(copy_read_write):
    csv_read_filename = csv_write_filename
    fieldnames_read = fieldnames_write

'''
mysql> describe student;
+--------------------+-----------+------+-----+---------+-------+
| Field              | Type      | Null | Key | Default | Extra |
+--------------------+-----------+------+-----+---------+-------+
| roll               | char(30)  | NO   | PRI | NULL    |       |
| name               | char(120) | NO   |     | NULL    |       |
| dob                | date      | YES  |     | NULL    |       |
| email              | char(200) | YES  |     | NULL    |       |
| reg_no             | char(120) | YES  |     | NULL    |       |
| phone              | char(20)  | YES  |     | NULL    |       |
| alt_phone          | char(20)  | YES  |     | NULL    |       |
| address            | text      | YES  |     | NULL    |       |
| wbjee_rank         | int(11)   | YES  |     | NULL    |       |
| gender             | char(20)  | YES  |     | NULL    |       |
| board10            | char(10)  | YES  |     | NULL    |       |
| marks10            | float     | YES  |     | NULL    |       |
| board12            | char(10)  | YES  |     | NULL    |       |
| marks12            | float     | YES  |     | NULL    |       |
| gpa1               | float     | YES  |     | NULL    |       |
| gpa2               | float     | YES  |     | NULL    |       |
| gpa3               | float     | YES  |     | NULL    |       |
| gpa4               | float     | YES  |     | NULL    |       |
| gpa5               | float     | YES  |     | NULL    |       |
| gpa6               | float     | YES  |     | NULL    |       |
| gpa7               | float     | YES  |     | NULL    |       |
| gpa8               | float     | YES  |     | NULL    |       |
| reg_year           | char(20)  | YES  |     | NULL    |       |
| batch_passing_year | int(11)   | YES  |     | NULL    |       |
| course             | char(20)  | YES  |     | NULL    |       |
| department         | char(20)  | YES  |     | NULL    |       |
| job_offer          | char(20)  | YES  |     | NULL    |       |
| cgpa               | float     | YES  |     | NULL    |       |
| city               | char(40)  | YES  |     | NULL    |       |
| pin_code           | char(10)  | YES  |     | NULL    |       |
| school10           | text      | YES  |     | NULL    |       |
| school12           | text      | YES  |     | NULL    |       |
| passing_year_10    | int(11)   | YES  |     | NULL    |       |
| passing_year_12    | int(11)   | YES  |     | NULL    |       |
| guardian           | char(120) | YES  |     | NULL    |       |
+--------------------+-----------+------+-----+---------+-------+
35 rows in set (0.01 sec)


'''
