from src.model.student import Student
from src.dao.student_dao import StudentDAO
from src.csvreader.csv_database_reader import CsvDatabaseReader
from src import fieldnames_read, fieldnames_write, csv_read_filename, csv_write_filename, read_flag, write_flag
from src.csvreader.csv_database_writer import CsvDatabaseWriter
from src.gpa_calculator import GPACalculator

# print([student.name for student in Student.select()])
# test_stud = Student();
# test_stud.name = 'hellowor12323 ld'
# test_stud.roll = '0012105014000'
# test_stud.gpa6 = 123.234
# print(test_stud)
# test_stud.save()
# 
# data_dict = {'roll':'12334', 'name':'4564dfg'}
# #Student.create(**data_dict)
# studentDAO = StudentDAO()
# studentDAO.createOrUpdateModel(studentDAO.dictionaryToModel(data_dict))
# print([student.name for student in Student.select()])

if(read_flag):
    csv_reader = CsvDatabaseReader(*fieldnames_read)
    dict_list = csv_reader.csvToDictionaryList(csv_read_filename)
    print(dict_list)
    for dict in dict_list:
        print(dict)
        studentDAO = StudentDAO()
        studentDAO.createOrUpdateModel(studentDAO.dictionaryToModel(dict))
        
        
# for student in Student.select():
#     cgpa = GPACalculator.calculateGpaForStudent(student)

#GPACalculator.updateCGPAForAllStudents()
# studentDAO = StudentDAO()
# list_students = studentDAO.getStudentsByBatch("CSE", "2016", "BE")#[student for student in Student.select()]
# list_students_2 = studentDAO.getStudentsByBatch("IT", "2016", "BE")
# list_students = list_students + list_students_2
# for student in list_students:
#     print(student.name, student.roll)

if(write_flag):
    studentDAO = StudentDAO()
    list_students = [student for student in Student.select().order_by(Student.course, Student.department, Student.batch_passing_year, Student.roll)]
    #print(list_students)
    csvDatabaseWriter = CsvDatabaseWriter(*fieldnames_write)
    print(fieldnames_write)
    list_students_dictionaries = [student.__dict__.get('_data') for student in list_students]
    #print(list_students_dictionaries)
    csvDatabaseWriter.dictionaryListToCsv(csv_write_filename, *list_students_dictionaries)


