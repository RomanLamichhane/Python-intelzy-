'''
Write a program to accept the costprice of a bike and display the road tax to be paid according to the following criteria :
costprice(in Rs)      Tax
>100000               15%
>50000 and <=100000   10%
<=50000               5%
'''
user_costprice=int(input("Enter the costprice:"))
if user_costprice > 100000:
    print("The tax is 15%")
elif user_costprice  > 50000 and user_costprice  <=100000:
    print("The tax is 10%")
elif user_costprice <= 50000:
    print("The tax is 5%") 
else:
    print("not valid")
    