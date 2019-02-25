# return an error via try-except
def NumOnly (parm) :
    try :
        result = parm ** .5
    except TypeError :
        result = "parm must be a number"
    return result

# return an error via raise
def NumOnly2 (parm) :
    if isinstance(parm,str):
        raise ValueError ("parm must be a number") 

    result = parm ** .5
    
    return result

print(NumOnly2('2'))


