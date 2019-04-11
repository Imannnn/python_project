import math
# print("--------------------------Making a calculation method-----------------------------")

class Calculations:
    def __init__(self):
        print("")

    def introduction(self):
        print("Lets get started with some statistical analysis")

    def average_number_of_casualities(self, data):
        print("The average number of casualities in the UK is:")
        length = len(data)
        total_number_of_casualities = 0
        for item in data[1:]:
            total_number_of_casualities += item[2]
        average = round(total_number_of_casualities/ length )
        print(average)

    def average_age_of_casualities(self, data):
        print("The average age of casualities in the UK is:")
        length = len(data)
        total_age_of_casualities = 0
        for item in data[1:]:
            total_age_of_casualities += item[9]
        average = round(total_age_of_casualities/ length )
        print(average)



    def sex_of_casuality (self, data):
        print("The gender with the highest number of casuilities is:")
        for item in data[1:]:
            if item[1] == 11:
                print( "Gender: " + str(item[8]))


    def junction_control_with_high_casualities(self,data):
        print("The junction(s) with the highest number of casualties in 2017 are: ")
        for item in data[1:]:
            if item[1] == 11:
                print( "Junction control: " + str(item[3]))


    def weather_with_high_casualities (self, data):
        print("The weather condition with the highest number of accidents is:")
        for item in data[1:]:
            if item[1]== 11:
                print("Weather condition:" + str(item[5]))

    def lighting_condition(self,data):
        print("The lighting condition with the highest number of accidents is:")
        for item in data[1:]:
            if item[1] == 11:
                print("Lighting condition:" + str(item[4]))











