from src.model.student import Student
from peewee import IntegrityError
import traceback

class StudentDAO:
    def createOrUpdateModel(self, student):
        try:
            student.save(force_insert=True)
        except IntegrityError:
            print("Item already exists in DB. Updating item")
            try:
                student.save()
            except Exception:
                print("Error: unable to update database entry")
                traceback.print_exc()
                
    def createDictonary(self, student):
        try:
            Student.create(**student)
        except Exception:
            print("Error: unable to update database entry")
            traceback.print_exc()

    def dictionaryToModel(self, dictionary):
        student = Student()
        for key in dictionary:
            setattr(student, key, dictionary[key])
        return student

    def readEntry(self, roll):
        try:
            student = Student.get(Student.roll == roll)
        except Exception:
            print("Error: invalid roll number")
            return None
        return student
    
    def getAllStudents(self):
        try:
            list_students = [student for student in Student.select()]
        except Exception:
            print("Exception occurred.")
            traceback.print_exc()
            return None
        return list_students
    
    def getStudentsByBatch(self, department, year_of_passing, course):
        try:
            list_students = [student for student in Student.select().where((Student.department == department) & (Student.batch_passing_year == year_of_passing) & (Student.course == course))]
        except:
            print("Exception occurred")
            traceback.print_exc()
            return []
        return list_students

