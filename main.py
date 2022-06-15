choice = int()
x = float()
y = float()
solution = float()

if __name__ == '__main__':
    print("Calculator")
    print("Please select a mathematical operation (integer only):\nAddition (1), Subtraction (2), Multiplication (3), Division (4), Remainder (5)")

    choice = int(input("Enter your selection (integer only): "))
    if 0 < choice < 6:
        print("Please select two values (integer or decimal) for your calculation: ")
        x = float(input("Enter your first value: "))
        y = float(input("Enter your second value: "))
        if choice == 1:
            solution = (x+y)
            print(solution)
        elif choice == 2:
            solution = x - y
            print(solution)
        elif choice == 3:
            solution = x * y
            print(solution)
        elif choice == 4:
            solution = x / y
            print(solution)
        else:
            solution = x % y
            print(solution)
    else:
         print("Please input a selection from 1 through 5 as noted above.")

