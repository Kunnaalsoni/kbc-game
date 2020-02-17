# Stores the amount in te variable
money = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000,
         10000000]
stage = 0

# function to print the money
def win_money(correct_answer):
    print(money[correct_answer - 1])
    if money[correct_answer - 1] == 10000:
        print("Congrats!Aapka Padaav pura ho gaya hai.")
    elif money[correct_answer - 1] == 320000:
        print("Congrats! Aapka dusra Padaav pura ho gaya hai.")
    elif money[correct_answer - 1] == 10000000:
        print("Congrats! Aap ek crore rupaye jeet gaye hai.")


def start():
    global stage
    # Question list for kbc
    question = [
        "Which of these Hindi phrases is used to denote high inflation?",
        "Complete the title of this film starring Anil Kapoor and Kajol, 'Hum Aapke _____ Mein Rehte Hain'",
        "Which one of these four birds has the longest beak and feet?",
        "Which of these formulae is used to calculate the area of a rectangular agriculture field?",
        "Which one of these festivals is celebrated during winter in India?",
        "which of these Hindi idioms means to defame someone ?",
        "The traditional attire 'pheta' is worn on which part of the body ?",
        "Which of the following was once a lifeline on the TV show 'Kaun Banega Crorepati'?",
        "what time corresponds to 23:23 hours ?",
        "The south-eastern coast of India is popularly called what ?",
        "Which of these chief ministers has the middle name of Gangadharrao ?",
        "Which of these diseases is caused by bacteria, not viruses ?"
        "Which of these is produced in plants of Narora, Lakrapar and Tarapur ?",
        "Which of these naval exercises is conducted jointly by India and Singapore?",
        "Who did Dennis Lillee once reject as a fast bowler, and about whom he later jokingly said, 'I think I did him and game of cricket a favour' ?",
        "How much money you want?"

    ]
    # Option for the game
    first_option = [
        "Fasal Bikau Mehngaai", "Gali",
        "Heron", "breadth-length",
        "Baisakhi", "Keechad Uchaalna",
        "Arm", "Tridev", "Lawn Tennis",
        "11:23PM", "Muqaddar Ka Sikandar",
        "Konkan", "Manohar Parrikar",
        "Typhoid", "Atomic Power", "Varuna",
        "Irfan Pathan",
        "10"

    ]
    second_option = [
        "Padgi Chor Mehngaai", "Dil",
        "Parrot", "length * breadth * height",
        "Makar Sankanti", "Paani Daalna",
        "Head", "Triguni", "Badminton",
        "11.11PM", "O Saathi Re", "Malabar",
        "Siddaramaiah", "Dengue", "EVMs",
        "Malabar", "Sourav Ganguly","20"

    ]
    third_option = [
        "Aankhfod Mehngaai", "Kholi",
        "Crow", "length * breadth",
        "Naag Panchami", "Mitti Khodna",
        "Waist", "Trimurti", "Table Tennis",
        "7:23PM", "Dekha Ek Khwab", "Porbandar",
        "Vijay Rupani", "Chikungunya", "Coins",
        "Simbex", "Sahin Tendulakar","30"
    ]
    fourth_option = [
        "Kamartod Mehngai", "Baju",
        "Pigeon", "breadth/length",
        "Ganesh Chaturthi", "Rang Lagaana",
                            "Chest", "Trilok", "Squash",
        "9.11PM", "Amar Akbar Anthony",
        "Coromandel", "Devendra Fadnavis",
        "Mumps", "Slinex","Chain coaches"
        "Brett Lee","40"
    ]
    # All option are kept in it for easy use
    all_option = [
        first_option, second_option,
        third_option, fourth_option
    ]
    # For iterating till user doesn't gives wrong answer
    wrong_answer = False
    # For counting at which level the user is
    correct_answer = 0
    # List for keeping record of all answer in sequence wise
    ans_key = [3, 1, 0, 2, 1, 0, 1, 1, 2, 1, 3, 3, 0, 0, 2, 2, 1]

    # Games  begins from here
    while (wrong_answer != True):
        # variable used to pick the questions from the list
        

        # prints the question from the list
        print("\n----*----*----*----*----*----*----*----*----*\n")
        print("Q." + question[stage])

        # prints the option
        for Number, option in enumerate(all_option):
            print(str(Number + 1) + ". " + option[stage])
        # Takes the input of the user
        answer = input("Apna answer dijye: ")
        try:
            answer = int(answer,10)
        except ValueError:
            print("Invalid choice selected, enter a integer")
            start()
            

        key = (ans_key[stage] + 1)
        # checks if the answer is correct or not
        if key == answer:
            print("Congrats! Aapka answer sahi hai aap jeete hai : Rs", end="")
            correct_answer += 1
            win_money(correct_answer)
        else:
            print("Sadly aapka javab galat hai")
            correct_answer = 0
            wrong_answer = True
        # checks if it is the last level or not
        if correct_answer < 15:
            stage += 1
        else:
            break
        #print(correct_answer)
start()
