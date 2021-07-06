import random
for i in range(6):
    my_input = int(input("enter a number : "))
    computer_random_number = random.randint(0, 5)

    if my_input <= 5:
        if my_input == computer_random_number:
            print("you win")
        else:
            print("you lost, Computer chose: "+ str(computer_random_number))
    else:
        print("invalid input")
