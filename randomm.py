import random 

print("********* Number gueesing game ***********")
list= [ i for i in range(1,10)]

# list=[i for i in range(1,101)]
# # shuffle given list randomly
# random.shuffle(list)
# print("list is", list)

random_choice = random.choice(list)
# print(random_choice)
guessed_num= -1
while guessed_num != random_choice:
    guessed_num = int(input("Enter your guess #:"))

    if guessed_num > random_choice:
        print("Too High!")
    if guessed_num < random_choice:
        print("Too Low!")

print("you guessed right! The number is ", random_choice)