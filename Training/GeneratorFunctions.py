# Uses Yield instead of Return, each time called yields the next value

num_list = [2,4,6,8,10]

def getnumber(x):
    for newvalue in x:
        newvalue +=1
        yield newvalue

for newvalue in getnumber(num_list):
    print(newvalue)

# Create a list of strings
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

# Define generator function get_lengths
def get_lengths(input_list):
    """Generator function that yields the
    length of the strings in input_list."""

    # Yield the length of a string
    for person in input_list:
        yield len(person)

# Print the values generated by get_lengths()
for value in get_lengths(lannister):
    print(value)

