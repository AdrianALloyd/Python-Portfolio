import random
import json
questions = {
    1: "What is the capital of France?", 
    2: "Which element has the chemical symbol 'O'?",
    3: "Who wrote 'To Kill a Mockingbird?",
    4: "What is the largest planet in our solar system?",
    5: "What year did the Titanic sink?",
    6: "What is the square root of 64?",
    7: "Who painted the Mona Lisa?",
    8: "What is the capital of Japan?",
    9: "Which planet is known as the Red Planet?",
    10: "Who developed the theory of relativity?",
    11: "What is the chemical symbol for gold?",
    12: "Who is the author of 'Pride and Prejudice'?",
    13: "What is the smallest prime number?",
    14: "Which planet is closest to the sun?",
    15: "What is the currency of Japan?",
    16: "Who discovered penicillin",
    17: "What is the hardest substance on Earth?",
    18: "What is the largest ocean on Earth?",
    19: "Who was the first person to walk on the moon?",
    20: "Which country hosted the 2016 Summer Olympics?",
    21:"What is the main ingredient in traditional Japanese miso soup?",
    22:"Which country is known as the Land of the Rising Sun?",
    23:"What is the largest mammal in the world?",
    24:"Who wrote the play 'Romeo and Juliet'?",
    25:"What is the capital city of Australia?",
    26:"Which planet has the most moons?",
    27:"What is the smallest country in the world by area?",
    28:"Who painted the ceiling of the Sistine Chapel?",
    29:"What is the longest river in the world?",
    30:"Which element is said to keep bones strong?",
    31:"What is the speed of light in a vacuum",
    32:"Who is known as the 'Father of Computers'?",
    33:"What is the chemical formula for table salt?",
    34:"Which planet is known for its rings?",
    35:"Who wrote 'The Odyssey'?",
    36:"What is the powerhouse of the cell?",
    37:"Which gas is most abundant in the Earth's atmosphere?",
    38:"Who developed the polio vaccine?",
    39:"What is the capital of Canada?",
    40:"Which element has the atomic number 1?"
    }

answers = {
    1 : ["Paris","Berlin", "Madrid", "Rome"],
    2 : ["Oxygen","Gold", "Silver", "Hydrogen"],
    3 : ["Harper Lee","F.Scott Fitzgerald","J.D. Salinger","Mark Twain"],
    4 : ["Jupiter","Earth","Venus","Mars"],
    5 : ["1912","1905","1918","1923"],
    6 : ["8","6","10","12"],
    7 : ["Leonardo Da Vinci","Vincent Van Gogh","Pablo Picasso","Claude Monet"],
    8 : ["Tokyo","Beijing","Seoul","Bangkok"],
    9 : ["Mars","Earth","Jupiter","Saturn"],
    10 : ["Albert Einstein","Isaac Newton","Nikola Tesla","Galileo Galilei"],
    11 : ["AU","Ag","Gd","Ga"],
    12 : ["Jane Austin","Charlotte Brontë","Emily Brontë","Mary Shelley"],
    13 : ["2","1","3","5"],
    14 : ["Mercury","Venus","Earth","Mars"],
    15 : ["Yen","Won","Yuan","Ringgit"],
    16 : ["Alexander Flemming","Marie Curie","Louis Pasteur","Gregor Mendel"],
    17 : ["Diamond","Gold","Titanium","Platimun"],
    18 : ["Pacific Ocean","Atlantic Ocean","Indian Ocean","Southern Ocean"],
    19 : ["Neil Armstrong","Buzz Aldrin","Yuri Gagarin","Michael Collins"],
    20 : ["Brazil","China","United Kingdom","Russia"],
    21 : ["Miso paste","Tofu","Seaweed","Rice"],
    22 : ["Japan","China","South Korea","Thailand"],
    23 : ["Blue Whale","Elephant","Giraffe","Great White Shark"],
    24 : ["William Shakespear","Christopher Marlowe","Ben Jonson","John Webster"],
    25 : ["Canberra","Sydney","Melbourne","Brisbane"],
    26 : ["Jupiter","Earth","Mars","Saturn"],
    27 : ["Vatican City","San Marino","Monaco","Liechtenstein"],
    28 : ["Michelangelo","Raphael","Leonardo Da Vinci","Donatello"],
    29 : ["Nile River","Amazon River","Yangtze River","Mississippi River"],
    30 : ["Calcium","Iron","Potassium","Sodium"],
    31 : ["299,792 km/s","300,000 km/s","150,000 km/s","60,000 km/s"],
    32 : ["Charles Babbage","Alan Turing","John Von Neumann","Steve Jobs"],
    33 : ["NaCl","NaCO3","KCl","NaOH"],
    34 : ["Saturn","Jupiter","Uranus","Neptune"],
    35 : ["Homer","Virgil","Sophocles","Aristophanes"],
    36 : ["Mitochondria","Nucleus","Ribosome","Endoplasmic Reticulum"],
    37 : ["Nitrogen","Oxygen","Carbon Dioxide","Hydrogen"],
    38 : ["Jonas Salk","Alexander Flemming","Edward Jenner","Louis Pasteur"],
    39 : ["Ottawa","Toronto","Vancouver","Montreal"],
    40 : ["Hydrogen","Helium","Lithium","Beryllium"]
}


#question = random.choice(list(questions.keys()), 10)

#print (questions[question])
#

# while x <= 10:
#     question_list.append(random.randint(1,20,10))



def play():
    #question = questions[random.randint(1,20)]
    #print(question)
    

    question_list = random.sample(range(1,len(questions)), 10)
    print(question_list)
    score = 0
    question_number = 1
    for x in question_list:
        answer_list = random.sample(range(0,4), 4)
        user_answer = input(f"Question {question_number}:\n{questions[x]}\nA){answers[x][answer_list[0]]} \nB){answers[x][answer_list[1]]} \nC){answers[x][answer_list[2]]} \nD){answers[x][answer_list[3]]}\n")
        match user_answer:
            case 'a' | 'A':
                if answers[x][answer_list[0]] == answers[x][0]:
                    print("That is correct!")
                    score += 1
                else:
                    print(f"Sorry, {answers[x][answer_list[0]]} is not the correct answer!")
            case 'b' | 'B':
                if answers[x][answer_list[1]] == answers[x][0]:
                    print("That is correct!")
                    score += 1
                else:
                    print(f"Sorry, {answers[x][answer_list[1]]} is not the correct answer!")
            case 'c' | 'C':
                if answers[x][answer_list[2]] == answers[x][0]:
                    print("That is correct!")
                    score += 1
                else:
                    print(f"Sorry, {answers[x][answer_list[2]]} is not the correct answer!")
            case 'd' | 'D':
                if answers[x][answer_list[3]] == answers[x][0]:
                    print("That is correct!")
                    score += 1
                else:
                    print(f"Sorry, {answers[x][answer_list[3]]} is not the correct answer!")
            case _:
                print("please only type valid answers e.g a,b,c,d,A,B,C,D")
        print(f"***Score: {score}***")
        question_number += 1

def save():
    #savejson = json.dumps(expenses) 

    with open("questions.json", "w") as fp:
        json.dump(questions, fp)

    with open("answers.json", "w") as fp:
        json.dump(answers, fp)


    print("File successfully saved")

def load():
    f = open("questions.json")
    load_file = json.load(f)
    print(f"file:\n{load_file}")
    clear()
    questions.update(load_file)

    f = open("answers.json")
    load_file = json.load(f)
    print(f"file:\n{load_file}")
    clear()
    answers.update(load_file)
    print("File successfully loaded")
    
def clear():
    questions.clear()
    answers.clear()
    
    print("Your list has been cleared!")

while True:

    command = input("How can we help you today? type 'play' to start the quiz or 'exit' to quit\n")
    match command:

        case 'help':
            print("You can type: \nhelp - To show the help menu.")
            print("clear - To clear your expense list")
            print("exit - To exit the expense program")
            
        case 'save':
            save()
        case 'play':
            play()
        case 'exit':
            break
        case _:
            print("Sorry, that is not a recognised command, type 'help' to see a list of available commands\n")
            


#welcome message

#display question

#allow user to select answer

#calculate score, and keep track for the user

#display results, show score and message based on their performance

#data validation, make sure the user gives proper inputs

#thank user for using the application
