def grade():
    average = float(input("What is your average for the course? "))
    if average >= 90:
        print("A")
    elif average >= 80:
        print("B")
    elif average >= 70:
        print("C")
    else:
        print("You can do better! ")
    return

if __name__ == "__main__":
    grade()