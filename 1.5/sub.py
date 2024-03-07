class Height:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __sub__(self, other):
        total_height1 = self.feet * 12 + self.inches
        total_height2 = other.feet * 12 + other.inches
        result_height = total_height1 - total_height2
        
        feet_result = result_height // 12
        inches_result = result_height % 12

        return Height(feet_result, inches_result)

    def __str__(self):
        return f"{self.feet} feet {self.inches} inches"

height1 = Height(5, 10)
height2 = Height(3, 9)

result = height1 - height2
print("Result:", result)