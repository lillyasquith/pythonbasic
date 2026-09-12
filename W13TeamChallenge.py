import math

def compute_area_square(side):
    """Calculate area of a square"""
    square_area = float(side ** 2)
    return square_area

def compute_area_rectangle(length, width):
    """Calculate area of a rectangle"""
    rec_area = float(length * width)
    return rec_area

def compute_area_circle(radius):
    """Calculate area of a circle"""
    cir_area = float(math.pi *  radius ** 2)
    return cir_area


# shape = ""
# while shape != "quit":
#     shape = input("What kind of shape would you like to choose? ").lower()

#     if shape == "square":
#         square_side = float(input("What is the side length of the square? "))
#         print(f"The area of the square is: {compute_area_square(square_side):.2f} \n")

#     elif shape == "rectangle":
#         rec_length = float(input("What is the length of the rectangle? "))
#         rec_width = float(input("What is the width of the rectangle? "))
#         print(f"The area of the rectangle is: {compute_area_rectangle(rec_length, rec_width):.2f}\n")

#     elif shape == "circle":
#         circle_radius = float(input("What is the radius of the circle? "))
#         print(f"The area of the cicle is: {compute_area_circle(circle_radius):.2f}")


print("=" * 20)
print("Stretch Challenge")
print("=" * 20)

# Change your program so that the compute_area_square function doesn't compute the area directly, but instead calls the compute_area_rectangle to do the work
def compute_area_square(side):
    return compute_area_rectangle(side, side)

# print(compute_area_square(2))

# Write a new function called compute_area that accepts a first parameter of shape that can be either "square" or "circle" and then a value for the length of the side or the radius depending on the context. 
def compute_area(shape, value1, value2=None): #value2 is optional
    if shape == "square":
        return compute_area_square(value1)
    elif shape == "circle":
        return compute_area_circle(value1)
    # Add the ability for your new compute_area function to also compute the areas for rectangles.
    elif shape == "rectangle":
        return compute_area_rectangle(value1, value2)

# area_square = compute_area("square", 10)
# area_circle = compute_area("circle", 5)
# area_rectangle = (compute_area("rectangle", 7, 8))

# print(f"The area of the square is: {area_square:.2f}")
# print(f"The area of the circle is: {area_circle:.2f}")
# print(f"The area of the rectangle is: {area_rectangle:.2f}")

shape = ""
while shape != "quit":
    shape = input("What kind of shape would you like to choose? ").lower()

    if shape == "square":
        square_side = float(input("What is the side length of the square? "))
        area_square = compute_area("square", square_side)
        print(f"The area of the square is: {area_square:.2f} \n")

    elif shape == "rectangle":
        rec_length = float(input("What is the length of the rectangle? "))
        rec_width = float(input("What is the width of the rectangle? "))
        area_rectangle = (compute_area("rectangle", rec_width, rec_length))
        print(f"The area of the rectangle is: {area_rectangle:.2f} \n")

    elif shape == "circle":
        circle_radius = float(input("What is the radius of the circle? "))
        area_circle = compute_area("circle", circle_radius)
        print(f"The area of the cicle is: {area_circle:.2f} \n")