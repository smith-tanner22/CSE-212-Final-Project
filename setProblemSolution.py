print()
# Declare a new set called newSet1 and put the values 1, 4, 7, 9, 3, 10 in it and then print it

newSet1 = {1, 4, 7, 9, 3, 10} 
    # Alternatively we can declare a new set like this:
    # newSet1 = set([1, 4, 7, 9, 3, 10])
    # if you put print(type(newSet1)) you will see that they are both sets
print("My new set:")
print(newSet1)
print()

# Add the values 6, 12, 5, 14 to your set and then print it

newSet1.add(6)
newSet1.add(12)
newSet1.add(5)
newSet1.add(14)
print("After Adding:")
print(newSet1)
print()

# Remove the values 7, 3, 12 from your set and then print it

newSet1.remove(7)
newSet1.remove(3)
newSet1.remove(12)
print("After removing:")
print(newSet1)
print()

# Create a second set called newSet2 and put the values 2, 3, 5, 8, 9, 10 in it.
# Then shows the unique values of newSet1 and newSet2 and print it
newSet2 = {2, 3, 5, 8, 9, 10}
print()
print(newSet1) 
print(newSet2)
print()
print("Unique for newSet1:")
print(newSet1 - newSet2)
print()
print("Unique for newSet2:")
print(newSet2 - newSet1)
print()

# Compare the two sets again but this time show the ones they have in common and print it
print("In common for newSet1 and newSet2")
print(newSet1 & newSet2)
print()