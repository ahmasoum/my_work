def add(*args):
    total = 0
    for arg in args:
        total+=arg
    print (total)

def func(*args):
    # *args means for however many arguments you take in, it will catch them all
 
    for arg in args:
        print(arg)
         
l = [11,3,4,5,"tuts"]
 
print(func(*l))
################################################################################## 
def capital_cities(**kwargs): 
    # initialize an empty list to store the result
    result = []
    for key, value in kwargs.items():
        result.append("The capital city of {} is {} ".format (key,value))
 
    return result
##################################################################################
def Func(*args,**kwargs):
    for arg in args:
        print (arg)
    for item in kwargs.items():
        print (item)

