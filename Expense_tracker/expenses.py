
# output welcome message
print("Welcome to Expense Tracker")

expenses = {
    "152" : {"Bills" : "Paid gas and electric"},
    "22.56" : {"Shopping" : "Brought snacks"},
    "72.51" : {"Entertainment" : "Netflix 1 year"},
    "42.81" : {"Bills" : "Water Bill"}
}

def create_expense():
    # prompt for an expense ammount
    expense = format(float(input("Please enter an Expense to track:\n")), '.2f')
    #prompt for expense category
    category = input("Please enter what category this expense falls into:\n")
    #prompt for expense description
    description = input("Please give a brief description for this expense:\n")

    expenses[expense] = {category : description}

    print(expenses)
#store data

def total():
    cost_total = 0
    for x in expenses:
        try:
            cost_total += float(x)
            
        except TypeError:
            print("A type error has occurred!")
    print(f"Your total is £{cost_total}")

def categories():
    
    category = {}
    for x in expenses:
    
        for y in expenses[x]:
            if y in category:
                number = category.get(y)
                category[y] = float(number) + float(x)
            else:
                category.update({y: x})
                #print("category created")
            
        
    for x in category:
        print(f"{x} Total: £{category[x]}")
            

def details():
    for x in expenses:
        for y in expenses[x]:
            print(f"Cost: £{x}, For: {y}, Notes: {expenses[x][y]}")

def summary():
    print("#####--Start-#####")
    print("#####--Categories--#####")
    categories()
    print("#####--Details--#####")
    details()
    print("#####--Total--#####")
    total()

summary()


print("Thank you for using Expense Track, Have a nice day!")
# create_expense()
# create_expense()

# total()
# print("╪" *200)
# categories()
#display function, show total spent, show total per category, all expenses listed with details

#remember defensive programming checks

#thank you for using message at the end



# stretch: store in local file, so data persists, json? on load check for file and read, on adding item, write to file?