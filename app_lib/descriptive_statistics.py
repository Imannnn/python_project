from statistics import *
from app_lib.crime_file_reader import *
from app_lib.descriptive_statistics import *
from app_lib.class_calculations import  *



crime_data= CrimeFileReader("car_accidents.xlsx")
crime_data = crime_data.print_all_cell_data()


calc = Calculations()
calc.average_number_of_casualities(crime_data)
calc.junction_control_with_high_casualities(crime_data)
#calc.junction_control_with_low_casualities(crime_data)
