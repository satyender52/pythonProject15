def calculate_area():
    base = float(input("Enter the base length of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    return area

# Example usage:
triangle_area = calculate_area()
print("Area of the triangle:", triangle_area)
