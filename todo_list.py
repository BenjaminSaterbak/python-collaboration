
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
            mark_complete(database,databasec,task)
            print("Your list of completed tasks is:")
            print(databasec)
        elif userinput == 4:
            task = input("What task would you like to delete?: ")
            task_delete(database,task)
            print("Remaining tasks:")
            print(database)




def initialize_databases():
    database = set({})
    databasec = set({})
    return database,databasec

def add_task(database,task):
    database.add(task)
    
def view_tasks(database):
    print(database)

def mark_complete(database,databasec,task):
    if task in database:
        database.remove(task)
        databasec.add(task)
        
    else:
        print("Your task was not found")

def task_delete(database,task):
    if task in database:
        database.remove(task)

    else:
        print("Your task was not found")
    
    

database,databasec = initialize_databases()

while True:
    main()