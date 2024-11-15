import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.font as tkFont
import random
import json

#Variables to be used in the application
questions = {
    "1": "What is the capital of France?", 
    "2": "Which element has the chemical symbol 'O'?",
    "3": "Who wrote 'To Kill a Mockingbird?",
    "4": "What is the largest planet in our solar system?",
    "5": "What year did the Titanic sink?",
    "6": "What is the square root of 64?",
    "7": "Who painted the Mona Lisa?",
    "8": "What is the capital of Japan?",
    "9": "Which planet is known as the Red Planet?",
    "10": "Who developed the theory of relativity?",
    "11": "What is the chemical symbol for gold?",
    "12": "Who is the author of 'Pride and Prejudice'?",
    "13": "What is the smallest prime number?",
    "14": "Which planet is closest to the sun?",
    "15": "What is the currency of Japan?",
    "16": "Who discovered penicillin",
    "17": "What is the hardest substance on Earth?",
    "18": "What is the largest ocean on Earth?",
    "19": "Who was the first person to walk on the moon?",
    "20": "Which country hosted the 2016 Summer Olympics?",
    "21":"What is the main ingredient in traditional Japanese miso soup?",
    "22":"Which country is known as the Land of the Rising Sun?",
    "23":"What is the largest mammal in the world?",
    "24":"Who wrote the play 'Romeo and Juliet'?",
    "25":"What is the capital city of Australia?",
    "26":"Which planet has the most moons?",
    "27":"What is the smallest country in the world by area?",
    "28":"Who painted the ceiling of the Sistine Chapel?",
    "29":"What is the longest river in the world?",
    "30":"Which element is said to keep bones strong?",
    "31":"What is the speed of light in a vacuum",
    "32":"Who is known as the 'Father of Computers'?",
    "33":"What is the chemical formula for table salt?",
    "34":"Which planet is known for its rings?",
    "35":"Who wrote 'The Odyssey'?",
    "36":"What is the powerhouse of the cell?",
    "37":"Which gas is most abundant in the Earth's atmosphere?",
    "38":"Who developed the polio vaccine?",
    "39":"What is the capital of Canada?",
    "40":"Which element has the atomic number 1?"
    }
answers = {
    "1" : ["Paris","Berlin", "Madrid", "Rome"],
    "2" : ["Oxygen","Gold", "Silver", "Hydrogen"],
    "3" : ["Harper Lee","F.Scott Fitzgerald","J.D. Salinger","Mark Twain"],
    "4" : ["Jupiter","Earth","Venus","Mars"],
    "5" : ["1912","1905","1918","1923"],
    "6" : ["8","6","10","12"],
    "7" : ["Leonardo Da Vinci","Vincent Van Gogh","Pablo Picasso","Claude Monet"],
    "8" : ["Tokyo","Beijing","Seoul","Bangkok"],
    "9" : ["Mars","Earth","Jupiter","Saturn"],
    "10" : ["Albert Einstein","Isaac Newton","Nikola Tesla","Galileo Galilei"],
    "11" : ["AU","Ag","Gd","Ga"],
    "12" : ["Jane Austin","Charlotte Brontë","Emily Brontë","Mary Shelley"],
    "13" : ["2","1","3","5"],
    "14" : ["Mercury","Venus","Earth","Mars"],
    "15" : ["Yen","Won","Yuan","Ringgit"],
    "16" : ["Alexander Flemming","Marie Curie","Louis Pasteur","Gregor Mendel"],
    "17" : ["Diamond","Gold","Titanium","Platimun"],
    "18" : ["Pacific Ocean","Atlantic Ocean","Indian Ocean","Southern Ocean"],
    "19" : ["Neil Armstrong","Buzz Aldrin","Yuri Gagarin","Michael Collins"],
    "20" : ["Brazil","China","United Kingdom","Russia"],
    "21" : ["Miso paste","Tofu","Seaweed","Rice"],
    "22" : ["Japan","China","South Korea","Thailand"],
    "23" : ["Blue Whale","Elephant","Giraffe","Great White Shark"],
    "24" : ["William Shakespear","Christopher Marlowe","Ben Jonson","John Webster"],
    "25" : ["Canberra","Sydney","Melbourne","Brisbane"],
    "26" : ["Jupiter","Earth","Mars","Saturn"],
    "27" : ["Vatican City","San Marino","Monaco","Liechtenstein"],
    "28" : ["Michelangelo","Raphael","Leonardo Da Vinci","Donatello"],
    "29" : ["Nile River","Amazon River","Yangtze River","Mississippi River"],
    "30" : ["Calcium","Iron","Potassium","Sodium"],
    "31" : ["299,792 km/s","300,000 km/s","150,000 km/s","60,000 km/s"],
    "32" : ["Charles Babbage","Alan Turing","John Von Neumann","Steve Jobs"],
    "33" : ["NaCl","NaCO3","KCl","NaOH"],
    "34" : ["Saturn","Jupiter","Uranus","Neptune"],
    "35" : ["Homer","Virgil","Sophocles","Aristophanes"],
    "36" : ["Mitochondria","Nucleus","Ribosome","Endoplasmic Reticulum"],
    "37" : ["Nitrogen","Oxygen","Carbon Dioxide","Hydrogen"],
    "38" : ["Jonas Salk","Alexander Flemming","Edward Jenner","Louis Pasteur"],
    "39" : ["Ottawa","Toronto","Vancouver","Montreal"],
    "40" : ["Hydrogen","Helium","Lithium","Beryllium"]
}
questions_file ="questions.json"
answers_file = "answers.json"
quiz_length = 10
question_count = 1
answer_a = ""
answer_b = ""
answer_c = ""
answer_d = ""
correct_answer = 1
score = 0
question_list = ""
answer_list = ""

#Creates the application window
root = tk.Tk()
root.title('Quiz Game')
root.geometry('600x400')
#root.config(bg="skyblue")
root.resizable(height=None, width=None)


#Function to initialize the quiz
def load_game():
    global question_list, answer_list
    if type(quiz_length) == int:
        question_list = random.sample(range(1,len(questions)), quiz_length)
    else:
        print(quiz_length)
        
        question_list = random.sample(range(1,len(questions)), int(quiz_length))
        print(question_list)
    answer_list = random.sample(range(0,4), 4)
    
    play()

#Function to create and handle playing the quiz
def play():
    global correct_answer, question_list, answer_list, answer_a, answer_b, answer_c, answer_d, home_button, questions
    destroy()
    title.grid()
    score_counter.place(x=475, y=0)
    home_button.place(x=10, y=350)
    answer_list = random.sample(range(0,4), 4)
    display_label.config(text=f"Question {question_count}:\n {questions[str(question_list[question_count -1])]}")
    answer_a_button.grid(row=4, column=1, padx=15, pady=15, ipady=10, sticky='e')
    answer_b_button.grid(row=4, column=2, padx=15, pady=15, ipady=10, sticky='w')
    answer_c_button.grid(row=5, column=1, padx=15, pady=15, ipady=10, sticky='e')
    answer_d_button.grid(row=5, column=2, padx=15, pady=15, ipady=10, sticky='w')
    
    answer_a = answers[str(question_list[question_count - 1])][answer_list[0]]
    answer_b = answers[str(question_list[question_count - 1])][answer_list[1]]
    answer_c = answers[str(question_list[question_count - 1])][answer_list[2]]
    answer_d = answers[str(question_list[question_count - 1])][answer_list[3]]
    
    answer_a_button.config(text= f"A: {answer_a}")
    answer_b_button.config(text=f"B: {answer_b}")
    answer_c_button.config(text=f"C: {answer_c}")
    answer_d_button.config(text=f"D: {answer_d}")
    correct_answer = answers[str(question_list[question_count -1])][0]



#Function to determine whether the answer is correct and what to do next
def answer(choice):
    global correct_answer, question_count, quiz_length, score
    destroy()
    score_counter.place(x=475, y=0)
    if choice == correct_answer:
        display_label.config(text="That is correct!")
        score += 1
    else:
        display_label.config(text="Sorry, that is not correct!")

    score_counter.config(text=f"Score: {score}")
    if question_count < int(quiz_length):
        next_button.config(text="Next Question")
        next_button.grid(column=2, row=5)
        home_button.place(x=10, y=350)
    else:
        next_button.grid_remove()
        home_button.place_forget()
        next_button.grid(column=2, row=5)
        next_button.config(text="Finish")    

    
    
#Function to load the next question, or end the quiz if final question
def load_next():
    global question_count, answers_file
    question_count += 1
    if question_count <= int(quiz_length):
        destroy()
        home_button.place(x=10, y=350)  
        play()
    else:
        display_label.config(text=f"Thank you for playing\nYour final score was:\n{score}")
        next_button.grid_remove()
        home_button.place_forget()
        home_button.grid(column=2, row=5)
        home_button.config(text="Exit")    
        question_count = 1

#Function to save the quiz questions and answers to files, creates a new file if there is not one
def save():
    global questions_file, answers_file
    destroy()
    with open(questions_file, "w") as fp:
        json.dump(questions, fp)

    with open(answers_file, "w") as fp:
        json.dump(answers, fp)

    display_label.config(text="File successfully saved")
    home_button.place(x=10, y=350)

#Function to load the selected files into questions and answers
def load():
    destroy()
    clear()
    f = open("questions.json")
    load_file = json.load(f)
    print(f"file:\n{load_file}")
    
    questions.update(load_file)
    display_label.config(text="File successfully loaded")
    print(questions)
    
    f = open("answers.json")
    load_file = json.load(f)
    print(f"file:\n{load_file}")
    
    answers.update(load_file)
    display_label.config(text="File successfully loaded")

    home_button.place(x=10, y=350)

#Function to clear the questions and answers lists
def clear():
    questions.clear()
    answers.clear()
    print("Your list has been cleared!")

#Function to create the settings screen
def settings():
    destroy()
    display_label.config(text="")
    question_file_label.grid(row=2, column=2, padx=100, pady=5)
    question_file_in.grid(row=3, column=2, padx=200, pady=5)
    answer_file_label.grid(row=4, column=2, padx=200, pady=5)
    answer_file_in.grid(row=5, column=2, padx=200, pady=5)
    quiz_length_label.grid(row=6, column=2, padx=200, pady=5)
    quiz_length_in.grid(row=7, column=2, padx=200, pady=5)
    set_button.grid(row=8, column=2, padx=50, pady=5)
    home_button.place(x=10, y=350)

#Function called by save settings button, applys user specified settings from settings screen
def set_settings():
    global questions_file, answers_file, quiz_length
    if question_file_in.get != "":
        questions_entry = question_file_in.get()
        questions_file = f"{questions_entry}.json"

    if answer_file_in.get != "":
        answers_entry = answer_file_in.get()
        answers_file = f"{answers_entry}.json"

    if quiz_length_in.get != "":
        quiz_length = quiz_length_in.get()
    
    load_main()
    

#Clears the screen 
def destroy():
    score_counter.place_forget()
    save_button.grid_remove()
    load_button.grid_remove()
    settings_button.grid_remove()
    play_button.grid_remove()
    answer_a_button.grid_remove()
    answer_b_button.grid_remove()
    answer_c_button.grid_remove()
    answer_d_button.grid_remove()
    next_button.grid_remove()
    home_button.place_forget()
    question_file_label.grid_remove()
    question_file_in.grid_remove()
    answer_file_label.grid_remove()
    answer_file_in.grid_remove()
    quiz_length_label.grid_remove()
    quiz_length_in.grid_remove()
    set_button.grid_remove()
    home_button.grid_remove()

#Loads the home screen
def load_main():
    destroy()
    display_label.config(text="Please select an option from the left, or press play to begin")
    title.grid(row =0, column=1, columnspan = 3, pady=5, sticky='w', padx=150)
    save_button.grid(row=3, column=0, pady=5, padx=10, sticky='w')
    load_button.grid(row=4, column=0, pady=5, padx=10, sticky='w')
    settings_button.grid(row=5, column=0, pady=5, padx=10, sticky='w')
    display_label.grid(column=1, row=2, rowspan=2, columnspan=2, padx=100, pady=5, sticky='e')
    play_button.grid(column=1, row=5, ipadx=5, ipady=5, padx=5, pady=5,sticky='e' )


#Creating and screen elements
title = tk.Label(root, height=2, width=20, text="Quiz Game", font=tkFont.Font(size=20))
save_button = ttk.Button(root, text="Save",command = save)
load_button = ttk.Button(root, text="Load",command = load)
settings_button = ttk.Button(root, text="Settings", command =settings)
display_label = tk.Label(root, height = 5, width=50, text="Please press play to begin")
play_button = ttk.Button(root, text="Play!", command = load_game)
answer_a_button = ttk.Button(root, text="A:", width=25, command = lambda: answer(answer_a))
answer_b_button = ttk.Button(root, text="B:", width=25, command = lambda: answer(answer_b))
answer_c_button = ttk.Button(root, text="C:", width=25, command = lambda: answer(answer_c))
answer_d_button = ttk.Button(root, text="D:", width=25, command = lambda: answer(answer_d))

question_file_label = ttk.Label(root, text="Questions file:")
question_file_in = Entry(root)
answer_file_label = ttk.Label(root, text="Answers file:")
answer_file_in = Entry(root)
quiz_length_label = ttk.Label(root, text="Quiz length:")
quiz_length_in = Entry(root)
set_button = ttk.Button(root, text = "Save changes", command= set_settings)


next_button = ttk.Button(root, text="Next Question", command=load_next)
score_counter = tk.Label(root, text = f"Score: {score} ", font=tkFont.Font(size=15))
home_button = ttk.Button(root, text="Back", command=load_main)




#Initial loading of the main screen
load_main()

#Places the main display label below other widgets
display_label.lower()

#Main loop to keep the application screen running
root.mainloop()