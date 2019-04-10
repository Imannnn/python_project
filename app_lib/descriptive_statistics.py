from statistics import *
from app_lib.crime_file_reader import *
from app_lib.descriptive_statistics import *
from app_lib.class_calculations import  *



crime_data= CrimeFileReader("California_Gang_Crime.xlsx")
crime_data = crime_data.print_all_cell_data()


calc = Calculations()
calc.average_murder(crime_data)
calc.top_5(crime_data)
calc.bottom_5(crime_data)