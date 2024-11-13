import tkinter as tk
from tkinter import ttk
from tkinter import *
import json
import string

expenses = {
    "152.00" : {"Bills" : "Paid gas and electric"},
    "22.56" : {"Shopping" : "Brought snacks"},
    "72.51" : {"Entertainment" : "Netflix 1 year"},
    "42.81" : {"Bills" : "Water Bill"}
}

root = tk.Tk()
root.title('Expense Tracker')
root.geometry('700x500')
#root.config(bg="skyblue")

# creates main window

# summary = tk.Label(root, text="Hello prog")
# summary.pack(pady=5)


def summary():
    destroy()
    summary_text = ""
    category_text = categories()
    detail_text = details()
    total_text = total()

    summary_text = f"Summary\n {category_text}\n{detail_text}\n{total_text}"
    display_label.config(text=summary_text)

def categories():
    destroy()
    category = {}
    category_text= ""
    for x in expenses:
        for y in expenses[x]:
            if y in category:
                number = category.get(y)
                category[y] = float(number) + float(x)
            else:
                category.update({y: x})
                #print("category created")
            
    for x in category:
        category_text += (f"{x} Total: £{category[x]}\n")
            
    display_label.config(text=category_text)
    return category_text
    
def details():
    destroy()
    detail_text=""
    for x in expenses:
        for y in expenses[x]:
            detail_text += (f"Cost: £{x}, For: {y}, Notes: {expenses[x][y]}\n")
    display_label.config(text=detail_text)
    return detail_text

def total():
    destroy()
    total_text = "Your total is £"
    cost_total = 0
    for x in expenses:
        try:
            cost_total += float(x)
            
        except TypeError:
            print("A type error has occurred!")
        except ValueError:
            print("A value error has occured")
    total_text += str(cost_total)
    display_label.config(text=total_text)
    return total_text

def save():
    destroy()
    with open("my_expenses.json", "w") as fp:
        json.dump(expenses, fp)

    display_label.config(text="File successfully saved")

def load():
    destroy()
    f = open("my_expenses.json")
    load_file = json.load(f)
    print(f"file:\n{load_file}")
    clear()
    expenses.update(load_file)
    display_label.config(text="File successfully loaded")
    
def delete():
    destroy()
    summary()
    display_label.config(text="Which item do you want to delete from your list,\n please select from the menu:\n")
    create_delete_option()
    
        
def add():
    destroy()
    create_add()
    
    price = tk.StringVar()
    expense_category = tk.StringVar()
    details = tk.StringVar()
    display_label.config(text="")

    def push():
        expenses.update({format(float(price.get()), '.2f') : {expense_category.get() : details.get()}})
        
        refresh()
        destroy()
        display_label.config(text="Expense successfully added to list")

    #destroy()
    
    
    title_label.config(text = "Please enter details for the new expense:")
    price_label.config(text = "Cost:")
    price_input.config(textvariable = price)
    category_label.config(text="Category:")
    category_input.config(textvariable = expense_category)
    details_label.config(text="Details:")
    details_input.config(textvariable=details)
    add_expense_button.config(text="Add Expense", command=push)
    
    
    
def refresh():
    
    deleting_dropdown["menu"].delete(0, END)
    selected_option.set(list(expenses.keys())[0])
    new_options = expenses.keys()
    for options in new_options:
        #deleting_dropdown["menu"].add_command(label = options)
        deleting_dropdown["menu"].add_command(label = options, command = tk._setit(selected_option, options))


def create_delete_option():
    delete_title_label.grid()
    deleting_dropdown.grid()
    delete_option_button.grid()
    
    
def change_delete_label(*args):
    selected = selected_option.get()
    detail_text= ""
    delete_category = list(expenses[selected].keys())
    delete_detail = list(expenses[selected].values())
    # for x in expenses:
    #     for y in expenses[x]:
    #         detail_text += (f"Cost: £{x}, For: {y}, Notes: {expenses[x][y]}\n")
    detail_text= f"Cost: £{selected}\nCategory: {delete_category[0]}\nDetails: {delete_detail[0]}"
    display_label.config(text=detail_text)
    return detail_text

def remove(selected):
    expenses.pop(str(selected.get()))
    destroy()
    refresh()
    # selection_remove = deleting_dropdown['menu'].index(selected_option.get())
    # deleting_dropdown["menu"].delete(selection_remove)
    display_label.config(text="Entry successfully deleted\n")
    


def create_add():
    title_label.grid()
    price_label.grid()
    price_input.grid()
    category_label.grid()
    category_input.grid()
    details_label.grid()
    details_input.grid()
    add_expense_button.grid()
    


def destroy():
    # add widgets
    title_label.grid_remove()
    price_label.grid_remove()
    price_input.grid_remove()
    category_label.grid_remove()
    category_input.grid_remove()
    details_label.grid_remove()
    details_input.grid_remove()
    add_expense_button.grid_remove()
    # delete widgets
    delete_option_button.grid_remove()
    deleting_dropdown.grid_remove()
    delete_title_label.grid_remove()
    selected_option.set('Please select an expense')
def clear():
    destroy()
    expenses.clear()
    
    

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)





title = tk.Label(root, height=2, width=20, text="Expense Tracker")
title.grid(row =0, column=0, columnspan = 3)

#screen elements for adding an expense
title_label = tk.Label(root,text = "Please enter details for the new expense:", bg = "red")
price_label = tk.Label(root,text = "Cost:")
price_input = Entry(root)
category_label = tk.Label(root,text="Category:")
category_input = Entry(root)
details_label = tk.Label(root,text="Details:")
details_input = Entry(root)
add_expense_button = ttk.Button(root,text="Add Expense")

title_label.grid(column=1, row=2, pady=5, sticky='w')
price_label.grid(column=1, row=3, pady=5, sticky='w')
price_input.grid(column=1, row=4, pady=5, sticky='w')
category_label.grid(column=1, row=5, pady=5, sticky='w')
category_input.grid(column=1, row=6, pady=5, sticky='w')
details_label.grid(column=1, row=7, pady=5, sticky='w')
details_input.grid(column=1, row=8, pady=5, sticky='w')
add_expense_button.grid(column=1, row=9, pady=5, sticky='w')


# End of expense adding

selected_option = tk.StringVar(root)
selected_option.trace("w", change_delete_label)
delete_title_label = tk.Label(root,text = "Please select an expense to delete from the dropdown menu:", bg = "red")
deleting_dropdown = OptionMenu(root, selected_option, *expenses.keys())
delete_option_button = ttk.Button(root, text="Delete selected option", command=lambda: remove(selected_option))

deleting_dropdown.grid(column=1, row=3, pady=5, sticky='w', ipadx=50, padx=30)
delete_title_label.grid(column=1, row=2, pady=5, sticky='w')
delete_option_button.grid(column=1, row= 5, padx=30, pady=5 )




destroy()



summary_button = ttk.Button(root, text="Summary",command = summary)
summary_button.grid(row=2, column=0, pady=5, padx=10, sticky='w')

categories_button = ttk.Button(root, text="Categories",command = categories)
categories_button.grid(row=3, column=0, pady=5, padx=10, sticky='w')

total_button = ttk.Button(root, text="Total",command = total)
total_button.grid(row=4, column=0, pady=5, padx=10, sticky='w')

add_button = ttk.Button(root, text="Add Item",command = add)
add_button.grid(row=5, column=0, pady=5, padx=10, sticky='w')


delete_button = ttk.Button(root, text="Delete Item",command = delete)
delete_button.grid(row=6, column=0, pady=5, padx=10, sticky='w')

clear_button = ttk.Button(root, text="Clear List",command = clear)
clear_button.grid(row=7, column=0, pady=5, padx=10, sticky='w')

save_button = ttk.Button(root, text="Save",command = save)
save_button.grid(row=8, column=0, pady=5, padx=10, sticky='w')

load_button = ttk.Button(root, text="Load",command = load)
load_button.grid(row=9, column=0, pady=5, padx=10, sticky='w')



display_label = tk.Label(root, height = 20, width=50, text="Please select an option from the left")
display_label.grid(column=1, row=3,rowspan=7, sticky='w')
display_label.lower()

#create_expense function

#button to create expense
#button to delete expense
#button to show the total
#button to show the summary
#button to show the category breakdown
#dropdown menu to select categories in category view
#save and load buttons
#save and load functions



root.mainloop()
