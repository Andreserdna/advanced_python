
# -*- coding: utf-8 -*-

#3- Write a program that repeatedly prompts 
#the user to enter a capital for a state. Upon receiving the user input, 
#the program reports whether the answer is correct. The program prompts the user 
#to answer all the states capital and displays the total correct count. 
#The answer should not be case sensitive. Implement using a dictionary.


import sys
from random import shuffle

capital_dict = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona':'Phoenix',
    'Arkansas':'Little Rock',
    'California': 'Sacramento',
    'Colorado':'Denver',
    'Connecticut':'Hartford',
    'Delaware':'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'St. Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'  
}


leave = 'quit'

while True:
    right_answers = 0
    wrong_answers = 0
    quit = 'quit'
    print("Type \'quit\' anytime to exit the game!")
    for k,v in capital_dict.items():
        printstring = ("What is the capitol for %s : ") % (k)
        answer = input(printstring)
        if answer.lower() == v.lower():
            print("Correct!")
            right_answers += 1
        elif answer.lower() == quit.lower():
            print("quitting game! \nscore can be found below")
            print("Total right answers",right_answers)
            print("Total wrong answers", wrong_answers)
            sys.exit()
        elif answer.lower() != v.lower():
            print("Wrong!")
            print("your answer was:",answer)
            print("correct answer was : ", v)
            wrong_answers += 1
