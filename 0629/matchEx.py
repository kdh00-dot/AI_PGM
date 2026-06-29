score = int(input("enter score:"))
oneDigit = score // 10
match oneDigit:
    case 10 | 9 :
        print("Excellent!")
    case 8:
        print("Good job!")
    case 7:
        print("You can do better.")
    case _:
        print("You need to improve your perfomance.")

print("thank you for using the grade evaluator.")