#creating a key and a list with dictionary
travel_log = {
  "Abeokuta":["Abiola Way", "Idi-Aba", "Olorunsogo"],
  "Ibadan": ["Iwo Road", "Apata", "challenge"],
}
print(travel_log)

# Accessing Individual Element
print("+++++++++++++++++++++++++")
print(travel_log["Abeokuta"][1])

print("++++++++++++++++++++++++++++++")
#creating a dictionary of a dictionary
student_database = {
  "Abdullahi": {'course': "Electrical", 'Sex': "M", "status": "Married"},
  "Abubakar": {'course': "Surveying", 'Sex': "M", "status": "Single"},
}
print(student_database)
## Accessing Element of Dictionary of a Dictionary
print("Course:", student_database["Abdullahi"]["status"])