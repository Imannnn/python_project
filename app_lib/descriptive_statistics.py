from statistics import *
from app_lib.crime_file_reader import *
from app_lib.descriptive_statistics import *
from app_lib.class_calculations import  *



crime_data= CrimeFileReader("car_accidents.xlsx")
crime_data = crime_data.print_all_cell_data()


calc = Calculations()
calc.average_number_of_casualities(crime_data)
calc.average_age_of_casualities(crime_data)
calc.sex_of_casuality(crime_data)
#calc.maximum_number_casualities(crime_data)
calc.junction_control_with_high_casualities(crime_data)
#calc.junction_control_with_low_casualities(crime_data)
calc.weateher_with_high_casualities(crime_data)
calc.lighting_condition(crime_data)

#create a profile of the casuality



# create a scene of when and why accidents happen