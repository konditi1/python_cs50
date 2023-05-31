"""
In a file called einstein.py, implement a program in Python that prompts
the user for mass as an integer (in kilograms) and then outputs the
equivalent number of Joules as an integer. Assume that the user will input
an integer.E =mc^2
"""
def energy_cal(mass):
    c = 300000000
    return (mass * c **2)

E = int(input("m: "))
print("E: ", energy_cal(E))