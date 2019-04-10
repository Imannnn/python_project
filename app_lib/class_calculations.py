from statistics import *
# print("--------------------------Making a calculation method-----------------------------")

class Calculations:
    def __init__(self):
        print("Lets start calculations")

    def introduction(self):
        print("Lets get started with some statistical analysis")

    def average_murder(self, data):
        print("The average murders in California is:")
        length = len(data)
        total_murders = 0
        for item in data[1:]:
            total_murders += item[1]
        average = round(total_murders/ length )
        print(average)

    def sum_of_square(self,data):
        return stdev(data)

    def top_5 (self,data):
        print("The 5 years with the highest murder numbers are: ")
        for item in data[1:]:
            if item[1] > 3550:
                print(str(item[0]) + " " + str(item[1]))

    def bottom_5(self,data):
        print( "The 5 years with the lowest murder numbers are: ")
        for item in data[1:]:
            if item[1] <= 2010:
                print(str(item[0]) + " " + str(item[1]))





