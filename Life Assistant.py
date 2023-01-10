import time
import datetime
import os
import playsound
import webbrowser
import pyjokes
import math
import csv
import random
import requests

class journal:
    def add_journal():
        while True:
            f = open("journal.txt","a")
            text1 = input(">>")
            print()
            f.write(text1+'\n') #appending entries into text file
            f.close()
            print('=========================')
            print("Entry Added Successfully!")
            print("=========================")
            print()
            add = input("Would you like to add more entries?(yes/no): ")
            if add == 'no':
                print()
                break
            print()

    def read_journal(): 
        try:
            with open("journal.txt", 'r') as f:
                count = 0
                entries = f.readlines()
                if entries == []: #if file is empty
                    print("No Entries Found!!")
                    print()
                    ch1 = input("Would you like to add entries? (yes/no): ")
                    if ch1.lower() == 'yes':
                        print()
                        journal.add_journal()
                    elif ch1.lower() == 'no':
                        pass
                    else:
                        print("Enter Valid Input")
                        print()
                        ch1 = input("Would you like to add entries? (yes/no): ")
                else:
                    for i in entries:
                        count += 1
                        print(str(count)+'.', i.strip('\n')) #displaying all entries added
                    print()
        except: #if file does not exist
            print("You Haven't Written any Entries yet!")
            print()
            ch2 = input("Would you like to start journaling? (yes/no): ")
            print()
            if ch2.lower() == 'yes':
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("Welcome To Virtual Journaling!! Proceed with writing your first entry!! Happy Journaling!")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print()
                journal.add_journal()
            elif ch2.lower() == 'no':
                print()
                print("No Worries! Start your daily journaling soon!")
                print()
            else:
                print("Enter Valid Input")
                print()
                ch2 = input("Would you like to add entries? (yes/no): ")
    
    def delete_journal():
        while True:
            print('+----------------------------------------------+')
            print('|                   Delete                     |')
            print('+----------------------------------------------+')
            print('| 1. Delete one entry                          |')
            print('| 2. Delete all entries                        |')
            print('+----------------------------------------------+') 
            print('| 3. Journal Menu                              |')
            print('+----------------------------------------------+') 
            print() 
            choice = int(input("Enter Choice(1/2/3): "))
            print()
            if choice == 1:
                try:
                    with open("journal.txt", 'r') as f:
                        entries = f.readlines()
                        count = 0
                        if entries == []:
                            print("No Entries Available for Deletion")
                        else:
                            print("The Entries till date are:-")
                            for i in entries:
                                count += 1
                                print(str(count)+'.', i.strip('\n')) #displaying entries 
                            print()
                            position = int(input("Enter the position of the entry to be deleted: "))
                            print()
                            del entries[position-1] #deleting specified entry
                            print('==========================')
                            print("Entry Deleted Successfully")
                            print('==========================')
                            print()
                        f = open("journal.txt", "w")
                        f.writelines(entries) #rewriting all entries except deleted entry
                        f.close()
                except:
                    print("No Entries Available for Deletion")
            elif choice == 2:
                try:
                    os.remove("journal.txt")
                    print('=================================')
                    print("All Entries Deleted Successfully" )
                    print('=================================')
                    print()
                except:
                    print("No Entries Available for Deletion")
                    print()
            elif choice == 3:
                break

    def journal_main():
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print("            WELCOME TO VIRTUAL JOURNALING!             ")
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print()
        while True:
            print('+-----------------------------------------------------+')
            print('|                Journal Categories                   |')
            print('+-----------------------------------------------------+')
            print('| 1. Add Journal Entry                                |')
            print('| 2. Read Journal Entry                               |')
            print('| 3. Delete Journal Entry                             |')
            print('| 4. Main Menu                                        |')
            print('| 5. Exit                                             |')
            print('+-----------------------------------------------------+') 
            print()   
            choice = input("Enter Choice (1/2/3/4/5): ")
            print() #calling all related functions
            if choice == '1':
                journal.add_journal()
            elif choice == '2':
                journal.read_journal()
            elif choice == '3':
                journal.delete_journal()
            elif choice == '4':
                break 
            elif choice == '5':
                quit() #exiting from file 
            else:
                print("Enter Valid Choice")
                
class clock:
    def timer():
        tt = int(input("Enter time in seconds: "))
        while tt:
            mins, secs = divmod(tt, 60)
            hours = 0 
            if mins > 60:
                hours, mins = divmod(mins, 60)
            timer_display = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
            print(timer_display, end="\r")
            time.sleep(1)
            tt -= 1
        print()
        print('========================')
        print("      Time's Up!!!      ")
        print('========================')
        print()
        playsound.playsound("alarm.wav")

    def alarm():
        settime = input("Enter time in HH:MM:SS format: ")
        sethour = settime[0:2]
        setminute = settime[3:5]
        setsecond = settime[6:8]
        while True:
            now = datetime.datetime.now()
            currenthour = now.strftime("%H")
            currentminute = now.strftime("%M")
            currentsecond = now.strftime("%S")
            if sethour == currenthour:
                if setminute == currentminute:
                    if setsecond == currentsecond:
                        print()
                        print('========================')
                        print("      Time's Up!!!      ")
                        print('========================')
                        print()
                        playsound.playsound("alarm.wav")
                        break

    def stopwatch():
        print("---Press Enter to Start---")
        input("Start: ")
        starttime = time.time()
        print("---Press Enter to Stop---")
        input("Stop: ")
        stoptime = time.time() 
        def convert(seconds):
            minutes = seconds // 60 
            seconds = seconds % 60
            hours = minutes // 60
            minutes = minutes % 60
            print("Time Passed = '{:02d}:{:02d}:{:02d}'".format(int(hours), int(minutes), int(seconds)))
            print()
        elapsed = round(stoptime - starttime, 2)
        convert(elapsed)

    def clock_main():
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print("                    WELCOME TO CLOCK!                    ")
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print()
        while True:
            print('+-------------------------------------------------------+')
            print('|                  Clock Categories                     |')
            print('+-------------------------------------------------------+')
            print('| 1. Timer                                              |')
            print('| 2. Alarm                                              |')
            print('| 3. Stopwatch                                          |')
            print('| 4. Main Menu                                          |')
            print('| 5. Exit                                               |')
            print('+-------------------------------------------------------+') 
            print()   
            choice = input("Enter Choice (1/2/3/4/5): ")
            print()
            if choice == '1':
                clock.timer()
            elif choice == '2':
                clock.alarm()
            elif choice == '3':
                clock.stopwatch()
            elif choice == '4':
                break
            elif choice == '5':
                quit()
            else:
                print("Enter correct choice")

class calendar:
    def calendar_display():
        month = int(input("Enter desired month(1-12): "))
        print()
        year = int(input("Enter desired year: "))
        months = {1:'January', 2:'February', 3:'March', 4:'April',
                5:'May', 6:'June', 7:'July',8:'August', 9:'September', 
                10:'October', 11:'November', 12:'December'}
        #odd days
        day = (year-1)%400
        day = (day//100)*5 + ((day % 100) - (day % 100)//4) + ((day % 100)//4)*2
        day = day % 7 
        nonleap = [31,28,31,30,31,30,31,31,30,31,30,31] #number days in case of non leap year
        leap = [31,29,31,30,31,30,31,31,30,31,30,31] #number of days in case of leap year
        s = 0 
        if year % 4 == 0:
            for i in range(month-1):
                s += leap[i]
        else:
            for i in range(month-1):
                s += nonleap[i]
        day += s % 7 
        day = day % 7 
        #space for places of no date
        space = ''
        space = space.rjust(2, ' ')
        print()
        print('  ', months[month], year)
        print('Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa')
        #months with 30 days
        if month == 4 or month == 6 or month == 9 or month == 11:
            for i in range(31 + day):
                if i <= day:
                    print(space, end = ' ')
                else:
                    print("{:02d}".format(i-day), end = ' ')
                    if (i+1)%7 == 0:
                        print()
            print()
            print()
        #month of 28/29 days - February
        elif month == 2:
            if year % 4 == 0:
                num = 30 
            else:
                num = 29
            for i in range(num + day):
                if i <= day:
                    print(space, end = ' ')
                else:
                    print("{:02d}".format(i-day), end = ' ')
                    if (i+1)%7 == 0:
                        print()
            print()
            print()
        #months with 31 days
        else: 
            for i in range(32 + day):
                if i <= day:
                    print(space, end = ' ')
                else:
                    print("{:02d}".format(i-day), end = ' ')
                    if (i+1)%7 == 0:
                        print()
            print()
            print()
        
    def important_dates():
        while True:
            print()
            print('+----------------------------------------+')
            print('|           Important Dates              |')
            print('+----------------------------------------+')
            print('| 1. Add Important Date                  |')
            print('| 2. Read Important Date                 |')
            print('+----------------------------------------+')
            print('| 3. Calendar Categories                 |')
            print('+----------------------------------------+') 
            print()
            choice = input("Enter Choice(1/2/3): ")
            print()
            if choice == '1':
                while True:
                    print("Enter important date with name of occassion")
                    f = open("dates.txt", "a")
                    impdate = input(">>")
                    f.write(impdate + '\n')
                    f.close()
                    print()
                    more = input("Would you like to add more dates(yes/no): ")
                    print()
                    if more == 'no':
                        break
            elif choice == '2':
                try:
                    with open("dates.txt", "r") as f:
                        dates = f.readlines()
                        if dates == []:
                            print("No Important Dates Added!")
                            print()
                        else:
                            print("Important Dates-")
                            for i in dates:
                                print(i.strip('\n'))
                except:
                    print("No Dates Added")
            elif choice == '3':
                break
            else:
                print("Enter Valid Choice!")
          
    def calendar_main():
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print("                 WELCOME TO CALENDAR!                  ")
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print()
        while True:
            print('+-----------------------------------------------------+')
            print('|                Calendar Categories                  |')
            print('+-----------------------------------------------------+')
            print('| 1. Display Calendar                                 |')
            print('| 2. Important Dates                                  |')
            print('| 3. Main Menu                                        |')
            print('| 4. Exit                                             |')
            print('+-----------------------------------------------------+') 
            print()   
            choice = input("Enter desired choice(1/2/3/4): ")
            print()
            if choice == '1':
                calendar.calendar_display()
            elif choice == '2':
                calendar.important_dates()
            elif choice == '3':
                break
            elif choice == '4':
                quit()
            else:
                print("Enter valid choice!")
                
class todolist:
    def add_task():
        add = 'yes'
        while add.lower() == 'yes':
            if add.lower() == 'no':
                break
            f = open("tasks.txt", "a")
            task = input("Enter task: ") #appending tasks to file
            f.write(task+'\n')
            f.close()
            print()
            add = input("Would you like to add more tasks?(yes/no): ")
            print()

    def display_tasks():
        count = 0 
        try:
            with open("tasks.txt", "r") as f:
                tasks = f.readlines()
                if tasks == [] : #if file is empty
                    print("No Tasks Found!!")
                    print()
                    ch1 = input("Would you like to add tasks? (yes/no): ")
                    if ch1.lower() == 'yes':
                        todolist.add_task()
                    elif ch1.lower() == 'no':
                        pass
                    else:
                        print("Enter Valid Input")
                        ch1 = input("Would you like to add tasks? (yes/no): ")
                        print()
                print("The following are your tasks:-")
                for i in tasks:
                    count += 1
                    print(str(count)+'.', i.strip('\n')) #displaying tasks
                print()
        except:
            print("You haven't written any tasks yet!")
            print()
            ch2 = input("Would you like to add tasks? (yes/no): ")
            print()
            if ch2.lower() == 'yes':
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print("Welcome to To-Do List!! Proceed with writing your first task!!")
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print()
                todolist.add_task()
            elif ch2.lower() == 'no':
                print()
            else:
                print("Enter Valid Input")
                ch2 = input("Would you like to add tasks? (yes/no): ")

    def delete_task():
        while True:
            print()
            print('+----------------------------------------------+')
            print('|                   Delete                     |')
            print('+----------------------------------------------+')
            print('| 1. Delete one task                           |')
            print('| 2. Delete all tasks                          |')
            print('+----------------------------------------------+') 
            print('| 3. To-Do List Menu                           |')
            print('+----------------------------------------------+')
            print() 
            choice = int(input("Enter Choice(1/2/3): "))
            print()
            if choice == 1:
                try:
                    with open("tasks.txt", "r") as f:
                        count = 0
                        tasks = f.readlines()
                        if tasks == []:
                            print("No Tasks Available for Deletion")
                        print("The following are your tasks:-")
                        for i in tasks:
                            count += 1
                            print(str(count)+'.', i.strip('\n'))
                        print()
                        position = int(input("Enter the position of the task to be deleted: "))
                        print()
                        del tasks[position-1]
                        print('==========================')
                        print("Task Deleted Successfully")
                        print('==========================')
                    f = open("tasks.txt", "w")
                    f.writelines(tasks) #rewriting all tasks except the one deleted
                    f.close()
                except:
                    print("No Tasks Available for Deletion!")
            elif choice == 2:
                os.remove("tasks.txt") 
                print('==============================')
                print("All Tasks Deleted Successfully")
                print('==============================')
            elif choice == 3:
                break

    def completed_task():
        more = 'yes'
        while more.lower() == 'yes':
            if more.lower() == 'no':
                break
            todolist.display_tasks()
            list1 = []
            position = int(input("Enter position of completed task: "))
            f = open("tasks.txt", "r")
            tasks = f.readlines()
            f.close()
            for i in range(len(tasks)):
                if i == position-1:
                    tasks[i] = tasks[i].strip('\n') + " ✔" + '\n' #appending a ✔ in front of completed tasks
                    list1.append(tasks[i])
                else:
                    list1.append(tasks[i])
            f = open("tasks.txt", "w")
            f.writelines(list1)
            f.close()
            todolist.display_tasks()
            more = input("Would you like to mark more tasks complete(yes/no): ")

    def todolist_main():
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print("                WELCOME TO TO-DO LIST!                  ")
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print()
        while True:
            print('+-------------------------------------------------------+')
            print('|                To Do List Categories                  |')
            print('+-------------------------------------------------------+')
            print('| 1. Add Tasks                                          |')
            print('| 2. Read Tasks                                         |')
            print('| 3. Delete Task                                        |')
            print('| 4. Mark Task Complete                                 |')
            print('| 5. Main Menu                                          |')
            print('| 6. Exit                                               |')
            print('+-------------------------------------------------------+') 
            print()   
            choice = int(input("Enter your desired choice(1/2/3/4/5/6): "))
            print()
            if choice == 1:
                todolist.add_task()
            elif choice == 2:
                todolist.display_tasks()
            elif choice == 3:
                todolist.delete_task()
            elif choice == 4:
                todolist.completed_task()
            elif choice == 5: 
                break
            elif choice == 6:
                quit()
            else:
                print("Enter correct choice")

class entertainment:
    def sites():
        print("Following are some websites to watch:")
        print('+--------------------------------+')
        print('|      WEBSITES AVAILABLE        |')
        print('+--------------------------------+')
        print('|1. Youtube                      |')
        print('|2. Netflix                      |')
        print('|3. Disney+ Hotstar              |')
        print('|4. Amazon Prime Video           |')
        print('+--------------------------------+')
        print()
        choice = int(input("Enter choice(1/2/3/4): "))
        print()
        if choice == 1:
            webbrowser.open('https://www.youtube.com')
        elif choice == 2:
            webbrowser.open('https://www.netflix.com/in/')
        elif choice == 3:
            webbrowser.open('https://www.hotstar.com/in')
        elif choice == 4:
            webbrowser.open('https://www.primevideo.com')
        else:
            print("Enter correct choice")
    
    def jokes():
        more = 'yes'
        while more == 'yes':
            if more == 'no':
                break
            joke = pyjokes.get_joke(language="en", category="neutral")
            print(joke)
            print()
            more = input("Would you like to hear more jokes? (yes/no): ")
            print()
    
    def rockpaperscissors():
        print("Welcome to the game Rock Paper and Scissors!!")
        print()
        rules = input("Do you know the rules of the game? (yes/no): ")
        print()
        if rules[0].lower() == 'n':
            print('=========================================')
            print('|               RULES                   |')
            print('=========================================')
            print("| The rules of the game are as follows: |")
            print("| Rock V/s Paper -- Paper Wins!         |")
            print("| Scissors V/s Rock -- Rock Wins!       |")
            print("| Paper V/s Scissors -- Scissors Wins!  |")
            print('=========================================')
        else:
            print("Okay! Let's Proceed with the game!")
        print()
        while True:
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print('            MOVES              ')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print(' 1. Rock                       ')
            print(' 2. Paper                      ')
            print(' 3. Scissors                   ')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print()
            user = int(input("Your Move(1/2/3): "))
            if user < 1 or user > 3:
                print("Enter valid input")
                user = int(input("Your Move(1/2/3): "))
            if user == 1:
                user_choice = 'Rock'
            elif user == 2:
                user_choice = 'Paper'
            else:
                user_choice = 'Scissors'
            print()
            print("You chose...{}".format(user_choice))
            computer = random.randint(1,3)
            while computer == user:
                computer = random.randint(1,3)
            if computer == 1:
                comp_choice = 'Rock'
            elif computer == 2:
                comp_choice = 'Paper'
            else:
                comp_choice = 'Scissors'
            print()
            print("Computer chose...{}".format(comp_choice))
            print()
            if user == 1 and computer == 2 or user == 2 and computer == 1:
                result = 2
            elif user == 1 and computer == 3 or user == 3 and computer == 1:
                result = 1
            else:
                result = 3
            if result == user:
                print("----------------YOU WIN!!------------------")
            else:
                print("------------COMPUTER WINS!!----------------")
            print()
            choice = input("Would you like to play again?(yes/no):  ")
            print()
            if choice == 'no':
                print("Thanks for Playing!")
                print()
                break

    def entertainment_main():
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print("          YOU HAVE EARNED SOME ENTERTAINMENT TIME!!          ")
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print("                 WELCOME TO ENTERTAINMENT!                   ")
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print()
        while True:
            print('+-----------------------------------------------------------+')
            print('|                Entertainment Categories                   |')
            print('+-----------------------------------------------------------+')
            print('| 1. TV Shows/Movies/Videos                                 |')
            print('| 2. Jokes                                                  |')
            print('| 3. Rock Paper Scissors                                    |')
            print('| 4. Main Menu                                              |')
            print('| 5. Exit                                                   |')
            print('+-----------------------------------------------------------+') 
            print()   
            choice = int(input("Enter your choice(1/2/3/4/5): "))
            print()
            if choice == 1:
                entertainment.sites()
            elif choice == 2:
                entertainment.jokes()
            elif choice == 3:
                entertainment.rockpaperscissors()
            elif choice == 4:
                break
            elif choice == 5:
                quit()
            else:
                print("Kindly Enter Valid Input")
                print()

class flashcard:
    def add_flashcard():
        while True: 
            f = open("flashcard.csv", "a", newline='')
            writer = csv.writer(f)
            header = ['Word', 'Definition']
            data = []
            if f.tell() == 0: #if header does not exist
                writer.writerow(header)
            for i in range(1):
                word = input("Enter term: ")
                print()
                definition = input("Enter Definition of term: ")
                print()
                record = [word, definition]
                data.append(record)
            writer.writerows(data)
            f.close()
            print('========================')
            print("Card Added Successfully!")
            print("========================")
            print()
            more = input("Would you like to add more cards?(yes/no): ")
            print()
            if more == 'no':
                break
        
    def read_flashcard():
        try:
            with open ("flashcard.csv", "r") as f:
                count = 0
                record = []
                reader = csv.reader(f)
                next(f)
                for row in reader: #creating a list with all cards
                    record.append([row[0], row[1]]) 
                if record == []: #if file is empty
                    print("No Flashcards Found")
                    print()
                    ch1 = input("Would you like to add cards? (yes/no): ")
                    if ch1.lower() == 'yes':
                        print()
                        flashcard.add_flashcard()
                    elif ch1.lower() == 'no':
                        pass
                    else: 
                        print("Enter Valid Input")
                        print()
                        ch1 = input("Would you like to add cards? (yes/no): ")
                else:
                    for row in record: #displaying all cards made
                        count += 1
                        print(str(count)+'.', row[0], ':', row[1])
                    print()
        except: #if file does not exist
            print("You Haven't Added any Flashcards yet!")
            print()
            ch2 = input("Would you like to add flashcards? (yes/no)")
            print()
            if ch2.lower() == 'yes':
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print("Welcome to Flashcard Maker!! Proceed with making your first card!!")
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print()
                flashcard.add_flashcard()
            elif ch2.lower() == 'no':
                print()
                print("No Worries! Start making your cards soon!")
            else:
                print("Enter Valid Input")
                print()
                ch2 = input("Would you like to add flashcards? (yes/no): ")

    def delete_flashcard():
        while True:
            print('+----------------------------------------------+')
            print('|                   Delete                     |')
            print('+----------------------------------------------+')
            print('| 1. Delete one Flashcard                      |')
            print('| 2. Delete all Flashcards                     |')
            print('+----------------------------------------------+') 
            print('| 3. Flashcard Menu                            |')
            print('+----------------------------------------------+') 
            print()
            choice = int(input("Enter Choice(1/2/3): "))
            print()
            if choice == 1:
                try:
                    with open("flashcard.csv", "r") as f:
                        count = 0
                        record = []
                        reader = csv.reader(f)
                        next(f)
                        for row in reader:
                            record.append([row[0], row[1]])
                        if reader == []:
                            print("No Flashcards available for Deletion")
                        print()
                        print("The Cards Made till date:-") #displaying entries
                        for i in record:
                            count += 1 
                            print(str(count)+'.', i[0], ':', i[1])
                        print()
                        position = int(input("Enter the position of the task to be deleted: "))
                        print() 
                        del record[position-1] #deleting specified card
                        print('=========================')
                        print("Card Deleted Successfully")
                        print('=========================')
                        print()
                    f = open("flashcard.csv","w")
                    writer = csv.writer(f) 
                    header = ['Word', 'Definition']
                    writer.writerow(header)
                    writer.writerows(record) #rewritting all cards except deleted card
                    f.close()
                except:
                    print("You haven't added any Flashcards yet!")
            elif choice == 2:
                try:
                    os.remove("flashcard.csv")
                    print('=================================')
                    print("All Entries Deleted Successfully")
                    print('=================================')
                    print()
                except:
                    print("No Cards Available for Deletion")
                    print()
            elif choice == 3:
                break
    
    def quiz_flashcards():
        try:
            f = open ("flashcard.csv", "r")
            record = []
            reader = csv.reader(f)
            next(f)
            for row in reader: #creating a list with all cards
                record.append([row[0], row[1]]) 
            if record == []: #if file is empty
                print("You Haven't Added any Cards!!")
                print()
            else:
                while True:
                    for terms in record:
                        word = terms[0] 
                        print("What is the definition of {}?".format(word))
                        print()
                        answer = input("Answer: ")
                        print()
                        if answer.lower() == terms[1].strip().lower():
                            print("-------------Correct Answer-------------")
                            print()
                        else:
                            print("--------------Wrong Answer--------------")
                            print()
                    more = input("Would you like to practice again? (yes/no): ")
                    if more == 'no':
                        print()
                        break
        except: #if file does not exist
            print("You Haven't Added any Cards!!")
            
    def flashcard_main():
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print("              WELCOME TO FLASHCARD MAKER!                ")
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print()
        while True:
            print('+-------------------------------------------------------+')
            print('|                Flashcard Categories                   |')
            print('+-------------------------------------------------------+')
            print('| 1. Add Flashcard                                      |')
            print('| 2. Read Flashcards                                    |')
            print('| 3. Delete Flashcards                                  |')
            print('| 4. Quiz on Flashcards                                 |')
            print('| 5. Main Menu                                          |')
            print('| 6. Exit                                               |')
            print('+-------------------------------------------------------+') 
            print()   
            choice = int(input("Enter Choice (1/2/3/4/5/6): "))
            print() #calling all related functions
            if choice == 1:
                flashcard.add_flashcard()
            elif choice == 2:
                flashcard.read_flashcard()
            elif choice == 3:
                flashcard.delete_flashcard()
            elif choice == 4:
                flashcard.quiz_flashcards()
            elif choice == 5: #returning to main menu
                break
            elif choice == 6:
                quit() #exiting from file
            else:
                print("Enter Valid Choice")

class weather:
    def forecast():
        while True:
            city = input("Enter City Name: ")
            print()
            print("Displaying Weather for {}...".format(city))
            print()
            url = 'https://wttr.in/{}'.format(city)
            req = requests.get(url)
            print(req.text)
            print()
            more = input("Would you like to see forecast for another city ? (yes/no): ")
            print()
            if more.lower() == 'no':
                print()
                break

    def weather_main():
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print("              WELCOME TO WEATHER FORECAST!               ")
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print()
        while True:
            print('+-------------------------------------------------------+')
            print('|            Weather Forecast Categories                |')
            print('+-------------------------------------------------------+')
            print('| 1. Weather Forecast                                   |')
            print('| 2. Main Menu                                          |')
            print('| 3. Exit                                               |')
            print('+-------------------------------------------------------+') 
            print()   
            choice = int(input("Enter Choice (1/2/3): "))
            print() #calling all related functions
            if choice == 1:
                weather.forecast()
            elif choice == 2:
                break
            elif choice == 3:
                quit()
            else:
                print("Enter Valid Choice")

class calculator:
    def addition():
        values = []
        sizenumbers = int(input("Enter how many numbers you would like to add: "))
        print()
        for i in range(sizenumbers):
            nums = input("Enter Number: ")
            print()
            values.append(nums)
        print("Result =", ' + '.join(values))
        print()
        result = 0 
        for element in values:
            result += int(element)
        print("Result =", result)
        print()
        
    def subtraction():
        numbers = []
        sizenumbers = int(input("Enter how many numbers you would like to subtract: "))
        print()
        for i in range(sizenumbers):
            nums = input("Enter Number: ")
            print()
            numbers.append(nums)
        print("Result =", ' - '.join(numbers)) 
        print()
        result = int(numbers[1])
        for element in numbers:
            result -= int(element)
        print("Result =", result)
        print()            

    def multiplication():
        numbers = []
        sizenumbers = int(input("Enter how many numbers you would like to multiply: "))
        print()
        for i in range(sizenumbers):
            nums = input("Enter Number: ")
            print()
            numbers.append(nums)
        print("Result =", ' ✕ '.join(numbers)) 
        print()
        result = 1
        for element in numbers:
            result *= int(element)
        print("Result =", result)
        print()            

    def division():
        numbers = []
        sizenumbers = int(input("Enter how many numbers you would like to divide: "))
        print()
        for i in range(sizenumbers):
            nums = input("Enter Number: ")
            print()
            numbers.append(nums)
        print("Result =", ' ÷ '.join(numbers)) 
        print()
        result = int(numbers[0])
        for element in numbers:
            if element == numbers[0]:
                pass
            else:
                result = result/int(element)
        print("Result =", result)
        print()            

    def squareroot():
        number = int(input("Enter Number: "))
        print()
        root = math.sqrt(number)
        print("Result =", ' √', number)
        print()
        print("Result =", root)
        print()

    def calculator_main():
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print("                WELCOME TO CALCULATOR!                ")
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print()
        while True:
            print('+-----------------------------------------------------+')
            print('|             Calculator Categories                   |')
            print('+-----------------------------------------------------+')
            print('| 1. Addition                                         |')
            print('| 2. Subtraction                                      |')
            print('| 3. Multiplication                                   |')
            print('| 4. Division                                         |')
            print('| 5. Square root                                      |')
            print('| 6. Main Menu                                        |')
            print('| 7. Exit                                             |')
            print('+-----------------------------------------------------+') 
            print()   
            choice = int(input("Enter Choice (1/2/3/4/5/6/7): "))
            print() #calling all related functions
            if choice == 1:
                calculator.addition()
            elif choice == 2:
                calculator.subtraction()
            elif choice == 3:
                calculator.multiplication()
            elif choice == 4:
                calculator.division()
            elif choice == 5:
                calculator.squareroot()
            elif choice == 6:
                break 
            elif choice == 7:
                quit()
            else:
                print("Enter Valid Choice")

print()
print(' =======================================================')
print('               WELCOME TO LIFE ASSISTANT!'               )
print(' =======================================================')
print()
while True:
    print('+-------------------------------------------------------+')
    print('|                     MAIN MENU                         |')
    print('+-------------------------------------------------------+')
    print('|   1. Journal                                          |')
    print('|   2. Clock                                            |')
    print('|   3. Calendar                                         |')
    print('|   4. To Do List                                       |')
    print('|   5. Flashcard                                        |')
    print('|   6. Weather Forecast                                 |')
    print('|   7. Calculator                                       |')
    print('|   8. Exit                                             |')
    print('+-------------------------------------------------------+') 
    print()   
    choice = input("Enter choice(1/2/3/4/5/6/7/8): ")
    print()
    if choice == '1':
        journal.journal_main()

    elif choice == '2':
        clock.clock_main()

    elif choice == '3':
        calendar.calendar_main()

    elif choice == '4':
        todolist.todolist_main()
        choice2 = input("Have you completed all your tasks(yes/no): ")
        print()
        if choice2 == 'yes': #displaying entertainment section only if tasks are completed
            entertainment.entertainment_main()
        else:
            print("Complete your tasks soon!!")

    elif choice == '5':
        flashcard.flashcard_main()

    elif choice == '6':
        weather.weather_main()

    elif choice == '7':
        calculator.calculator_main()

    elif choice == '8':
        break

    else:
        print("Kindly Enter Valid Input")
        print()
