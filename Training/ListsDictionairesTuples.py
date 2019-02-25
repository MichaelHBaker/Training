#tuples used to return multiple values from a function, element values are immutable
a_tuple = (1,2,3) #define with (), not like a list, but address a cell with [], like a list
print(a_tuple[1])
print(type(a_tuple))
a_list = [1,2,3]
print(type(a_list))
a,b,c = a_tuple
print(a)

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
# for k,v in europe.items() :
#     print("the capital of " + k + " is " + v)

a = [1,2,3]
a = a + [4]
print(a)

europe.update({'japan':'Tokyo'})
europe['japan'] = 'tokyo'

europe_list = list(enumerate(europe)) #creates list of the key values with an index from 0-n, a list of tuples
print(europe_list)
    
