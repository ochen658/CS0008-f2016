#
# Template for code submission
# name : Hanping Chen
# email : hac105@pitt.edu
# date : 09/06/2016
# class : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# description of this file goes here
# Starting with Python, Chapter 1, Exercise 3
# Notes:
#template

meter = input("How many square meters do you have? ")
print(meter)
acres = meter/4046.8564224
print(acres)
#
print('The distance the car will travel in 6 hours is',6 * 90)
print('The distance the car will travel in 10 hours',10 * 90)
print('The distance the car will travel in 15 hours',15 * 90)
print('The distance the car will travel in 2 hours and 25 minutes',145/60 * 90)

kilometers = float(input("how many miles you drive:"))
gallons = float(input("how many gallons used:"))
fuelconsumption = 100 * gallons / kilometers
print(kilometers)
print(gallons)
print(fuelconsumption)

FTemperature = float(input('temperature in Fahrenheit:'))
CTemperature = 5 * (FTemperature - 32) / 9
print(CTemperature)

cookies = int(input('how many cookies you wnat to make:'))
sugar = 300 / 48 * cookies
buttes = 240 / 48 * cookies
flour = 330 / 48 * cookies
print(sugar)
print(flour)
print(buttes)
