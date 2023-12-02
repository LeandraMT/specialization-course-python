class Height(object):
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __str__(self):
        output = str(self.feet) + " feet, " + str(self.inches) + " inches"
        return output

    def __add__(self, other):
        height_A_inches = self.feet * 12 + self.inches
        height_B_inches = other.feet * 12 + other.inches

        total_height_inches = height_A_inches + height_B_inches
        output_feet = total_height_inches // 12
        output_inches = total_height_inches - (output_feet * 12)

        return Height(output_feet, output_inches)

    def __sub__(self, other):
        height_C_inches = self.feet * 12 + self.inches
        height_D_inches = other.feet * 12 + other.inches

        total_height_inches = height_C_inches - height_D_inches
        output_feet = total_height_inches // 12
        output_inches = total_height_inches % 12

        return Height(output_feet, output_inches)

    def __gt__(self, other):
        height_E_inches = self.feet * 12 + self.inches
        height_F_inches = other.feet * 12 + other.inches

        return height_E_inches > height_F_inches

    def __ge__(self, other):
        height_G_inches = self.feet * 12 + self.inches
        height_H_inches = other.feet * 12 + other.inches

        return height_G_inches >= height_H_inches

    def __ne__(self, other):
        height_I_inches = self.feet * 12 + self.inches
        height_J_inches = other.feet * 12 + other.inches

        return height_I_inches != height_J_inches


# Addition
person_A_height = Height(5, 10)
person_B_height = Height(4, 10)
height_sum_A_B = person_A_height + person_B_height

# Subtraction
person_C_height = Height(5, 11)
person_D_height = Height(3, 9)
height_sum_C_D = person_C_height - person_D_height

print("Total height from person A and B: ", height_sum_A_B)
print("Total height from person C and D: ", height_sum_C_D)

# Greather than
result_E_and_F = Height(5, 6) > Height(8, 10)
print("Is Height 5, 6 greater than height 8, 10?: ", result_E_and_F)

# Greather than or equal to
result_G_and_H = Height(3, 6) >= Height(3, 6)
print("Is Height 3, 6 greater than or equal to height 3, 6?: ", result_G_and_H)

# Not equal to
result_I_and_J = Height(5, 11) != Height(5, 10)
print("Is Height 5, 11 not equal to height 8, 10?: ", result_I_and_J)
