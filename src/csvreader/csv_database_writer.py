'''
Created on 22-Jul-2015

@author: siddhanthgupta
'''
import csv

class CsvDatabaseWriter:
    '''
    classdocs
    '''


    def __init__(self, *fieldnames):
        '''
        Constructor
        '''
        self.fieldnames = fieldnames
        
    '''
    @param     dictionary_students     A list of dictionaries, where each dictionary corresponds 
                                       to a single student
    @param     filename                The name of the file to which the list of students is to be written
    '''
    def dictionaryListToCsv(self, filename, *dictionary_students):
        with open(filename, 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames = self.fieldnames, extrasaction = 'ignore')
            writer.writeheader()
            for row in dictionary_students:
                writer.writerow(row)