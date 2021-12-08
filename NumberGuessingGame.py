import random

def again():
    main()

def main():
    try:
        ua = int(input("Insert a number from 1 to 10: "))
    except:
        print("It must be a number from 1 to 10: ")

    ra = random.randint(1,10)

    if ra == ua:
        print("Correct!")
        t = input("Do you want to try again? [y/n]: ")
    else:
        print("Wrong!")
        t = input("Do you want to try again? [y/n]: ")

    if t == "y"or t == "yes" or t == "Y" or t == "Yes" or t == "YES":
        again()
    elif t == "n"or t == "no" or t == "N" or t == "No" or t == "NO":
        quit()

main()