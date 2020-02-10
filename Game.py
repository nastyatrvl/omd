#!/usr/bin/env python
# coding: utf-8

# In[1]:


def main():
    print("*** Avito Adventure***\n")
    name = input("Hi! What's your name?").title()
    print ("\nOK, " +  name +", it's your very first day in Avito. Let's get started! \U0001f389")
    step_1()

# Step 1

def step_1():
    print(
        "You have an important meeting right away."
        "\nThe room is called Shikotan."
        "\nWhere the hell is it?")
    option = ''
    options = {'10th': True, '13th': False, '14th': False,'15th': False}
    while option not in options:
        print("Choose: {}/{}/{}/{}".format(*options))
        option = input()
              
    if options[option]:
        print("Well done! You've arrived just in time and it went well\n")
        return step_2()
    else:
        print("You've missed the very first meeting... I'm afraid you are fired\n")

# Step 2

def step_2():
    print("Now it's a lunch time! Would you wait an elevator or take stairs?")

    option = ''
    options = {'Stairs': True, 'Elevator': False}
    while option not in options:
        print("Choose: {}/{}".format(*options))
        option = input()
              
    if options[option]:
        print("Good choice!"
              "\nYou skipped the queue and look awesome\n")
        return step_3()
    else:
        print("You died from hunger \U0001f641\n")

# Step 3

def step_3():
    print("You met Pravdiviy, what would you do?"
          "\nGreet him or run?")

    option = ''
    options = {'Say hi': True, 'Run away': False}
    while option not in options:
        print("Choose: {}/{}".format(*options))
        option = input()
              
    if options[option]:
        print("You've had a great conversation and even got some promising thoughts about your promotion U1F60E\n")
        return step_4()
    else:
        print("Not the best idea of yours. You are fired! \U0001f97A\n")

# Step 4

def step_4():

    print("Now it's time to make your hands dirty."
          "\nYou open DBeaver, write the 900 lines code but..."
          "\nWhich port to choose for query execution?")

    option = ''
    options = {'5433': True, '5435': False}
    while option not in options:
        print("Choose: {}/{}".format(*options))
        option = input()
              
    if options[option]:
        print("DWH is coming for you. The game is over.\n")
    else:
        print("You do well!\n")
        return step_5()

# Step 5
              
def step_5():

    print("There is a new course from Avito Academy!"
          "\nIt's all about Python coding"
          "\nWanna enroll?")

    option = ''
    options = {'Yes': True, 'No': False}
    while option not in options:
        print("Choose: {}/{}".format(*options))
        option = input()
              
    if options[option]:
        print("Good choice! Seems you and Avito is a perfect match \U0001f913"
              "\nPlenty of good things are awaiting for you! \U0001f389\n")
    else:
        print("I don't want to continue this game with you... Bye \U0001f97A\n")

if __name__ == '__main__':
    main()


# In[ ]:




