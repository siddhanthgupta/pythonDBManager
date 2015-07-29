import urllib3
import traceback
import re
from bs4 import BeautifulSoup
from src.model.student import Student
from src.dao.student_dao import StudentDAO
try:
    for i in range(1, 70):
        exam_roll = 'CSE1550' + format(i, '02d');
        gpa_flag = False
        gpa_value = None
        class_roll = None
        http = urllib3.PoolManager()
        request = http.request('GET', 'http://www.juexam.org/newexam/show_result.asp?f1=' + exam_roll + '&f2=E3CSE1531R')
#         print(request.status)
#         print(request.headers)
#         print(request.data)
        soup = BeautifulSoup(request.data, 'lxml')
#         print(soup.prettify())
        list_strong = soup.find_all("strong")
        for elem in list_strong:
#             print("item: ")
#             print(elem.text)
            x = elem.text.split(':')
#             print(x)
            if('SGPA' in x[0]):
#                 print('yes',x[1].strip())
                try:
                    gpa_value = float(x[1].strip())
                except Exception:
                    print("Exception occurred in extracting GPA")
                    traceback.print_exc()
                else:
                    gpa_flag = True
        if(gpa_flag):       
            list_td = soup.find_all("td", attrs={"align":"center", "class":"underlineresult"})
            for elem in list_td:
                text = elem.text.strip()
                if(re.search("^0012105010", text)):
                    class_roll = text
        if(gpa_flag and class_roll):
            print(exam_roll, class_roll, gpa_value)
            student = Student()
            student.roll = class_roll
            student.gpa5 = gpa_value
            studentDAO = StudentDAO()
            studentDAO.createOrUpdateModel(student)
except Exception:
    print("Exception occurred")
    traceback.print_exc()