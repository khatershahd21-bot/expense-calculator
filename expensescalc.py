expenses = []
while True:
            x = input("enter your expenses :")
            if x == "calc":
                break 
            try:
                x= int(x)
                expenses.append(x)
            except ValueError:
                print("Please enter a valid number or 'calc'.")
    
def expenses_calc( expenses):

    total = sum(expenses)
    average = total / len(expenses)
    minmum  = min(expenses)
    maximum = max(expenses)
    print("avg is : " , average , "\ntotal expenses is :" , total , "\nminmum expenses is :" , minmum , "\nmax expenses is :" , maximum)

expenses_calc(expenses) 