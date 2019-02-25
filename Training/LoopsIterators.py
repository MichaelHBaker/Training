limit = -8
while limit != 0 :
    print(limit)
    if limit < 0 :
        limit = limit + 1
    elif limit > 0 :
        limit = limit - 1


areas = [["hallway",11.25], ["kitchen",18.0], ["living room",20.0], ["bedroom", 10.75], ["bathroom",9.50]]
house = [["hallway", 11.25],["kitchen", 18.0],["living room", 20.0],["bedroom", 10.75],["bathroom", 9.50]]
iareas = iter(areas)
ihouse = iter(house)
ierr = False
while not(ierr) :
    try :
        print(next(ihouse))
    except :
        ierr = True



for index, a in enumerate(areas) :
    print("room " + str(index+1) + ": " + str(a))
    
         
# # Build a for loop from scratch
# for h in house :
#     print("the " + h[0] + " is " + str(h[1]) + " sqm")



values = range(10,21)
print(values)
lvalues = list(values)
print(lvalues)
print(sum(lvalues))

