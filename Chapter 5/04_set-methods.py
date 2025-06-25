s = {1,67,34,2,1,4,1,"Ikrash"}
print(s, type(s))

s.add(35)
print(s, type(s))
 
# Now i will come to chatgpt and i will say give me some most important set methods in python
# This is a code provided by ChatGPT
# Set creation
set_a = {1, 2, 3}
set_b = {3, 4, 5}

print("Initial Sets:")
print("Set A:", set_a)
print("Set B:", set_b)


# 1. update()
set_a.update([7, 8])
print("After update([7, 8]):", set_a)

# 2. remove()
set_a.remove(1)
print("After remove(1):", set_a)

# 3. discard()
set_a.discard(10)  # No error even if 10 is not in set
print("After discard(10):", set_a)

# 4. pop()
popped = set_a.pop()
print(f"Popped element: {popped}")
print("After pop():", set_a)

# 5. clear() - We'll demonstrate this on a new set
temp_set = {100, 200}
temp_set.clear()
print("After clear():", temp_set)

# 6. union()
union_set = set_a.union(set_b)
print("\nUnion of A and B:", union_set)

# 7. intersection()
intersection_set = set_a.intersection(set_b)
print("Intersection of A and B:", intersection_set)

# 8. difference()
diff_set = set_a.difference(set_b)
print("Difference A - B:", diff_set)

# 9. symmetric_difference()
sym_diff = set_a.symmetric_difference(set_b)
print("Symmetric Difference:", sym_diff)

# 10. issubset()
subset_result = {3, 4}.issubset(set_b)
print("\nIs {3, 4} subset of Set B?", subset_result)

# 11. issuperset()
superset_result = set_b.issuperset({3})
print("Is Set B superset of {3}?", superset_result)

# 12. isdisjoint()
disjoint_result = set_a.isdisjoint({99, 100})
print("Is Set A disjoint with {99, 100}?", disjoint_result)
