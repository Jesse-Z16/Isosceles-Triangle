# ask for the length of sides
# figure out if its an isosceles triangle
#print if it is or if its not isosceles

side1 = int(input('how long is the first side of the triangle:'))
side2 = int(input('how long is the second side of the triangl:'))
side3 = int(input('how long is the third side of the triangle:'))

if side1 == side2 or side2 == side3:
    print('The triangle is isosceles')
else:
    if side1 == side3 or side3 == side2:
        print('The triangle is isosceles')
    else:
        print('Triangle is not isosceles')
    