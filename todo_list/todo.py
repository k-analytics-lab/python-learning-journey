print(5*"-","To Do List",5*"-")

tasks = []
while True:
    print("1.View Tasks\n2.Add Task\n3.Remove Task\n4.Exit")
    option = int(input("Enter your option: "))
    
    if option == 1:
        if len(tasks)==0:
            print("No tasks available\n")
        else:    
            num = 1
            print(5*"-","Your Tasks",5*"-")
            for task in tasks:
                print(f"{num}.{task}")
                num +=1
            print(22*"-")
            print()
    elif option == 2:
        add = input("Enter your Task: ")
        tasks.append(add)
        print("Task added successfully\n")
    elif option == 3:
        remove = int(input("Enter the task you want to remove: "))
        index_list = remove-1
        if remove < 1 or remove > len(tasks):
            print("Invalid task number\n")
            continue
        index_list = remove-1
        tasks.pop(index_list)
        print("Task removed successfully\n")
    elif option == 4:
        print("Exiting the Program ...")
        break
       


