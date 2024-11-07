
import json


expenses = {
    "152" : {"Bills" : "Paid gas and electric"},
    "22.56" : {"Shopping" : "Brought snacks"},
    "72.51" : {"Entertainment" : "Netflix 1 year"},
    "42.81" : {"Bills" : "Water Bill"}
}

def create_expense():
    # prompt for an expense ammount
    try:
        expense = format(float(input("Please enter an Expense (e.g 20.50)to track:\n")), '.2f')

        if float(expense) < 0:
            print("I'm sorry but that is not a valid number, defaulting value to 0")
            expense = 0
        #prompt for expense category
        category = input("Please enter what category this expense falls into:\n")
        #prompt for expense description
        description = input("Please give a brief description for this expense:\n")

        expenses[expense] = {category : description}
        print("Expense successfully added!\n")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An error has occured: {e}")

def total():
    cost_total = 0
    for x in expenses:
        try:
            cost_total += float(x)
            
        except TypeError:
            print("A type error has occurred!")
        except ValueError:
            print("A value error has occured")

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

def summary(): #formatting, and calling functions to print the summary
    print("#####--Start-#####")
    print("#####--Categories--#####")
    categories()
    print("#####--Details--#####")
    details()
    print("#####--Total--#####")
    total()

def save():
    #savejson = json.dumps(expenses) 

    with open("my_expenses.json", "w") as fp:
        json.dump(expenses, fp)

    print("File successfully saved")

def load():
    f = open("my_expenses.json")
    load_file = json.load(f)
    print(f"file:\n{load_file}")
    clear()
    expenses.update(load_file)
    print("File successfully loaded")
    

def delete():
    summary()
    deleting = input("Which item do you want to delete from your list, please type the ammount:\n")
    if deleting == "":
        expenses.clear()
    elif deleting in expenses:
        del expenses[deleting]
        print("Entry successfully deleted\n")
    else:
        print(f"Sorry, could not find a match for {deleting} in your list")

def clear():
    expenses.clear()
    
    print("Your list has been cleared!")

#program start user welcome
print("Welcome to Expense Tracker")


while True:
    command = input("How can we help you today? type 'help' for a list of options\n")
    match command:

        case 'help':
            print("You can type: \nhelp - To show the help menu.")
            print("new - To add a new expense.")
            print("total - To show the total of expenses.")
            print("details - To show all the details of your expenses")
            print("category - To view a breakdown of expenses by category.")
            print("summary - To see a summary of all expenses.")
            print("save - To save your expense list")
            print("load - To load your expense list")
            print("delete - To delete an item from your expense list")
            print("clear - To clear your expense list")
            print("exit - To exit the expense program")
            
        case 'new':
            create_expense()
            
        case 'total':
            total()
            
        case 'details':
            details()
            
        case 'category':
            categories()
            
        case 'summary':
            summary()
            
        case 'save':
            save()
        case 'load':
            load()
        case 'delete':
            delete()
        case 'clear':
            clear()
            print("Your expenses list has been cleared!\n")
        case 'exit':
            break
        case _:
            print("Sorry, that is not a recognised command, type 'help' to see a list of available commands\n")
            


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