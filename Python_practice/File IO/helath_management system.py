def atime():
    import datetime
    a = datetime.datetime.now()
    return a.strftime("%x " + "%X")
time = atime()

def makhdoom():
    print("\n1: Retrieve\n2: Submit")
    rs = int(input("Select a number: "))
    # For writing data
    if rs == 2:
        print("\n1: Cars\n2: Foods")
        cf = int(input("Select a number: "))
        if cf == 1:
            with open("MakhdoomCar.txt", "a") as f:
                mc = input()
                f.write("\n" + time + " " + mc)
        elif cf == 2:
            with open("MakhdoomFood.txt", "a") as f:
                mf = input()
                f.write("\n" + time + " " + mf)
        else:
            print("\nInvalid input! Try Again")
    # For reading data
    elif rs == 1:
        print("\n1: Cars\n2: Foods")
        cf = int(input("1 or 2 : "))
        if cf == 1:
            with open("MakhdoomCar.txt") as f:
                a = f.read()
                print(a)
        elif cf == 2:
            with open("MakhdoomFood.txt") as f:
                a = f.read()
                print(a)
        else:
            print("Invalid input! Try Again")
    else:
        print("\nInvalid Selection please try again")


def hassan():
    print("\n1: Retrieve\n2: Submit")
    rs = int(input("Select a number: "))
    # For writing data
    if rs == 2:
        print("\n1: Cars\n2: Foods")
        cf = int(input("Select a number: "))
        if cf == 1:
            with open("HassanCar.txt", "a") as f:
                mc = input()
                f.write("\n" + time + " " + mc)
        elif cf == 2:
            with open("HassanFood.txt", "a") as f:
                mf = input()
                f.write("\n" + time + " " + mf)
        else:
            print("\nInvalid input! Try Again")
    # For reading data
    elif rs == 1:
        print("\n1: Cars\n2: Foods")
        cf = int(input("1 or 2 : "))
        if cf == 1:
            with open("HassanCar.txt") as f:
                a = f.read()
                print(a)
        elif cf == 2:
            with open("HassanFood.txt") as f:
                a = f.read()
                print(a)
        else:
            print("Invalid input! Try Again")
    else:
        print("\nInvalid Selection please try again")

def faizan():
    print("\n1: Retrieve\n2: Submit")
    rs = int(input("Select a number: "))
    # For writing data
    if rs == 2:
        print("\n1: Cars\n2: Foods")
        cf = int(input("Select a number: "))
        if cf == 1:
            with open("faizanCar.txt", "a") as f:
                mc = input()
                f.write("\n" + time + " " + mc)
        elif cf == 2:
            with open("faizanFood.txt", "a") as f:
                mf = input()
                f.write("\n" + time + " " + mf)
        else:
            print("\nInvalid input! Try Again")
    # For reading data
    elif rs == 1:
        print("\n1: Cars\n2: Foods")
        cf = int(input("1 or 2 : "))
        if cf == 1:
            with open("faizanCar.txt") as f:
                a = f.read()
                print(a)
        elif cf == 2:
            with open("faizanFood.txt") as f:
                a = f.read()
                print(a)
        else:
            print("Invalid input! Try Again")
    else:
        print("\nInvalid Selection please try again")


q = 2
while q == 2:
    print("\n1: Makhdoom\n2: Hassan\n3: Faizan")
    name = int(input("Select a number: "))
    if name == 1:
        makhdoom()
    elif name == 2:
        hassan()
    elif name == 3:
        faizan()
    else:
        print("Invalid")

    print("\n1: Quit the program\n2; Rerun the program")
    q = int(input("Select a number: "))
    if q == 1:
        print("Program quit successfully ")
    else:
        print()

