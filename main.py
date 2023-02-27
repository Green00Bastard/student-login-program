def RunMenu(menuList):
    print(menuList[0])  # menu

    for x in range(1, len(menuList)):
        print(x, ": ",  menuList[x])

    menuChoice = int(input("Please make a selection: \n"))
  
    return menuChoice

continueLoop = True
while continueLoop:

    menuList = ["------MENU------\n\n", "Register Student", "Take register", "Assign Student to the class", "Exit"]
  
    menuChoice = RunMenu(menuList)

    if menuChoice == 1:
        print("Register student: \n")
    elif menuChoice == 2:
        print("Take register: \n")
    elif menuChoice == 3:
        print("Assign Student to the class: \n")
    else:
        print("Exiting program...\n", "Good bye")  
        continueLoop = False


  
    
  