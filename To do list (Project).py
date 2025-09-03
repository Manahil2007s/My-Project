def to_do_list():
 tasks=[]

while True:
    print("1.Enter the task")
    print("2.Remove the task")
    print("3. View the task")
    print("4. Quit")
    choice=input("Enter your choice") 
    if choice=="1":
        task=input("Enter the task: ")
        tasks.append(task)
        print("task added")
    elif choice=="2":
            task=input("Enter the task to remove")
            if task in tasks:
                tasks.remove(task)
            else:
                print("Task not Found")
                end
    elif choice=="3":
                    print("Your task are: ")
                    for task in Tasks:
                        print(task)
    elif choice=="4":
                            break
    else:
                                print("Invalid choice")
    
