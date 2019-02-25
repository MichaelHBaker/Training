# * replicates strings
"abc" * 3
# + throws error on int and str
#"abc" + 3
# + works with float and int
1.1 + 3
# lists
a= ["string" * 3, True, 1, 2.2]
print(a)

hall = 20
bath = 50
bedroom = 100
house = [
            ["Hall",hall], 
            ["Bath",bath],
            ["bedroom", bedroom]]
print(house[0][0])

v1 = 20
v2 = 50
v3 = 100
a = [
        ["Hall",v1],
        ["Bath", v2],
    ["bedroom", v3]
    ]
print(a)


# type
print(type(house))
# list index starts with 0, negative indexes allowed
print(a[-1])
# list[start:end], blank = all such as
print(a[-2:])
#lists can contain lists, addressed by successive [][]
nested = [
            [1,2,3,4,5],
            [6,7,8,9,10],
            [11,12,13,14,15]
          ]
print(nested[0][0])
# + operator appends lists
list1 = ["a","b","c"]
list2 = ["d","e"]
list3 = list1+list2
print(list3)
#del operator
del(list3[-1])
print(list3)
# = operator makes a pointer to a list, so if you change either one you change both
list1_copy = list1
list1_copy[0]="z"
print (list1)
# use the list() function, not really a funciton but it works like one, on all cells [:] to force an actual copy
list1_copy = list1[:]
list1_copy[0] = "z"
list1_copy = list(list1)
var1 = [1, 2, 3, 4]
varchar = "This is a string"
print(len(varchar))
print(int(False))
help(max)
print(max(list1))
lstInt = [1,2,3,4]
lstBool = [True,True,False,False]
lstStr = ["a","b","c"]
# it will concatnate mixed types but the sort will not work
lstAll = lstInt+lstStr
print(sorted(lstAll))
# string by itself is a type conversion, but is also has a collection of methods, which are separate functions
print(str.count("How many o's are in this string","o"))
# similarly list(), bool(), float(), int() all have method collections
# search for element in a list with index
print(list.index(lstInt,3))
print(list.count(lstInt,3))
# a list inherits methods
lstInt.append(5)
print(lstInt)
# import a package
import math
print(math.sqrt(4))
# you can import just a single function from a package
from math import radians
# numpy supports math on lists
import numpy as np
var1 = [2,4,6,8]
# can multiply by a constant for example
var2 = [10,20,30,40]
np_var1 = np.array(var1)
print(np_var1*2)
# can just multiply the two np arrays
np_var2 = np.array(var2)
np_var3 = np_var1 * np_var2
print(np_var3)
# adding two python lists appends, but adding to numpy list accumulates the cells, but the numpy arrays must have the same shape
a = [1,2,3,4] # if you add a 5th element, the numpy add below throws an error
b = [10,20,30,40]
npa = np.array(a)
npb = np.array(b)
print(a+b)
print(npa+npb)
# There are also methods
np_var3 = np.multiply(var1,var2)*2
help (np.multiply)
# numpy lists (arrays) can be subset with criteria
var2 = [10,20,30,40]
np_var2 = np.array(var2)
np_var2_bool = np_var2 >20 #creates a list of true / false values
print (np_var2[np_var2_bool])
# numpy 2D arrays
a = [[1,2,3,4,5,6],[10,20,30,40,50,60]]
print(a[0][0], a[0][1])
z = a[0][0]
anp = np.array(a)
print(anp*2)
print(anp[0,:]*anp[1,:]) #this multiplies one dimension of the array by the other
# numpy has library of functions
import numpy as np
np.average(a)