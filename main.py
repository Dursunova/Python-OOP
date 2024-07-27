from os.path import exists
from datetime import datetime

if not exists("table.txt"):
    with open("table.txt", "w") as file:
        file.write("Function Name | Worked Time |  Arguments |  Keyword Arguments | results \n")

def logger(func):
    def inner(*args,**kwargs):
        try:
            result=func(*args,**kwargs)
            result_str=str(result)
        except ZeroDivisionError as e:
            result_str=str(e)

        func_name=f"{func.__name__:<16}"
        worked_time=f"{datetime.now()}"
        args_str=",".join(map(str,args))
        kwargs_str=",".join(f"{key}={value}" for key,value in kwargs.items())


        with open("table.txt","a") as file:
            file.write(f"{func_name:<8} |{worked_time:<16} |{args_str} | {kwargs_str} | {result_str} \n")


    return inner

@logger
def sum(a,b):
    return a+b

@logger
def divide(a,b):
    return a/b

sum(3,2)
divide(a=4,b=2)