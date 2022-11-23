# write your code below this line

import math
def paint_calc(height, width, cover):
    paints_needed = math.ceil((height * width) / cover)
    print(f"You will need {paints_needed} cans of paint.")

# Don't change the code below this line
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height = test_h, width = test_w, cover = coverage)

