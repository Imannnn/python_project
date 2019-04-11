from statistics import *
from app_lib.crime_file_reader import *
from app_lib.descriptive_statistics import *
from app_lib.class_calculations import  *



crime_data = CrimeFileReader("car_accidents.xlsx")
crime_data = crime_data.print_all_cell_data()
calc = Calculations()
print("--------------------------------------------------------------------------------------------------------")
print("                                                 Descriptive Statistics ")
print("--------------------------------------------------------------------------------------------------------")
calc.average_number_of_casualities(crime_data)

print("--------------------------------------------------------------------------------------------------------")
print("                                                 User input ")
print("--------------------------------------------------------------------------------------------------------")
a = input("What gender do we think is most likely to be in accident")
if a == "male":
    print(True)
elif a == "=female":
    print(False)
else:
    print("Lets find out")

input()
print("--------------------------------------------------------------------------------------------------------")
print("                                                Casuality profile ")
print("--------------------------------------------------------------------------------------------------------")
input()
calc.average_age_of_casualities(crime_data)
input()
calc.sex_of_casuality(crime_data)
input()

print("--------------------------------------------------------------------------------------------------------")
print("                                                What causes accidents? ")
print("--------------------------------------------------------------------------------------------------------")
input()
calc.junction_control_with_high_casualities(crime_data)
input()
calc.weateher_with_high_casualities(crime_data)
input()
calc.lighting_condition(crime_data)

input()





# create a scene of when and why accidents happen