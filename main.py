# Working with For loops 
# The for loop in the program is used to compute the len of a list, computation of sum, maximum and minimum of elements in a list

student_height = input("Input list of student height:").split()
#Determination of the len of a list using hardcoding without using the len function
print("Generated List from Inputted value: ", end = "")
print (student_height)
count = 0
sum = 0
max = 0
min = int (student_height[0])
for height in student_height:
  count += 1
  sum += int (height)
  if max < int(height):
    max = int(height)
for height in student_height:
  if min > int(height):
    min = int(height)
print ("Number of entries:",count, ", Sum of entries: ", sum)
print("Maximum Value: ", max, "Minimum Value: ", min)