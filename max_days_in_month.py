month = int(input("Enter a month number : "))

match month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print("Max. days are 31")

    case 4 | 6 | 9 | 11:
        print("Max. days are 30")

    case 2:
        print("Max. days are 28 or 29")

    case _:
        print("Invalid month number")
        
