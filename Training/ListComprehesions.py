squares = [i**2 for i in range(0,10)]
print(squares)

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
# new_fellowship = [member if len(member) >= 7 else '' for member in fellowship]
new_fellowship = [member for member in fellowship if len(member)>= 7]
# Print the new list
print(new_fellowship)

# Create dict comprehension: new_fellowship
new_fellowship = {member:len(member) for member in fellowship}

# Print the new list
print(new_fellowship)
