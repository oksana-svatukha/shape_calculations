import math

def calculate_circle():
    radius = float(input('Please write radius... '))
    perimeter = round((2 * math.pi * radius), 2)
    area = round((math.pi * (radius ** 2)), 2)
    print(f'Perimeter of circle = {perimeter} sm\nArea of circle = {area} sm²')

def calculate_square():
    side_a = float(input('Please write sideA... '))
    perimeter = round((4 * side_a), 2)
    area = round((side_a ** 2), 2)
    print(f'Perimeter of square = {perimeter} sm\nArea of square = {area} sm²')

def calculate_rectangle():
    side_a = float(input('Please write sideA... '))
    side_b = float(input('Please write sideB... '))
    perimeter = round((2 * (side_a + side_b)), 2)
    area = round((side_a * side_b), 2)
    print(f'Perimeter of rectangle = {perimeter} sm\nArea of rectangle = {area} sm²')

def calculate_triangle():
    input('I can calculate only the area for an equilateral triangle write "yes" if you want to continue...')
    side_a = float(input('Please write sideA... '))
    side_b = float(input('Please write sideB... '))
    side_c = float(input('Please write sideC... '))
    half_per = (side_a + side_b + side_c) / 2
    perimeter = round((side_a + side_b + side_c), 2)
    area = round(math.sqrt(half_per * (half_per - side_a) * (half_per - side_b) * (half_per - side_c)), 2)
    print(f'Perimeter of triangle = {perimeter} sm\nArea of triangle = {area} sm²')

def main():
    shape_calculations = {
        'circle': calculate_circle,
        'square': calculate_square,
        'rectangle': calculate_rectangle,
        'triangle': calculate_triangle
    }

    msg = input("What figure do you want to calculate?").lower()

    if msg in shape_calculations:
        shape_calculations[msg]()
    else:
        print('Something went wrong, please write correct!')

if __name__ == "__main__":
    main()