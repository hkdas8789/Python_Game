# from win32com.client import Dispatch
#
# def speak(str):
#     speak=Dispatch(("SAPI.SpVoice"))
#     speak.speak(str)
# if __name__ == '__main__':
#     speak('hi')
#     print()


# *args use #


'''def function_1(*args):
    # print(type(args))
    if len(args)==3:
        print(f"The name of the student is {args[0]} and age is {args[1]} and roll no is {args[2]}.\n")
    else:
        print(f"The name of the student is {args[0]} and age is {args[1]}.\n")

lis=["Abhishek",15]'''
# function_1("Abhishek",14,3)
# function_1("Abhishek",14)
# function_1(*lis)



'''
# **kwargs use #

def print_marks(**kwargs):
    print(type(kwargs))
    for key,value in kwargs.items():
        print(key,"marks is ",value)


marklist= {"Abhishek": 100,"Rohon das":70,"Aman":91,"gaming with hunny":71}

print_marks(**marklist)'''


# over all use

"""def master(normal,*args,**kwargs):
    print(normal)
    for i in args:
        print(i)
    for key,value in kwargs.items():

        print(key,value)
marklist= {"Abhishek": 100,"Rohon das":70,"Aman":91,"gaming with hunny":71}
lis=["Abhishek",15]

master("normal args ",*lis,**marklist)
"""





def print_detals(*ankle):
    print("Maxmium value is",max(ankle),".")
    print("Minmum value is ",min(ankle),".")
print_detals(23,43,24,10,9,3)


# def area_of_circle(*redius):
#     print(2*22/7*redius[0])
#
# area_of_circle(7)


# def detels(*ask):
#     print(type(ask))
#     if len(ask)==3:
#         return f"The name is {ask[0]} salary is {ask[1]} and number is {ask[2]}.\n"
#     elif len(ask)==2:
#         return f"The name is {ask[0]} and salary is {ask[1]}.\n"
#     elif len(ask)==1:
#         return f"The name is {ask[0]}.\n"
#     else:
#         return f"Give argumant"
#
# print(detels('Abhishek'))
# print(detels("Abhishek",100000))
# print(detels("Abhishek",100000,9155039949))
#
# print(detels())