from statistics import *
from itertools import groupby
# print("--------------------------Making a calculation method-----------------------------")

class Calculations:
    def __init__(self):
        print("Lets start calculations")

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

    def maximum_number_casualities(self,data):
        print("The maximum number of casualties in 2017 was: ")
        for item in data[1:]:
            maximum = max(item[3])
            print(maximum)

    def junction_control_with_high_casualities(self,data):
        print("The junction(s) with the highest number of casualties in 2017 are: ")
        for item in data[1:]:
            if item[1] == 11:
                print( "Junction control: " + str(item[3]))

    # def junction_control_with_low_casualities(self,data):
    #     print( "The junction(s) with the lowest number of casualties in 2017 are: ")
    #     for item in data[1:]:
    #         if item[1] <= 3:
    #
    #             print(item[3].count("Give way"))










