def nested(value):
    new_value = value*10
    return(new_value)
def test(value1, value2):
    """Returns the cube of value"""
    new_value = nested(value1)**value2
    new_value2 = nested(value2)**value1
    a_tuple = (new_value,new_value2)
    return(a_tuple)
x1, x2 = test(3,2)
print(x1,x2)

# Example of a function returning a pointer to an inner function
def echo(n):
    """Return the inner_echo function."""

    # Define inner_echo
    def inner_echo(word1):
        """Concatenate n copies of word1."""
        echo_word = word1 * n
        return echo_word

    # Return inner_echo
    return inner_echo

# Call echo: twice
twice = echo(2) #the type of twice is <class 'function'>

# Call echo: thrice
thrice = echo(3)

# Call twice() and thrice() then print
print(twice('hello'), thrice('hello')) #so they can be called as if there were a function by that name

# One argument with default value, which makes it optional in the call
def shout_echo(word1, echo=1):
    """Concatenate echo copies of word1 and three
     exclamation marks at the end of the string."""

    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo

    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'

    # Return shout_word
    return shout_word

# Call shout_echo() with "Hey": no_echo
no_echo = shout_echo("Hey")


# Call shout_echo() with "Hey" and echo=5: with_echo
with_echo = shout_echo("Hey", 5)

# Print no_echo and with_echo
print(no_echo)
print(with_echo)

# Import reduce from functools
from functools import reduce

# Create a list of strings: stark
stark = ['robb', 'sansa', 'arya', 'brandon', 'rickon']

# Use reduce() to apply a lambda function over stark: result
result = reduce(lambda item1,item2 : item1+item2, stark)

# Print the result
print(result)