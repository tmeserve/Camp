'''
Created on Nov 17, 2017

@author:  Will Strueh and Tyler Meserve
'''
from BinSearchTree import BinarySearchTree as BST
from Queues import Queue as Q

def help(Bin_T, queue, nothing2, nothing3, nothing4, nothing5, nothing6, nothing7, nothing8):
    print("The commands are:\nh (help)\nr filename (read in a file)\nw filename (write a file to enroll the campers)\nq (quit)\n"
    + "e name age gender (enrolls a camper)\nd name (withdraw the specified camper)\na (prints the average age of all the campers)\n" 
    + "l name (prints the attributes of the specified camper)\n"
    + "g (prints the number of male and female campers)\np order (print all the currently enrolled campers with the specified order (pre, in, post))\n"
    + "a time number name (the named party with the specifed number of people has arrived in the mess hall at the specifed time, to wait for their table\n"
    + "t time (a table is open for the party which is first in the queue at the specified time)\n"
    + "c (the mess hall is no longer serving food after this command is read)")

def reads(Bin_T, queue, file, nothing, nothing2, nothing3, nothing4, nothing5, nothing6):
    with open(file, 'r') as fil:
        for lines in fil:
            deal_with_commands(Bin_T, queue, lines)

def write(Bin_T, queue, file, nothing, nothing2, nothing3, names, nothing5, nothing6):
    
    i = 0
    
    fil = open(file, 'w')
    
    name_age_gender = []
    
    for names in Bin_T.preorder():
        name_age_gender.append(names)
    
    
    while i < len(name_age_gender):
        name_age_genders = name_age_gender[i]
        name = name_age_genders[0]
        age_gender = name_age_genders[1].split()
        age = age_gender[0]
        gender = age_gender[1]
        fil.write(name + " " + age + " " + gender + "\n")
        i += 1

def enroll(Bin_T, queue, name, two_words, nothing, nothing2, nothing3, nothing4, nothing5):
    Bin_T.insert(name, (name, two_words))

def drop(Bin_T, queue, name, nothing, nothing2, nothing3, nothing4, nothing5, nothing6):
    
    campers_stats = Bin_T.lookup(name)
    
    campers_name = campers_stats[0]
    
    campers_age_gender = campers_stats[1].split()
    
    age = campers_age_gender[0]
    
    gender = campers_age_gender[1]
    
    print("{0} has been dropped".format(campers_name))
    Bin_T.remove(name)

def average(Bin_T, queue, nothing, nothing2, nothing3, age, nothing4, nothing5,nothing6):
    total = sum(age)
    average = total/len(age)
    print("The average age of campers is {0}".format(average))

def lookup(Bin_T, queue, name, nothing, nothing2, nothing3, nothing4, nothing5, nothing6):
    
    campers_stats = Bin_T.lookup(name)
    
    campers_name = campers_stats[0]
    
    campers_age_gender = campers_stats[1].split()
    
    campers_age = campers_age_gender[0]
    
    campers_gender = campers_age_gender[1]
    
    if campers_gender.lower() == "m":
        campers_gender = "male"
    elif campers_gender.lower() == "f":
        campers_gender = "female"
    
    print("{0} is {1} and is {2}".format(campers_name, campers_age, campers_gender))

def gender_count(Bin_T, queue, nothing, nothing2, nothing3, nothing4, names, male, female):
    print("There are {0} males and {1} females".format(male, female))

def order(Bin_T, queue, order, nothing, nothing2, nothing3, names, nothing4, nothing5):
    if order == "pre":
        for names in Bin_T.preorder():
            print(names)
    elif order == "in":
        for names in Bin_T.inorder():
            print(names)
    elif order == "post":
        for names in Bin_T.postorder():
            print(names)

def arrival(Bin_T, queue, time_number_name, nothing, nothing2, nothing3, nothing4, nothing5, nothing6):
    time_number_name_split = time_number_name.split()
    
    time = time_number_name_split[0]
    number_of_people = time_number_name_split[1]
    name = time_number_name_split[2].title()
    
    queue.enqueue(time_number_name)
    
    print("Party {0} has now been queued to arrive at {1} with {2} people".format(name, time, number_of_people))

def table(Bin_T, queue, time, nothing, nothing2, nothing3, nothing4, nothing5, nothing6):
    party_to_be_seated = queue.dequeue()
    
    time_number_name = party_to_be_seated.split()
    
    time = time_number_name[0]
    number_of_people = time_number_name[1]
    name = time_number_name[2].title()
    
    print("Party {0} has been seated {1} after opening with {2} people.".format(name, time, number_of_people))

def close(Bin_T, queue, nothing, nothing2, nothing3, nothing4, nothing5, nothing6, nothing7):
    print("The lunch line is being emptied and is no longer seating people.")
    while queue is not None:
        queue.dequeue()
    print("The lunch line has now been emptied and is now closed.")

def deal_with_commands(Bin_T, queue, commands):
    
    male_campers = 0
    female_campers = 0
    names = []
    
    comm, com, co, c = "", "", "", ""
    nothing = ""
    ages = []
    
    comms = {"h" : help, "r" : reads, "w" : write, "e" : enroll, "d" : drop, "l" : lookup, "g" : gender_count, "p" : order, "a" : arrival, "t" : table}
    
    if commands.lower() == "a":
        average(Bin_T, queue, com, co, c, ages, names, male_campers, female_campers)
    elif commands.count("\"") == 2:
        
        comm = commands[0]
        parts = commands.split('"')
        
        if comm.lower() == "e":
            parts[0] = parts[1]
            parts[1] = parts[2].strip()
            com = parts[0]
            partss = parts[1].split()
            co = partss[0]
            c = partss[1]
            double_word = parts[1]
            parts.pop()
        elif comm.lower() == "l":
            parts[0] = parts[1]
            com = parts[0]
            parts.pop()
            parts.pop()
        
        if commands.startswith("e"):
            ages.append(int(co))
            names.append(com)
            comm.lower()
            comms[comm](Bin_T, queue, com, double_word, nothing , ages, names, male_campers, female_campers)
            if commands.lower().endswith("m") or commands.lower().endswith("male"):
                male_campers += 1
            elif commands.lower().endswith("f") or commands.lower().endswith("female"):
                female_campers += 1
        
        else:
            comm.lower()
            comms[comm](Bin_T, queue, com, co, c, ages, names, male_campers, female_campers)
    else:
        parts = commands.split()
        str1 = ' '.join(parts)
        words = [] # create an empty list of your words
        chars = [] # create an empty list of characters
        for char in str1:
            if char == " " and chars: # if the character is a space and we've stored some chars
                words.append("".join(chars)) # combine the stored chars into a word and add it to the word lise
                chars = [] # clear out the stored chars
            elif char != " ":
                chars.append(char) # otherwise, store the char if it's not a space
        if chars:
            words.append("".join(chars))
        
        if str1.count(' ') == 0:
            comm = words[0]
        elif str1.count(' ') == 1:
            comm, com = words[0], words[1]
        elif str1.count(' ') == 3:
            comm, com, co, c = words[0], words[1], words[2], words[3]
        
        if commands.startswith("a") and commands.count(" ") == 3:
            com = com + " " + co + " " + c
        
        if commands.startswith("e"):
            double_word = co + " " + c
            ages.append(int(co))
            names.append(com)
            comm.lower()
            comms[comm](Bin_T, queue, com, double_word, nothing , ages, names, male_campers, female_campers)
            if commands.lower().endswith("m") or commands.lower().endswith("male"):
                male_campers += 1
            elif commands.lower().endswith("f") or commands.lower().endswith("female"):
                female_campers += 1
        else:
            comm.lower()
            comms[comm](Bin_T, queue, com, co, c, ages, names, male_campers, female_campers)

def main():
    
    qu = Q()
    Bin = BST()
    
    anocom = False
    while anocom == False:
        commands = input("Please enter a command.\n")
        
        if commands.lower() == "q":
            print("Bye, have a good time.")
            anocom = True
            continue
        elif commands.startswith(" ") or not commands:
            print("Please input a command. To get help type in h.")
        else:
            deal_with_commands(Bin, qu, commands)

if __name__ == '__main__':
    main()