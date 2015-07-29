import csv
import traceback
from datetime import datetime
from src import read_date_format

class CsvDatabaseReader:
    def __init__(self, *fieldnames):
        self.fieldnames = fieldnames
        
    def csvToDictionaryList(self, filename):
        list_student_dictionaries = []
        try:
            with open(filename) as csv_file:
                reader = csv.DictReader(csv_file, self.fieldnames)
                for row in reader:
                    modified_row = {k:v for k, v in row.items() if v}
                    datestring = modified_row.get('dob')
                    if(datestring):
                        date_object = datetime.strptime(datestring, read_date_format)
                        modified_row['dob'] = date_object
                    roll_no = modified_row.get('roll')
                    
                    if(roll):
                        modified_roll = roll.zfill(12)
                        modified_row['roll'] = modified_roll
                        list_student_dictionaries.append(modified_row)
                    else:
                        print("Unable to add student " + modified_row + "NO ROLL PRESENT")
        except Exception:
            print("Error: unable to read CSV file")
            traceback.print_exc()
            return None
        return list_student_dictionaries