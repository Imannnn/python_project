from statistics import *
from app_lib.crime_file_reader import *

reader= CrimeFileReader("California_Gang_Crime.xlsx")
print(reader.print_all_cell_data())
