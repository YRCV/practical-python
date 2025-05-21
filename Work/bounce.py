# bounce.py
#
# Exercise 1.5
bounces = 1
number_of_bounces = 10
height = 100 # starting height

for bounces in range(1,number_of_bounces+1):
    height *= 3/5
    print(bounces, round(height,4))