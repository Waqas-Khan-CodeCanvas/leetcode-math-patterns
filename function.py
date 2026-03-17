"""
topic -> functions:
    definition:
        set of instruction a block of code that perform a specifi a single task.
        is a reuseable part of code
    
    general syntax :
    def func_name(value / var):  value , var -> parameters
        func_body
        
        return
    func_calling(values/ var)  values , var -> arguments
    
    types of function 
        i ->  built-in
        ii -> user defined function
        
    parameter and arguments
    
    types of arguments
        i -> positionanl arguments and positional only arguments
        ii -> keyword arguments and keyword only arguments
        iii -> defalt parameters
        iv -> arbitrary arguments *args and **kawargs 
    
    variable scope (local , global , nonlocal) 
    function annotations   
    function as a modules    
        
    types of user defined functions
        simple function
        callback function
        recursive function
        heigh order function
        first class function
        ananymous function (lambda)
        clousers of a function
        hoisting of a function
        memoization of a function
        
    practice questions
    
    1 :- count string charcters
    2 :- reverse string in memory replacement
    3 :- reverse vowels in a string 
    4 :- count sum of digits in a number
    5 :- reverse even digits of a number 
    6 :- length of the last word in a string        
    
"""


# a = 5
# b = 20

# sum = a + b
# print(sum)

def add():
    a = 5
    b =10
    sum = a +b
    print(f"sum of a + b is {sum}")

# add()

# number_list = [1,2,3,4,5,6,7,8,10]
# result = sum(number_list)
# print(f"sum of number_list is : {result}")


# parameters and arguments

# def greet():
#     print("my name is ali and i'm from cs department")

# greet()    

# def greetAhmad():
#     print("my name is ahmad and i'm from cs department")
    
    
# def greetAhmadDS():
#     print("my name is ahmad and i'm from ds department")
    
    
def greet(name="test_user",department="test_department"): # name -> parameter
    print(f"my name is {name} and i'm from {department} department")

name = "zaryab khan"
department = "cs"
# greet(name , department)   # name ->  argument 
# greet("ali" , "ds")   # ali ->  argument 
# greet("ahmad" )   # ahmad ->  argument 
# # greet()  


# positional arguments 
# TODO: change order of these arguments
# greet(department=department, name=name)

# default paramentes
# greet()  


# keyword only 
def add( a , * ,b):
    print(a ,b)
    
# add(2 ,3) 
# add(2 ,b=3) 

def mult( a  , / ,b ):
    print(a , b, )   
# mult(a=3, b=3)
# mult(3, b=3)



# arbitrary arguments
def avg(*numbers):
    avrage = int(sum(numbers) / len(numbers))
    print(avrage)

avg(1,2,3,4,5,6,7,8,9,10) 

def percentage(math , sci , **optional_subjects):
    print(f"Maths marks is : {math}")
    print(f"Science marks is : {sci}")
    
    total = 600
    sum = math + sci
    
    for k , v  in optional_subjects.items():
        print(f" {k} -> {v}")
        sum  += v
    
    result = (sum / total) * 100
    return result
    
# math=80, sci=75, Eng=70, Hist=65, Geo=72 , Urd=80
# math and sci complasary
result = percentage(math=90 , sci=80 , Eng=70, Hist=65, Geo=72 , Urd=80)
# result = percentage(math=100 , sci=100 , Eng=100, Hist=100, Geo=100 , Urd=100)


print(f"your percentage is : {round(result , 1)}%")