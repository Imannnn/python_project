from app_lib.accident_excel_generator import  CrimeExcelGenerator

class AccidentsItem():
    def __init__(self):
        self.ufo_items = {}  #use a dictionary

    def add_accidents_item(self,item,value):
        self.accidents_items[item] = value  # it will asign a value in the dictionary
    def return_accidentss_item_value(self, key):
        return self. accidents_items[key]

    def delete_accidents_item(self, item):
        del self.accidents_item[item]

    def print_accidents_items(self):
        print(self.accidents_items)

    def save_accidents_items(self, file_name = 'default'):
        self.create_crime_list(self.crime_items)
        self.save_file_as(file_name)
