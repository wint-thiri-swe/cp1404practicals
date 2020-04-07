name = input("enter name")
MENU = "(H)ello\n(G)oodbye\n(Q)uit"
print(MENU)
choice = input().upper()
while choice != "Q":
    if choice == "H":
        print("Hello", name)
    elif choice == "G":
        print("Goodbye", name)
    else:
        print("invalid option")
    print(MENU)
    choice = input().upper()
print("finished")
