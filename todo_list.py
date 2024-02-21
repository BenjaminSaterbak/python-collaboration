
import os

def main():
    os.system('cls')
    print("""
Welcome to Benjamin's To-do List Program
-----------------------------------------
Please Choose an action below:
1) Add a task
2) View all Tasks
3) Mark Tasks as Complete
4) Delete Tasks""")
    while True:
        userinput = int(input("Please enter a number (1-4): "))
        if userinput == 1:
            task = input("What task would you like to add?: ")
            add_task(database,task)
            input("Your task ("+task+") was successfully added to the task list. Press enter to continue.")
            break
        elif userinput == 2:
            view_tasks(database)
        elif userinput == 3:
            task = input("What task would you like to mark as complete?: ")




def initialize_database():
    database = set({})
    return database

def add_task(database,task):
    database.add(task)
    
def view_tasks(database):
    print(database)

def mark_complete(databse,task):
    if task in database:
        database.remove(task)
    else:
        print("Your task was not found")
    
    

database = initialize_database()

while True:
    main()