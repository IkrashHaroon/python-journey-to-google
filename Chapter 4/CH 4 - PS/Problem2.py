# Problem Statement: Write a program to take 6 marks as input from the user and store them in a list. Then sort the list and print it.
marks = []

c1 = int(input("Enter Marks here:"))
marks.append(c1)
c2 = int(input("Enter Marks here:"))
marks.append(c2)
c3 = int(input("Enter Marks here:"))
marks.append(c3)
c4 = int(input("Enter Marks here:"))
marks.append(c4)
c5 = int(input("Enter Marks here:"))
marks.append(c5)
c6 = int(input("Enter Marks here:"))
marks.append(c6)
marks.sort()
print("marks in the list:", marks)
