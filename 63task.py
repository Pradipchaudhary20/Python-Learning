#Write a Python program that asks the user to enter the names of n people, then prints all names that start with the letter 'B', and if no such names are found, it should display "No Name Found


def find_b_names():

    n = int(input("Enter the number of people: "))
    names = []
    for n in range(n):
        name = input("Enter a name: ").upper()
        names.append(name)
    found = False
    for name in names:
        if name.startswith('B'):
            print(name)
            found = True
    if not found:
        print("No Name Found")
find_b_names()
