# Indicate generators with () as opposed to list [] or dictionaries {}
#   Different than tuples, which are listes of immutable element values (1,2,3,4)
#   List comprehesions [] populate the entire list in memory, genertors only create value when called
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']
fellow2 = (member for member in fellowship if len(member)>=7)
for i in fellow2 :
    print(i)

i = (2 * n for n in range(50))
print(next(i)) # prints the first generated values
for y in i: # continues on with the second through the last
    print(y)

# Create a list of strings: lannister
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

# Create a generator object: lengths
lengths = (len(person) for person in lannister)

# Iterate over and print the values in lengths
for value in lengths:
    print(value)
