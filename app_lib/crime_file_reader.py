from openpyxl import load_workbook
from app_lib.class_data import Crime


class CrimeFileReader:

    def __init__(self, file_name_and_path):
        self.workbook = load_workbook(file_name_and_path, read_only=True)
        self.worksheet = self.workbook.active

    def return_cell_value(self, cell_reference):
        return self.worksheet[cell_reference].value

    def print_worksheet(self):
        for item in self.worksheet:
            print(item)

    def print_all_cell_data(self):
        list = []
        for row in self.worksheet.values:
            dict_data= { "Year" : row[0], "Violent_Crime": row[1] , "Murder": row[2], "Robbery":row[3], "Population":row[4]}

            list.append(dict_data)
        return list[1:]



    def print_all_data_cells_coordinates(self):
        for i in self.worksheet.rows:
            for p in i:
                print(p.coordinate)

reader= CrimeFileReader("California_Gang_Crime.xlsx")
print(reader.print_all_cell_data())