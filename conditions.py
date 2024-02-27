# #Equal operator 
# a=1
# b=3
# if a==b:
#     print("a and b are same")
# if a is b:
#     print("a and b are same")

# #Not equal operator 
# if a != b:
#     print("a and b are  not same")
# if a is not b:
#     print("a and b are not same")

# # greater than , less than ,greaterthan or equal to lessthan or equals to
# if a > b:
#     print("a > b")
# if a < b:
#     print("a > b")
# if a >= b:
#     print("a > b")
# if a <= b:
#     print("a > b")

# #logical operator
# b = None 
# if a or b :
#     print("one of them exists")
# if a and b :
#     print("both of them exists")

if __name__ == "__main__":
    """
    Write a program that takes marks as floating number and prints which division it falls :
    80 and above : Distinction 
    60-79 : First division 
    50-59 : Second Division 
    40-49 : Third Division 
    39 and below : Fail 
    """  
    marks=float(input("Enter the marks:"))
    if marks >= 80:
        print("The division is Distinction")
    elif marks >=60 and marks <=79 :
        print("The division is First")
    elif marks >=50 and marks <=59 :
        print("The division is Second")
    elif marks >=40 and marks <=49 :
        print("The division is Third")
    else:
        print("Fail")




