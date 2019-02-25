x = 10
def change_x (y):
    global x
    x = y **2
    return x
print(change_x(x))

import builtins
dir(builtins)
