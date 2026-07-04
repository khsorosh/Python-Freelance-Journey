"""
Lesson 03: Strings

Objective:
Practice accessing individual characters and transforming text using
common string operations.
"""

full_name = "john doe"
favorite_language = "python"
favorite_editor = "visual studio code"

print(f"{'Display Summary':^36}")
print("====================================")
print(f"Full name: {full_name:>15}")
print(f"|-> Uppercased: {full_name.upper():>10}")
print(f"|-> Title cased: {full_name.title():>9}")
print(f"|-> First letter: {full_name[0]}")
print(f"|-> Last letter: {full_name[-1]:>2}")
print("************************************")
print(f"Favorite language: {favorite_language}")
print(f"|-> Uppercased: {favorite_language.upper():>9}")
print(f"|-> First letter: {favorite_language[0]:>2}")
print("************************************")
print(f"Favorite editor: {favorite_editor}")
print(f"|-> Title cased: {favorite_editor.title()}")
