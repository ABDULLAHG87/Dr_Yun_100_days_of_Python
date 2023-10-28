#write your code below this line
import math 
def paint_calc(height, width, cover):
  number_of_cans = math.ceil((height * width) / cover)
  print(f"You will need {number_of_cans} cans of paints")


#write your code aboe this line
#define a function called paint_calc() so the code below works

#don't change the code below
test_h = int(input()) #height of wall (m)
test_w = int(input()) #width of wall (m)
coverage =5
paint_calc(height = test_h, width = test_w, cover = coverage)