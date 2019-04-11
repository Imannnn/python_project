from statistics import *
from app_lib.crime_file_reader import *
from app_lib.descriptive_statistics import *
from app_lib.class_calculations import  *



crime_data = CrimeFileReader("car_accidents.xlsx")
crime_data = crime_data.print_all_cell_data()
calc = Calculations()

print("--------------------------------------------------------------------------------------------------------")
print("                                                 Car accidents in the UK ")
print("--------------------------------------------------------------------------------------------------------")
input()
print("The UK was amongst the bottom 25 countries for the number of casualities in car accidents  ")
input()
print("Though the UK was amongst the bottom 25, we were still beaten by countries like the Maldives, Norway,"
      " Malta, Sweden and 10 other countries ")
input()
print("I have obtained data from the British governments site for car accidents in 2017")
input()
print("Let us explore why car accidents happen in the UK")
input()

print("--------------------------------------------------------------------------------------------------------")
print("                                                 Descriptive Statistics ")
print("--------------------------------------------------------------------------------------------------------")
input()
calc.average_number_of_casualities(crime_data)
input()

print("--------------------------------------------------------------------------------------------------------")
print("                                                 User input ")
print("--------------------------------------------------------------------------------------------------------")
input()
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
print("                                                What causes car accidents? ")
print("--------------------------------------------------------------------------------------------------------")
input()
print("The hypothesis: Signs such as the stop signs are likely to have high number of accidents. Is this true?")
input()
calc.junction_control_with_high_casualities(crime_data)
input()
print("So the hypothesis is partially true, since only one sign had the highest number of accidents")
input()
print("Is it possible that the lighting conditions at the time of the accident was bad")
input()
calc.lighting_condition(crime_data)
input()
print("Hmmmm, I would of thought give way signs were less visible during night time. "
      "However, it seems the lighting conditions were good")
input()
print("Could it possibly be  ")
calc.weateher_with_high_casualities(crime_data)
input()






# create a scene of when and why accidents happen