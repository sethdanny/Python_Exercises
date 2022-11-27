#!/usr/bin/python3

money = input("Enter the amount of money to invest in shillings: ")
interest_rate = input("Enter your interest rate: ")

money = float(money)
interest_rate = float(interest_rate) * 0.01

for year in range(10):
    money = money + money * interest_rate

print("The amount of money invested after 10 years is UG shs {:.2f}".format(money))

