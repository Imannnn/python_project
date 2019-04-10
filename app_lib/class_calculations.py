print("--------------------------Making a calculation method-----------------------------")
import statistics
class Calculations:
    def __init__(self):
        print("Lets start calculations")
    def average(self, data):
        length_of_data = len(data) -1
        if length_of_data < 1:
            raise ValueError('There needs to be at least one observation to calculate the mean')
        sum_of_murder = 0
        for row in data[1:]:
            sum_of_murder += row[1]
        mean = sum_of_murder / length_of_data
        return mean





data = [(1,2,3,4), (2,3,4,1), (2,3,1,3)]

calcs = Calculations()
print(calcs.average(data))





