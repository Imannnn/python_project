from openpyxl import load_workbook
from app_lib.class_data import Crime


class AccidentsFileReader:

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
            list.append(row)
        return list[1:]



    def print_all_data_cells_coordinates(self):
        for i in self.worksheet.rows:
            for p in i:
                print(p.coordinate)

reader= AccidentsFileReader("car_accidents.xlsx")
print(reader.print_all_cell_data())