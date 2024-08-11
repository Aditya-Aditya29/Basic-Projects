def menu():
    return ("------Menu----------\n"
        "1:- Add\n"
        "2:- Delete\n"
        "3:- Show Tasks\n"
        "4:- Exit\n")


tasks=[]
Flag=True
while Flag:

    print(menu())
    try:
        user_input = int(input("Enter Number:- "))
    except ValueError:
        print("Enter a valid number")
        continue

    if user_input==1:
        print("------Adding a task------")
        task_user_input=input("Enter Task Name:-")
        if task_user_input:
            tasks.append(task_user_input)
            print("Task Added")
        else:
            print("Task name can't be empty")


    elif user_input ==2:
        print("Choose which task to delete")

        if tasks:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}:- {task}")
            try:
                del_user_input=int(input("Enter task number to delete:- "))
                if 1<= del_user_input <= len(tasks):
                    tasks.pop(del_user_input-1)
            except ValueError:
                print("Enter a valid number")


    elif user_input ==3:
        for i,task in enumerate(tasks,start=1):
            print(f"{i}:- {task}")

    elif user_input == 4:
        print("-----Exiting------")
        Flag=False
