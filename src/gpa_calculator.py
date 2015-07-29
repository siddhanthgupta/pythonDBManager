import re
from src.model.student import Student
from src.dao.student_dao import StudentDAO

'''
Created on 23-Jul-2015

@author: siddhanthgupta
'''

class GPACalculator(object):
    '''
    classdocs
    '''
    @staticmethod
    def calculateGpaForStudent(student):
        if(student.roll is None):
            return None
        lateral_entry = False
        if(re.search("^30", student.roll)):
            lateral_entry = True
        
        weightage = [0, 1, 1, 2, 2, 3.5, 3.5, 3.5, 3.5]
        marks = [None]
        
        marks.append(student.gpa1)
        marks.append(student.gpa2)
        marks.append(student.gpa3)
        marks.append(student.gpa4)
        marks.append(student.gpa5)
        marks.append(student.gpa6)
        marks.append(student.gpa7)
        marks.append(student.gpa8)
        try:
            gpa = sum([weightage[i] * marks[i] for i in range(1,9) if(weightage[i] and marks[i])]) / sum([weightage[i] for i in range(1,9) if(marks[i])])
        except ZeroDivisionError:
            print("Student ", student.name, student.roll, " has no marks in DB")
            return None
        else:
           # gpa =  float("{0:.2f}".format(round(gpa,2)))
            gpa = round(gpa,2)
            print(student.roll, student.name, gpa)
            return gpa
        
    @staticmethod
    def updateCGPAForAllStudents():
        for student in Student.select():
            cgpa = GPACalculator.calculateGpaForStudent(student)
            update_student = Student()
            update_student.roll = student.roll
            update_student.cgpa = cgpa
            studentDAO = StudentDAO()
            if(cgpa is not None):
                studentDAO.createOrUpdateModel(update_student)