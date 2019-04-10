from app_lib.crime_excel_generator import  CrimeExcelGenerator

class CrimeItem():
    def __init__(self):
        self.ufo_items = {}  #use a dictionary

    def add_crime_item(self,item,value):
        self.ufo_items[item] = value  # it will asign a value in the dictionary
    def return_crime_item_value(self, key):
        return self. crime_items[key]

    def delete_crime_item(self, item):
        del self.crime_item[item]

    def print_crime_items(self):
        print(self.crime_items)

    def save_crime_items(self, file_name = 'default'):
        self.create_crime_list(self.crime_items)
        self.save_file_as(file_name)
