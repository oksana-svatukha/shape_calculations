Code Documentation
This script allows the user to calculate the perimeter and area of various geometric shapes (circle, square, rectangle, triangle) based on user-provided parameters.
Function Descriptions
    1. calculate_circle()
        ◦ Prompts the user for the radius of the circle.
        ◦ Calculates the perimeter and area of the circle.
        ◦ Outputs the results.
    2. calculate_square()
        ◦ Prompts the user for the length of the square's side.
        ◦ Calculates the perimeter and area of the square.
        ◦ Outputs the results.
    3. calculate_rectangle()
        ◦ Prompts the user for the lengths of the rectangle's sides.
        ◦ Calculates the perimeter and area of the rectangle.
        ◦ Outputs the results.
    4. calculate_triangle()
        ◦ Warns the user that it only calculates the area for an equilateral triangle.
        ◦ Prompts the user for the lengths of the triangle's sides.
        ◦ Calculates the semi-perimeter of the triangle.
        ◦ Calculates the perimeter and area of the triangle.
        ◦ Outputs the results.
    5. main()
        ◦ Prompts the user for the name of the shape to calculate.
        ◦ Calls the corresponding function based on the entered shape name.
        ◦ Outputs an error message if the entered shape name is not supported.
Variable Descriptions
    • msg: A string entered by the user, containing the name of the geometric shape.
    • shape_calculations: A dictionary where the keys are shape names and the values are the corresponding functions for their calculations.
Usage Example
    1. The user runs the script.
    2. The script prompts: "What figure do you want to calculate?"
    3. The user enters the name of a shape, for example, "circle".
    4. The script prompts for the corresponding parameters for the calculation (radius for a circle).
    5. The script calculates and outputs the perimeter and area of the circle.
This script provides a convenient and flexible way to calculate the main geometric parameters for different shapes based on user-provided data.
