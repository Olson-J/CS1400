# program to find and print the distance needed
# to stretch an elastic in order to launch an egg
# over Old Main. Program asks user for two floats
# 'D' and 'theta'
# mass of egg = 0.065kg, elastic constant = 25N/M
# grav. constant = 9.8 M/(s^2)
###############################
# input: two floats
# output: distance x
###############################
# M = 0.065 kg
# G = 9.8 M/(s^2)
# K = 25 N/M
# D = eval(input("How many meters away is the professor?: "))
# T = eval(input("What is the angle of theta?: "))
# mult T by 2
# convert T to radians
# Mult T by sin
# denom = mult K by T
# num = m * g * d
# x = sqrt of (divide num by denom)
# print X
################################

import math

#given variables
mass = 0.065
grav = 9.8
kCon = 25

#user input
dis = eval(input("How many meters away is the professor?: "))
theta = eval(input("What is the angle of theta in degrees? "))

#math for (2theta)
theta = theta * 2
rad = math.radians(theta)
sin = math.sin(rad)

#math for denominator and numerator
denom = kCon * sin
num = mass * grav * dis

#square root of fraction and print statement
x = math.sqrt(num / denom)
print("You need to pull the elastic back ", x, " meters")