#!/usr/bin/python3

def milesToKilometers(miles):
    kilometers = miles * 1.60934
    return kilometers

miles = input("Enter the number of miles: ")
miles = int(miles)

result = milesToKilometers(miles)
print("{} Mile(s) is equal to {} Kilometers".format(miles, result))



