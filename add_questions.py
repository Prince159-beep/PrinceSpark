
import sqlite3

conn = sqlite3.connect("princespark.db")
c = conn.cursor()

questions = [
    # ---------------- EASY (30) ----------------
    ("2 + 2 = ?", "3", "4", "5", "6", "option2", "easy"),
    ("5 + 7 = ?", "11", "12", "13", "14", "option2", "easy"),
    ("Sun rises in the?", "North", "South", "East", "West", "option3", "easy"),
    ("Which is an animal?", "Apple", "Dog", "Car", "Chair", "option2", "easy"),
    ("How many days in a week?", "5", "6", "7", "8", "option3", "easy"),
    ("What is 10 - 3?", "6", "7", "8", "9", "option2", "easy"),
    ("Which is a fruit?", "Potato", "Tomato", "Banana", "Onion", "option3", "easy"),
    ("What is 3 × 3?", "6", "7", "8", "9", "option4", "easy"),
    ("What is the capital of India?", "Delhi", "Mumbai", "Kolkata", "Chennai", "option1", "easy"),
    ("Color of the sky?", "Blue", "Green", "Red", "Yellow", "option1", "easy"),
    ("Which is a vegetable?", "Banana", "Potato", "Mango", "Apple", "option2", "easy"),
    ("Which is used to write with?", "Book", "Pen", "Chair", "Table", "option2", "easy"),
    ("Which season is cold?", "Summer", "Winter", "Rainy", "Spring", "option2", "easy"),
    ("What comes after 9?", "8", "10", "11", "12", "option2", "easy"),
    ("Which shape has 3 sides?", "Square", "Triangle", "Circle", "Rectangle", "option2", "easy"),
    ("Which is a domestic animal?", "Lion", "Tiger", "Cow", "Wolf", "option3", "easy"),
    ("How many letters in English alphabet?", "24", "25", "26", "27", "option3", "easy"),
    ("Which day comes after Monday?", "Tuesday", "Wednesday", "Friday", "Sunday", "option1", "easy"),
    ("Which is the fastest animal?", "Cheetah", "Dog", "Elephant", "Horse", "option1", "easy"),
    ("What is 7 × 5?", "30", "35", "40", "45", "option2", "easy"),
    ("Which organ pumps blood?", "Liver", "Heart", "Lungs", "Kidney", "option2", "easy"),
    ("Which is the national flower of India?", "Rose", "Lily", "Lotus", "Sunflower", "option3", "easy"),
    ("What is H2O?", "Oxygen", "Water", "Carbon", "Hydrogen", "option2", "easy"),
    ("What planet do we live on?", "Mars", "Earth", "Venus", "Jupiter", "option2", "easy"),
    ("What is 12 ÷ 3?", "3", "4", "5", "6", "option2", "easy"),
    ("Which is used to see?", "Nose", "Ear", "Eye", "Hand", "option3", "easy"),
    ("How many days in a leap year?", "365", "366", "364", "367", "option2", "easy"),
    ("Which is a primary color?", "Pink", "Red", "Brown", "Black", "option2", "easy"),
    ("What is opposite of Hot?", "Cold", "Warm", "Cool", "Dark", "option1", "easy"),
    ("Which is used to eat food?", "Pen", "Book", "Spoon", "Chair", "option3", "easy"),

    # ---------------- MEDIUM (30) ----------------
    ("Square root of 81?", "7", "8", "9", "10", "option3", "medium"),
    ("Who invented Python?", "Dennis Ritchie", "James Gosling", "Guido van Rossum", "Linus Torvalds", "option3", "medium"),
    ("Largest planet?", "Earth", "Mars", "Jupiter", "Saturn", "option3", "medium"),
    ("What is 15 × 4?", "60", "55", "45", "50", "option1", "medium"),
    ("Chemical symbol of Water?", "O2", "H2O", "CO2", "NaCl", "option2", "medium"),
    ("Who wrote Ramayana?", "Valmiki", "Tulsidas", "Kalidas", "Ved Vyas", "option1", "medium"),
    ("Formula of Speed?", "d/t", "t/d", "d×t", "d+t", "option1", "medium"),
    ("Prime Minister of India (2025)?", "Narendra Modi", "Rahul Gandhi", "Manmohan Singh", "Amit Shah", "option1", "medium"),
    ("First man on the moon?", "Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin", "Kalpana Chawla", "option1", "medium"),
    ("Area of square?", "l×b", "πr²", "a²", "2πr", "option3", "medium"),
    ("Which gas do humans breathe?", "O2", "CO2", "N2", "H2", "option1", "medium"),
    ("Who is known as Father of Computer?", "Charles Babbage", "Alan Turing", "Bill Gates", "Steve Jobs", "option1", "medium"),
    ("How many continents?", "5", "6", "7", "8", "option3", "medium"),
    ("Which planet is called Red Planet?", "Earth", "Mars", "Jupiter", "Venus", "option2", "medium"),
    ("Currency of USA?", "Euro", "Dollar", "Pound", "Yen", "option2", "medium"),
    ("Fastest bird?", "Sparrow", "Eagle", "Peregrine Falcon", "Crow", "option3", "medium"),
    ("Which country hosted Olympics 2021?", "China", "Japan", "USA", "Brazil", "option2", "medium"),
    ("Who painted Mona Lisa?", "Picasso", "Leonardo da Vinci", "Van Gogh", "Michelangelo", "option2", "medium"),
    ("Which is the longest river?", "Ganga", "Amazon", "Nile", "Yangtze", "option3", "medium"),
    ("What is the capital of France?", "Rome", "London", "Berlin", "Paris", "option4", "medium"),
    ("Atomic number of Oxygen?", "6", "7", "8", "9", "option3", "medium"),
    ("How many states in India?", "27", "28", "29", "30", "option2", "medium"),
    ("Who discovered Gravity?", "Newton", "Einstein", "Kepler", "Darwin", "option1", "medium"),
    ("Fastest train in India?", "Rajdhani", "Vande Bharat", "Duronto", "Shatabdi", "option2", "medium"),
    ("Who was first President of India?", "Rajendra Prasad", "Nehru", "Patel", "Kalam", "option1", "medium"),
    ("Which is smallest continent?", "Asia", "Europe", "Australia", "Africa", "option3", "medium"),
    ("Symbol of Gold?", "Ag", "Au", "Gd", "Pt", "option2", "medium"),
    ("Brain of computer?", "CPU", "RAM", "Monitor", "Keyboard", "option1", "medium"),
    ("Taj Mahal built by?", "Akbar", "Shah Jahan", "Aurangzeb", "Babur", "option2", "medium"),
    ("Largest mammal?", "Elephant", "Blue Whale", "Shark", "Giraffe", "option2", "medium"),

    # ---------------- HARD (30) ----------------
    ("Who discovered penicillin?", "Newton", "Darwin", "Fleming", "Einstein", "option3", "hard"),
    ("Year WW2 ended?", "1943", "1944", "1945", "1946", "option3", "hard"),
    ("Value of π approx?", "3.12", "3.14", "3.15", "3.16", "option2", "hard"),
    ("Who invented C language?", "Guido", "Dennis Ritchie", "James Gosling", "Ken Thompson", "option2", "hard"),
    ("Which gas forms ozone?", "O2", "O3", "CO2", "H2", "option2", "hard"),
    ("Einstein’s famous equation?", "E=mc²", "F=ma", "V=IR", "PV=nRT", "option1", "hard"),
    ("First Indian in space?", "Rakesh Sharma", "Kalpana Chawla", "Sunita Williams", "Vikram Sarabhai", "option1", "hard"),
    ("Capital of Japan?", "Seoul", "Beijing", "Tokyo", "Osaka", "option3", "hard"),
    ("Father of Computer?", "Charles Babbage", "Alan Turing", "Bill Gates", "Steve Jobs", "option1", "hard"),
    ("HCF of 36 and 60?", "6", "12", "18", "24", "option2", "hard"),
    ("Atomic number of Carbon?", "4", "5", "6", "7", "option3", "hard"),
    ("Who proposed theory of relativity?", "Newton", "Einstein", "Tesla", "Bohr", "option2", "hard"),
    ("Smallest prime number?", "0", "1", "2", "3", "option3", "hard"),
    ("First Indian woman in space?", "Kalpana Chawla", "Sunita Williams", "Indira Gandhi", "None", "option1", "hard"),
    ("Who wrote Constitution of India?", "Gandhi", "Ambedkar", "Nehru", "Patel", "option2", "hard"),
    ("What is speed of light?", "2×10^8", "3×10^8", "1.5×10^8", "2.5×10^8", "option2", "hard"),
    ("Who discovered electricity?", "Edison", "Tesla", "Franklin", "Newton", "option3", "hard"),
    ("Binary of 10?", "1010", "1100", "1001", "1110", "option1", "hard"),
    ("Blood group called universal donor?", "A", "B", "AB", "O", "option4", "hard"),
    ("National income measured by?", "GDP", "GNP", "NDP", "CPI", "option1", "hard"),
    ("Where is Eiffel Tower?", "Rome", "London", "Paris", "Berlin", "option3", "hard"),
    ("Inventor of telephone?", "Edison", "Alexander Graham Bell", "Tesla", "Marconi", "option2", "hard"),
    ("Water boils at?", "90°C", "100°C", "120°C", "80°C", "option2", "hard"),
    ("Largest desert?", "Sahara", "Thar", "Gobi", "Arctic", "option1", "hard"),
    ("First computer programmer?", "Ada Lovelace", "Charles Babbage", "Alan Turing", "Grace Hopper", "option1", "hard"),
    ("Formula of Force?", "F=ma", "E=mc²", "V=IR", "P=VI", "option1", "hard"),
    ("Nobel Prize for Physics 1921?", "Planck", "Bohr", "Einstein", "Curie", "option3", "hard"),
    ("What is Newton’s 3rd law?", "F=ma", "Action=Reaction", "Energy=Mass", "PV=nRT", "option2", "hard"),
    ("Who invented WWW?", "Tim Berners-Lee", "Bill Gates", "Steve Jobs", "Linus Torvalds", "option1", "hard"),
    ("First nuclear bomb used in?", "Japan", "Germany", "Russia", "China", "option1", "hard"),
]

c.executemany(
    "INSERT INTO questions (question, option1, option2, option3, option4, correct_option, difficulty) VALUES (?, ?, ?, ?, ?, ?, ?)",
    questions
)

conn.commit()
conn.close()

print("✅ 90 Questions added successfully!")
