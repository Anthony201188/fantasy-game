# welcome to my fantaasy character creator - please check the README.md file in this repo for the brief

# First I will import any depednacies
import random

#print opening statement
print()
print()
print()
print("---WELCOME TO THE FANTASY LAND CHARACTER CREATOR!!---")
print("...")
print("...")
print("...")
print()


# next I will create variables for the required 5 character names at the same time as creating user input prompts for them
charachter_name_1 = input("Please input the name of your first character then press enter: ")
charachter_name_2 = input("Please input the name of your second character then press enter: ")
charachter_name_3 = input("Please input the name of your third character then press enter: ")
charachter_name_4 = input("Please input the name of your fourth character then press enter: ")
charachter_name_5 = input("Please input the name of your fith character then press enter: ")

#print character names
print("*********")
print()
print("Your character names are: ")
print("Character 1: ", charachter_name_1)
print("Character 2: ", charachter_name_2)
print("Character 3: ", charachter_name_3)
print("Character 4: ", charachter_name_4)
print("Character 5: ", charachter_name_5)
print()
print("***********")
print("---GENERATING CHARACTERS---")
print("***********")
print()

#put the different types of character in a variable as a list
character_type = ["Wiazrd", "Warrior", "Potato"]

"""As a side note trying to make things neat and creating variables for the ranom elements resulted in one single 
randomised global element which meant things were only randomised once and then printed out the same at all the other points in the programm so I had to remove the two line of code underneath """
##random_choice = random.choice(character_type)
##random_stat = random.randint(5,10)

print("***YOUR CHARACTERS ARE COMPLETE***")
# charachter 1 assign character type
charachter_name_1 += " is a "
charachter_name_1 += random.choice(character_type)
charachter_name_1 += "!"
print(charachter_name_1)
print()

#assign random intigers to stats
Health = random.randint(5,10)
Strength = random.randint(5,10)
Magic = random.randint(5,10)


#multiply stats depending on character type
if "Warrior" in charachter_name_1:
    Strength *= 3
if "Wizard" in charachter_name_1:
    Magic *= 3
if "Potato" in charachter_name_1:
    Health *= 3

#print stats
print("STATS...")
print("    Health:", Health)
print("    Strength:", Strength)
print("    Magic:", Magic)
print()
print()


#repeat for the rest of the characters

#character 2 assing type
charachter_name_2 += " is a "
charachter_name_2 += random.choice(character_type)
charachter_name_2 += "!"
print(charachter_name_2)
print()


#assign random intigers to stats
Health = random.randint(5,10)
Strength = random.randint(5,10)
Magic = random.randint(5,10)


#multiply stats depending on character type
if "Warrior" in charachter_name_2:
    Strength *= 3
if "Wizard" in charachter_name_2:
    Magic *= 3
if "Potato" in charachter_name_2:
    Health *= 3

#print stats
print("STATS...")
print("    Health:", Health)
print("    Strength:", Strength)
print("    Magic:", Magic)
print()
print()



#charachter 3 assing character type
charachter_name_3 += " is a "
charachter_name_3 += random.choice(character_type)
charachter_name_3 += "!"
print(charachter_name_3)
print()


#assign random intigers to stats
Health = random.randint(5,10)
Strength = random.randint(5,10)
Magic = random.randint(5,10)


#multiple depending on character type
if "Warrior" in charachter_name_3:
    Strength *= 3
if "Wizard" in charachter_name_3:
    Magic *= 3
if "Potato" in charachter_name_3:
    Health *= 3

#print stats
print("STATS...")
print("    Health:", Health)
print("    Strength:", Strength)
print("    Magic:", Magic)
print()
print()


#charachter 4 assing character type
charachter_name_4 += " is a "
charachter_name_4 += random.choice(character_type)
charachter_name_4 += "!"
print(charachter_name_4)
print()


#assign random intigers to stats
Health = random.randint(5,10)
Strength = random.randint(5,10)
Magic = random.randint(5,10)


#multiple stats depending on character type
if "Warrior" in charachter_name_4:
    Strength *= 3
if "Wizard" in charachter_name_4:
    Magic *= 3
if "Potato" in charachter_name_4:
    Health *= 3

#print stats
print("STATS...")
print("    Health:", Health)
print("    Strength:", Strength)
print("    Magic:", Magic)
print()
print()

#charachter 5 assing charachter type
charachter_name_5 += " is a "
charachter_name_5 += random.choice(character_type)
charachter_name_5 += "!"
print(charachter_name_5)
print()


#assign random intigers to stats
Health = random.randint(5,10)
Strength = random.randint(5,10)
Magic = random.randint(5,10)


#multiply stats depending on character type
if "Warrior" in charachter_name_5:
    Strength *= 3
if "Wizard" in charachter_name_5:
    Magic *= 3
if "Potato" in charachter_name_5:
    Health *= 3

#print stats
print("STATS...")
print("    Health:", Health)
print("    Strength:", Strength)
print("    Magic:", Magic)
print()
print()

print()
print("***********")



