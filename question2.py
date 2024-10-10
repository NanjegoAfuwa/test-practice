#using a function create a program that creeates avolume of cylinder

radius = int (input("Enter the number of radius of the cylinder:"))
height = int(input("Enter the number of height of the cylinder:"))
volume = 3.14 * radius**2
print(f"the volume of the cylinder: {volume}")


#approach 2 
import math
pie = math.pi
volume = pie * radius**2 * height
print(volume)

