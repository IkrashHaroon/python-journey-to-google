name = "Im  Ikrash  Haroon" # Name string has not change, Strings are immutable
print(name) # Output: Im  Ikrash  Haroon


# it has been printed as a new string
# because strings are immutable in Python
# So this function makes a new string and prints it, It does nit change your original string
print(name.replace("  ", " ")) # Output: Im Ikrash Haroon bcz it replaces double spaces with single space