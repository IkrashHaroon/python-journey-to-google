# most common used string functions
# 1. len() - returns the length of the string
name = "Zohaan" 
str_length = len(name)
print(f"The Length of the string {name} is {str_length}")
# 2. lower() - converts the string to lowercas
lower_name = name.lower()
print(f"The lowercase of {lower_name} is {lower_name}")
# 3. upper() - converts the string to uppercase
upper_name = name.upper()
print(f"The uppercase of {name} is {upper_name}")
# 4. endswith() - checks if the string ends with a specific substring
endswith = name.endswith("an")
print(f"Does the string {name} ends with 'an'? {endswith}")
# 5. startswith() - checks if the string starts with a specific substring
startwith = name.startswith("Zoh")
print(f"Does the string {name} ends with 'an'? {startwith}")
# 6. count() - counts the occurrences of a specific substring in the string
count = name.count("a")
print(f"The count of 'a' in {name} is {count}")
# 7. find() - finds the first occurrence of a specific substring in the string
find_index = name.find("a")
print(f"The index of first occurrence of 'a' in {name} is {find_index}")
# 8. capitalize() - capitalizes the first character of the string
capitalized_name = name.capitalize()
print(f"The capitalized version of {name} is {capitalized_name}")
# 9. find() - finds the first occurrence of a specific substring in the string
find = name.find("Z")
print(f"The index of first occurrence of 'Z' in {name} is {find}")
# 10. replace() - replaces a specific substring with another substring in the string
original_string = "Python Journey to Microsoft"
replace_func = original_string.replace("Microsoft", "Google")
print(f"The replaced string is: {replace_func}")