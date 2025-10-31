points_easy = 0
points_medium = 0
points_hard = 0

print("Hello Welcome to the illustrious Marvel quiz! Lets see if you know your stuff.\n")
level = input("Choose your level of difficulty: Easy, Medium, or Hard...\n")

if level == "Easy":
    print("\nWelcome to the easy quiz! Lets begin.")
    q1 = input("1. What is Tony Stark's superhero name?\n" + "A.Iron Man \nB.War Machine \nC.Iron Patriot \nD.Steel Man\n")
    if q1 == 'A':
        print("That is correct!")
        points_easy += 1
    elif q1 == 'B': 
        print("\nThat is incorrect. You get two more tries.")
        q1 = input("1. What is Tony Stark's superhero name?\n" + "A.Iron Man \nC.Iron Patriot \nD.Steel Man\n")
        if q1 == 'A':
            print("That is correct!")
            points_easy += 1
        elif q1 == 'C': 
            print("\nThat is incorrect. You get one more try.")
            q1 = input("1. What is Tony Stark's superhero name?\n" + "A.Iron Man \nD.Steel Man\n")
            if q1 == 'A':
                print("That is correct!")
                points_easy += 1
            else:
                print("That is incorrect. The correct Answer was A.")
        elif q1 == 'D': 
            print("\nThat is incorrect. You get one more try.")
            q1 = input("1. What is Tony Stark's superhero name?\n" + "A.Iron Man \nC.Iron Patriot\n")
            if q1 == 'A':
                print("That is correct!")
                points_easy += 1
            else:
                print("That is incorrect. The correct Answer was A.")
    elif q1 == 'C':
        print("\nThat is incorrect. You get two more tries.")
        q1 = input("1. What is Tony Stark's superhero name?\n" + "A.Iron Man \nB.War Machine \nD.Steel Man\n")
        if q1 == 'A':
            print("That is correct!")
            points_easy += 1
        elif q1 == 'B': 
            print("\nThat is incorrect. You get one more try.")
            q1 = input("1. What is Tony Stark's superhero name?\n" + "A.Iron Man \nD.Steel Man\n")
            if q1 == 'A':
                print("That is correct!")
                points_easy += 1
            else:
                print("That is incorrect. The correct Answer was A.")
        elif q1 == 'D': 
            print("\nThat is incorrect. You get one more try.")
            q1 = input("1. What is Tony Stark's superhero name?\n" + "A.Iron Man \nB.War Machine\n")
            if q1 == 'A':
                print("That is correct!")
                points_easy += 1
            else:
                print("That is incorrect. The correct Answer was A.")
    elif q1 == 'D':
        print("\nThat is incorrect. You get two more tries.")
        q1 = input("1. What is Tony Stark's superhero name?\n" + "A.Iron Man \nB.War Machine \nC.Iron Patriot\n")
        if q1 == 'A':
            print("That is correct!")
            points_easy += 1
        elif q1 == 'B': 
            print("\nThat is incorrect. You get one more try.")
            q1 = input("1. What is Tony Stark's superhero name?\n" + "A.Iron Man \nC.Iron Patriot\n")
            if q1 == 'A':
                print("That is correct!")
                points_easy += 1
            else:
                print("That is incorrect. The correct Answer was A.")
        elif q1 == 'C': 
            print("\nThat is incorrect. You get one more try.")
            q1 = input("1. What is Tony Stark's superhero name?\n" + "A.Iron Man \nB.War Machine\n")
            if q1 == 'A':
                print("That is correct!")
                points_easy += 1
            else:
                print("That is incorrect. The correct Answer was A.")

    q2 = input("2. What metal is Captain America’s shield made of? \nA.Adamantium \nB.Steel \nC.Vibranium \nD.Titanium\n")
    if q2 == 'C':
        print("That is correct!")
        points_easy += 1
    elif q2 == 'B': 
        print("\nThat is incorrect. You get two more tries.")
        q2 = input("2. What metal is Captain America’s shield made of? \nA.Adamantium \nC.Vibranium \nD.Titanium\n")
        if q2 == 'C':
            print("That is correct!")
            points_easy += 1
        elif q2 == 'D': 
            print("\nThat is incorrect. You get one more try.")
            q2 = input("2. What metal is Captain America’s shield made of? \nA.Adamantium \nC.Vibranium\n")
            if q2 == 'C':
                print("That is correct!")
                points_easy += 1
            else:
                print("That is incorrect. The correct Answer was C.")
        elif q2 == 'A': 
            print("\nThat is incorrect. You get one more try.")
            q2 = input("2. What metal is Captain America’s shield made of? \nC.Vibranium \nD.Titanium\n")
            if q2 == 'C':
                print("That is correct!")
                points_easy += 1
            else:
                print("That is incorrect. The correct Answer was C.")
    elif q2 == 'A':
        print("\nThat is incorrect. You get two more tries.")
        q2 = input("2. What metal is Captain America’s shield made of? \nB.Steel \nC.Vibranium \nD.Titanium\n")
        if q2 == 'C':
            print("That is correct!")
            points_easy += 1
        elif q2 == 'B': 
            print("\nThat is incorrect. You get one more try.")
            q2 = input("2. What metal is Captain America’s shield made of? \nC.Vibranium \nD.Titanium\n")
            if q2 == 'C':
                print("That is correct!")
                points_easy += 1
            else:
                print("That is incorrect. The correct answer was C.")
        elif q2 == 'D': 
            print("\nThat is incorrect. You get one more try.")
            q2 = input("2. What metal is Captain America’s shield made of? \nB.Steel \nC.Vibranium\n")
            if q2 == 'C':
                print("That is correct!")
                points_easy += 1
            else:
                print("That is incorrect. The correct answer was C.")
    elif q2 == 'D':
        print("\nThat is incorrect. You get two more tries.")
        q2 = input("2. What metal is Captain America’s shield made of? \nA.Adamantium \nB.Steel \nC.Vibranium\n")
        if q2 == 'C':
            print("That is correct!")
            points_easy += 1
        elif q2 == 'B': 
            print("\nThat is incorrect. You get one more try.")
            q2 = input("2. What metal is Captain America’s shield made of? \nA.Adamantium\nC.Vibranium\n")
            if q2 == 'C':
                print("That is correct!")
                points_easy += 1
            else:
                print("That is incorrect. The correct answer was C.")
        elif q2 == 'A': 
            print("\nThat is incorrect. You get one more try.")
            q2 = input("2. What metal is Captain America’s shield made of? \nB.Steel \nC.Vibranium\n")
            if q2 == 'C':
                print("That is correct!")
                points_easy += 1
            else:
                print("That is incorrect. The correct answer was C.")
    
    q3 = input("4. What is Spider-Man’s real name? \nA.Peter Parker \nB.Tony Stark \nC.Steve Rogers \nD.Scott Lang\n")
    if q3 == 'A':
        print("That is correct!")
        points_easy += 1
    elif q3 == 'B': 
        print("\nThat is incorrect. You get two more tries.")
        q3 = input("4. What is Spider-Man’s real name? \nA.Peter Parker \nC.Steve Rogers \nD.Scott Lang\n")
        if q3 == 'A':
            print("That is correct!")
            points_easy += 1
        elif q3 == 'D': 
            print("\nThat is incorrect. You get one more try.")
            q3 = input("4. What is Spider-Man’s real name? \nA.Peter Parker \nC.Steve Rogers\n")
            if q3 == 'A':
                print("That is correct!")
                points_easy += 1
            else:
                print("That is incorrect. The correct Answer was A.")
        elif q3 == 'C': 
            print("\nThat is incorrect. You get one more try.")
            q3 = input("4. What is Spider-Man’s real name? \nA.Peter Parker\nD.Scott Lang\n")
            if q3 == 'C':
                print("That is correct!")
                points_easy += 1
            else:
                print("That is incorrect. The correct Answer was A.")
    elif q3 == 'C':
        print("\nThat is incorrect. You get two more tries.")
        q3 = input("4. What is Spider-Man’s real name? \nA.Peter Parker\nB.Tony Stark\nD.Scott Lang\n")
        if q3 == 'A':
            print("That is correct!")
            points_easy += 1
        elif q3 == 'B': 
            print("\nThat is incorrect. You get one more try.")
            q3 = input("4. What is Spider-Man’s real name? \nA.Peter Parker\nD.Scott Lang\n")
            if q3 == 'C':
                print("That is correct!")
                points_easy += 1
            else:
                print("That is incorrect. The correct answer was A.")
        elif q3 == 'D': 
            print("\nThat is incorrect. You get one more try.")
            q3 = input("4. What is Spider-Man’s real name? \nA.Peter Parker\nC.Steve Rogers\n")
            if q3 == 'A':
                print("That is correct!")
                points_easy += 1
            else:
                print("That is incorrect. The correct answer was A.")
    elif q3 == 'D':
        print("\nThat is incorrect. You get two more tries.")
        q3 = input("4. What is Spider-Man’s real name? \nA.Peter Parker\nB.Tony Stark\nC.Steve Rogers\n")
        if q3 == 'A':
            print("That is correct!")
            points_easy += 1
        elif q3 == 'B': 
            print("\nThat is incorrect. You get one more try.")
            q3 = input("4. What is Spider-Man’s real name? \nA.Peter Parker \nC.Steve Rogers\n")
            if q3 == 'A':
                print("That is correct!")
                points_easy += 1
            else:
                print("That is incorrect. The correct answer was A.")
        elif q3 == 'C': 
            print("\nThat is incorrect. You get one more try.")
            q3 = input("4. What is Spider-Man’s real name? \nA.Peter Parker\nD.Scott Lang\n")
            if q3 == 'A':
                print("That is correct!")
                points_easy += 1
            else:
                print("That is incorrect. The correct answer was A.")
    
    
if level == "Medium":
    print("\nLooks like you consider your knowledge more morderate! Lets begin!")
    q1 = input("1. In Avengers: Endgame, what is Tony Stark’s daughter’s name? \nA.Lily\nB.Morgan\nC.Marcy\nD.Natalie\n")
    if q1 == 'B':
        print("That is correct!")
        points_medium += 1
    elif q1 == 'A': 
        print("\nThat is incorrect. You get one more try.")
        q1 = input("1. In Avengers: Endgame, what is Tony Stark’s daughter’s name? \nB.Morgan\nC.Marcy\nD.Natalie\n")
        if q1 == 'B':
            print("That is correct!")
            points_medium += 1
        else:
            print("That is incorrect. The correct Answer was B.")
    elif q1 == 'C':
        print("\nThat is incorrect. You get one more try.")
        q1 = input("1. In Avengers: Endgame, what is Tony Stark’s daughter’s name? \nA.Lily\nB.Morgan\nD.Natalie\n")
        if q1 == 'B':
            print("That is correct!")
            points_medium += 1
        else:
            print("That is incorrect. The correct Answer was B.")
    elif q1 == 'D':
        print("\nThat is incorrect. You get one more try.")
        q1 = input("1. In Avengers: Endgame, what is Tony Stark’s daughter’s name? \nA.Lily\nB.Morgan\nC.Marcy\n")
        if q1 == 'B':
            print("That is correct!")
            points_medium += 1
        else:
            print("That is incorrect. The correct Answer was B.")

    q2 = input("2. In Captain America: The Winter Soldier, who says the line “On your left”? \nA.Steve Rogers\nB.Natasha Romanoff\nC.Sam Wilson\nD.Bucky Barnes\n")
    if q2 == 'A':
        print("That is correct!")
        points_medium += 1
    elif q2 == 'B': 
        print("\nThat is incorrect. You get one more try.")
        q2 = input("2. In Captain America: The Winter Soldier, who says the line “On your left”? \nA.Steve Rogers\nC.Sam Wilson\nD.Bucky Barnes\n")
        if q2 == 'A':
            print("That is correct!")
            points_medium += 1
        else:
            print("That is incorrect. The correct Answer was A.")
    elif q2 == 'C':
        print("\nThat is incorrect. You get one more try.")
        q2 = input("2. In Captain America: The Winter Soldier, who says the line “On your left”? \nA.Steve Rogers\nB.Natasha Romanoff\nD.Bucky Barnes\n")
        if q2 == 'A':
            print("That is correct!")
            points_medium += 1
        else:
            print("That is incorrect. The correct answer was A.")
    elif q2 == 'D':
        print("\nThat is incorrect. You get one more try.")
        q2 = input("2. In Captain America: The Winter Soldier, who says the line “On your left”? \nA.Steve Rogers\nB.Natasha Romanoff\nC.Sam Wilson\n")
        if q2 == 'A':
            print("That is correct!")
            points_medium += 1
        else:
            print("That is incorrect. The correct answer was A.")
    
    q3 = input("3. What is the name of Thor’s axe introduced in Avengers: Infinity War? \nA.Godslayer\nB.Mjolnir II\nC.Stormbreaker\nD.Thunderstrike\n")
    if q3 == 'C':
        print("That is correct!")
        points_medium += 1
    elif q3 == 'B': 
        print("\nThat is incorrect. You get one more try.")
        q3 = input("3. What is the name of Thor’s axe introduced in Avengers: Infinity War? \nA.Godslayer\nC.Stormbreaker\nD.Thunderstrike\n")
        if q3 == 'C':
            print("That is correct!")
            points_medium += 1
        else:
            print("That is incorrect. The correct Answer was C.")
    elif q3 == 'A':
        print("\nThat is incorrect. You get one more try.")
        q3 = input("3. What is the name of Thor’s axe introduced in Avengers: Infinity War? \nB.Mjolnir II\nC.Stormbreaker\nD.Thunderstrike\n")
        if q3 == 'C':
            print("That is correct!")
            points_medium += 1
        else:
            print("That is incorrect. The correct answer was C.")
    elif q3 == 'D':
        print("\nThat is incorrect. You get one more try.")
        q3 = input("3. What is the name of Thor’s axe introduced in Avengers: Infinity War? \nA.Godslayer\nB.Mjolnir II\nC.Stormbreaker\n")
        if q3 == 'C':
            print("That is correct!")
            points_medium += 1
        else:
            print("That is incorrect. The correct answer was C.")


if level == "Hard":
    print("\nLooks like we're dealing with an expert! Lets begin!")
    print("This level will provide no help if you get a question wrong. So be careful!\n")
    q1 = input("1. What is the name of the alien race Ronan belongs to in Guardians of the Galaxy? \nA.Kree\nB.Skrulls\nC.Xandarians\nD.Asgardians\n")
    if q1 == 'A':
        print("That is correct!")
        points_hard += 1
    else:
        print("That is incorrect. The correct Answer was A.")

    q2 = input("2. What is the exact year Captain America: The First Avenger begins? \nA.1939 \nB.1941 \nC.1943 \nD.1945\n")
    if q2 == 'B':
        print("That is correct!")
        points_hard += 1
    else:
        print("That is incorrect. The correct Answer was B.")

    q3 = input("3. In Doctor Strange in the Multiverse of Madness, what universe is known as the main MCU universe? \nA.Earth-838\nB.Earth-199999\nC.Earth-616\nD.Earth-42\n")
    if q3 == 'C':
        print("That is correct!")
        points_hard += 1
    else:
        print("That is incorrect. The correct Answer was C.")

if points_easy == 3:
    print("\nCongratulations!!! You passed with flying colors")
elif points_easy == 2:
    print("\nGreat job! You got 2/3 Correct!")
elif points_easy > 2:
    print("\nNice Try! Better luck Next time!")

if points_medium == 3:
    print("\nCongratulations!!! You got 3/3 correct. It seems you know your stuff")
elif points_medium == 2:
    print("\nGreat job! You got 2/3 Correct!")
elif points_medium > 2:
    print("\nNice Try! Better luck Next time!")

if points_hard == 3:
    print("\nCongratulations!!! 3/3 correct! You really do have expert knowledge!")
elif points_hard == 2:
    print("\nGreat job! You got 2/3 Correct!")
elif points_hard > 2:
    print("\nNice Try! Better luck Next time!")


