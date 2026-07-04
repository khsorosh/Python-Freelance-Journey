"""
Lesson 02: Data Types

Objective:
Practice selecting appropriate Python data types and displaying them
using clean, readable output.
"""

username = "johndoe1"
age = 30 
height_meters = 1.70
is_employed = True
salary_annually = 120000.00
has_degree = True
years_experience = 10
current_company = "Goods For You" # The user currently works in this company.

print("User Profile Summary")
print("--------------------")
print(f"Username: {username}")
print(f"Age: {age} years old")
print(f"Height: {height_meters} meters")
print(f"Employed: {is_employed}")
print(f"Salary: ${salary_annually:,.2f} annually")
print(f"Degree: {has_degree}")
print(f"Experience: {years_experience} year(s)")
print(f"Company: {current_company}")