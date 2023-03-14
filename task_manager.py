import datetime

#=====importing libraries===========
'''This is the section where you will import libraries'''

tasks = open("tasks.txt", "r+")               # Open the "tasks.txt" file
user = open("user.txt", "r+")                 # Open the "user.txt" flie

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''
user_read = user.read()                   # Read the first 5 characters of a line in a file and make it a variable
split = user_read.split(";")

username = split[0]
password = split[1]

print(username)
print(password)

question1 = input("Enter username: ").lower()  # Ask the user to enter a username

while question1 != username:                  # If users input doesnt match the set variable the following should happen
    print("Wrong username, try again")
    question1 = input("Enter username: ").lower()
else:
    print("Correct username")

question2 = input("Enter password: ").lower()

while question2 != password:                   # If users input doesnt match the set variable the following should happen
    print("Wrong password, try again")
    question2 = input("Enter password: ").lower()
else:
    print("Correct password")

while True:
    #presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
gr - generate report
ds - display stats
e - Exit
: ''').lower()

    if menu == 'r':            # if "r" is chosen then the following should happen
        pass
        '''In this block you will write code to add a new user to the user.txt file
        - You can follow the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise you present a relevant message.'''
        def reg_user():
            
            new_user = input("Enter new username: ").lower()

            if new_user == username:
                print("Username already used, choose another username")
                new_user = input("Enter new username: ").lower()
            
            new_pass = input("Enter new password: ").lower()
            new_pass1 = input("Enter new password again: ").lower()

            while new_pass1 != new_pass:
                print("The passwords don't match. Try again.")
                new_pass = input("Enter new password: ").lower()
                new_pass1 = input("Enter new password again: ").lower()
            else:
                print("Congratulations!! Your new username and password is stored!")
                user.write(f"\n{new_user} , {new_pass1} \n")
                user.close()

        reg_user()

    elif menu == 'a':               # if "a" is chosen then the following should happen
        pass
        '''In this block you will put code that will allow a user to add a new task to task.txt file
        - You can follow these steps:
            - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''
        def add_task():

            new_user = input("Enter your username: ")
            tasks.write(f"\n{new_user}")
            title = input("Enter your task title: ")
            tasks.write(f", {title}")
            description = input("Enter description of the task: ")
            tasks.write(f", {description}")
            due_date = input("Enter the due date of the task: ")
            tasks.write(f", {due_date}")
            current_date = datetime.date.today()
            tasks.write(f", {current_date}")
            taskCompleted = input("Is task completed Yes or No: ")
            tasks.write(f", {taskCompleted} \n")
    

        add_task()   

    elif menu == 'va':              # if "va" is chosen then the following should happen
        pass
        '''In this block you will put code so that the program will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the L1T19 pdf file page 6
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 in L1T19 pdf
            - It is much easier to read a file using a for loop.'''
        def view_all():

            task1 = tasks.read().replace(",","\n")
            print(task1)
    

        view_all()

    elif menu == 'vm':                 # if "vm" is chosen then the following should happen 
        pass
        '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the L1T19 pdf
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same you print the task in the format of output 2 shown in L1T19 pdf '''
        def view_mine():

            task1 = tasks.readline()
            print(task1.replace(",","\n"))
            task = (f"Number Task : Task \n [0] : Username \n {question1} : Title \n [2] : Description \n [3] : Due date \n [4] : Completed \n [-1] : Main menu ")
            print(task)
            edit = input("Edit the tasks[Edit] or back to menu[-1]").lower
            if edit == "edit":
                edit_num = int(input("Enter task number: "))
                print(task1.replace(",","\n"))

            completedTask = input("Is the task completed, yes or no? ").lower
            if completedTask == "yes":
                task1 = task.strip().split(",")
                task_complete = task1[4]= "task completed"
                print(task_complete)
            elif completedTask == "no":
                task1 = task.strip().split(",")
                task_complete = task1[4]= "task not completed"
                print(task_complete)

            elif edit == "-1":
                print("back to menu")

        

        view_mine()

#When the user chooses to generate reports, two text files, called
#task_overview.txt and user_overview.txt, should be generated. 



    elif menu == 'gr':
        task_view = open("task_overview.txt","r+")
        user_view = open("user_overview.txt","r+")

        completedtasks = 0
        incompletetasks = 0
        due_tasks = 0

        num_task = tasks.read()

        work = input("Is work complete, yes or no: ").lower()
            
        if work == "yes":
            completedtasks += 1
        elif work == "no":
            incompletetasks += 1

        date_today = input("Enter todays date: ")
        due_date = input("Enter task due date: ")
        if date_today >= due_date:
            due_tasks += 1
        
        incomplete_percent = incompletetasks * 100 / len(num_task)
        complete_percent = completedtasks * 100 / len(num_task)

        task_view.write(f"Number of tasks: {num_task} \n")
        task_view.write(f"Completed task: {completedtasks} \n")
        task_view.write(f"Incomplete tasks: {incompletetasks} \n")
        task_view.write(f"Tasks due: {due_tasks} \n")
        task_view.write(f"Incompleted task percentage: {incomplete_percent} \n")
        task_view.write(f"completed tasks percentage: {complete_percent} \n")

        
        num_user = user.read()


        user_view.write(f"Number of tasks: {num_user} \n")
        user_view.write(f"Completed task: {completedtasks} \n")
        user_view.write(f"Incomplete tasks: {incompletetasks} \n")
        user_view.write(f"Tasks due: {due_tasks} \n")
        user_view.write(f"Incompleted task percentage: {incomplete_percent} \n")
        user_view.write(f"completed tasks percentage: {complete_percent} \n")


        task_view.close()
        user_view.close()

#Modify the menu option that allows the admin to display statistics so that
#the reports generated are read from task_overview.txt and user_overview.txt

    elif menu == 'ds':
        task1 = tasks.readlines()
        task2 = len(task1)
        print(f"The number of tasks = {task2}")   # print the number of tasks
        user1 = user.readlines()
        user2 = len(user1)
        print(f"The number of users is = {user2}")  # print the number of users
        user.close()
        tasks.close()

    elif menu == 'e':             # if "e" is chosen then the following should happen
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")