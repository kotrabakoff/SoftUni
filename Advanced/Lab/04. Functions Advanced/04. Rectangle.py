def rectangle(length, width):
    check_length = isinstance(length, int)
    check_width = isinstance(width, int)
    def __init__(self, length, width):
        self.length = length
        self.width = width


    if check_length and check_width:
        def area(length, width):
            final_area = length * width
            return f"Rectangle area: {final_area}"

        def perimeter(length, width):
            final_perimeter = (length + width) * 2
            return f"Rectangle perimeter: {final_perimeter}"



    else:
        return "Enter valid values!"

print(rectangle(2, 10))