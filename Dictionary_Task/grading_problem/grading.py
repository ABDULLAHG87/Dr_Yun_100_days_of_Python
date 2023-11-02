student_scores = {
  'Harry': 81,
  'Ron': 78,
  'Hermione': 99,
  'Draco': 74,
  'Neville': 62,
}

#TODO-1: create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write you code below to add thegrades to student_grades
# student_scores >=
for score in student_scores:
  if 91 <= student_scores[score] <= 100:
    student_grades[score] = "Outstanding"
  elif 81 <= student_scores[score] <= 90:
    student_grades[score] =  "Exceeds Expectation"
  elif 71 <= student_scores[score] <= 80:
    student_grades[score] =  "Acceptable"
  else:
    student_grades[score] =  "Fail"
    
print(student_grades)