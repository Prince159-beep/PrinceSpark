import sqlite3

# connect to quiz.db
conn = sqlite3.connect("quiz.db")
c = conn.cursor()

# create users table
c.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")

# create questions table
c.execute("""
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    option1 TEXT NOT NULL,
    option2 TEXT NOT NULL,
    option3 TEXT NOT NULL,
    option4 TEXT NOT NULL,
    answer INTEGER NOT NULL,
    difficulty TEXT NOT NULL
)
""")

# create scores table
c.execute("""
CREATE TABLE IF NOT EXISTS scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    score INTEGER NOT NULL,
    difficulty TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

# ---------------- EASY QUESTIONS ----------------
easy_questions = [
    ("What is 2 + 2?", "3", "4", "5", "6", 2, "easy"),
    ("What color is the sky?", "Blue", "Green", "Red", "Yellow", 1, "easy"),
    ("How many days in a week?", "5", "6", "7", "8", 3, "easy"),
    ("Which planet do we live on?", "Mars", "Earth", "Venus", "Jupiter", 2, "easy"),
    ("What is 10 - 4?", "4", "5", "6", "7", 3, "easy"),
    ("What is the first letter of English alphabet?", "Z", "B", "A", "C", 3, "easy"),
    ("Which animal says 'meow'?", "Dog", "Cat", "Cow", "Goat", 2, "easy"),
    ("What is 3 × 3?", "6", "9", "12", "8", 2, "easy"),
    ("How many colors in a rainbow?", "5", "6", "7", "8", 3, "easy"),
    ("What is the capital of India?", "Delhi", "Mumbai", "Kolkata", "Chennai", 1, "easy"),
    ("Which gas do humans breathe?", "Oxygen", "Carbon Dioxide", "Nitrogen", "Helium", 1, "easy"),
    ("What is 5 + 7?", "10", "11", "12", "13", 3, "easy"),
    ("Which is the smallest month?", "February", "January", "June", "April", 1, "easy"),
    ("What shape has 4 equal sides?", "Circle", "Triangle", "Square", "Rectangle", 3, "easy"),
    ("Which fruit is yellow?", "Apple", "Banana", "Orange", "Grapes", 2, "easy"),
    ("What is 100 ÷ 10?", "5", "10", "20", "50", 2, "easy"),
    ("Which is faster?", "Snail", "Dog", "Turtle", "Cat", 2, "easy"),
    ("What is opposite of hot?", "Cold", "Warm", "Cool", "Freeze", 1, "easy"),
    ("What do bees make?", "Honey", "Milk", "Juice", "Oil", 1, "easy"),
    ("Which shape is round?", "Square", "Circle", "Triangle", "Rectangle", 2, "easy"),
    ("What is 8 + 1?", "9", "10", "11", "8", 1, "easy"),
    ("Which animal is called the king of jungle?", "Tiger", "Lion", "Elephant", "Bear", 2, "easy"),
    ("What is the color of leaves?", "Red", "Blue", "Green", "Black", 3, "easy"),
    ("What comes after 99?", "100", "101", "98", "110", 1, "easy"),
    ("How many legs does a spider have?", "6", "8", "10", "12", 2, "easy"),
    ("Which organ pumps blood?", "Brain", "Heart", "Lungs", "Liver", 2, "easy"),
    ("What is 6 × 2?", "8", "10", "12", "14", 3, "easy"),
    ("Which star appears in the day?", "Moon", "Mars", "Sun", "Venus", 3, "easy"),
    ("How many wheels in a car?", "2", "3", "4", "5", 3, "easy"),
    ("Which is used to cut paper?", "Pen", "Scissors", "Eraser", "Book", 2, "easy")
]

# ---------------- MEDIUM QUESTIONS ----------------
medium_questions = [
    ("Who invented the light bulb?", "Einstein", "Newton", "Edison", "Tesla", 3, "medium"),
    ("What is the square root of 81?", "9", "8", "7", "6", 1, "medium"),
    ("Which country is called the Land of Rising Sun?", "China", "Japan", "Korea", "Thailand", 2, "medium"),
    ("What is 12 × 12?", "124", "144", "122", "132", 2, "medium"),
    ("Which gas do plants release?", "Oxygen", "Carbon dioxide", "Nitrogen", "Helium", 1, "medium"),
    ("What is H2O?", "Water", "Oxygen", "Hydrogen", "Salt", 1, "medium"),
    ("Who is the father of computers?", "Bill Gates", "Charles Babbage", "Steve Jobs", "Turing", 2, "medium"),
    ("What is the largest mammal?", "Elephant", "Blue Whale", "Shark", "Giraffe", 2, "medium"),
    ("How many continents are there?", "6", "7", "8", "5", 2, "medium"),
    ("What is the capital of France?", "Rome", "Berlin", "Paris", "London", 3, "medium"),
    ("Who wrote Ramayana?", "Valmiki", "Tulsidas", "Kalidas", "Ved Vyas", 1, "medium"),
    ("Which planet is closest to the sun?", "Earth", "Mercury", "Venus", "Mars", 2, "medium"),
    ("Which blood group is universal donor?", "A", "B", "AB", "O-", 4, "medium"),
    ("What is 15 × 5?", "60", "70", "75", "80", 3, "medium"),
    ("What is the largest river in the world?", "Nile", "Amazon", "Ganga", "Mississippi", 2, "medium"),
    ("What is 2³?", "6", "8", "9", "12", 2, "medium"),
    ("Which language is most spoken?", "English", "Spanish", "Hindi", "Mandarin Chinese", 4, "medium"),
    ("Who painted Mona Lisa?", "Michelangelo", "Da Vinci", "Van Gogh", "Picasso", 2, "medium"),
    ("What is the freezing point of water?", "0°C", "10°C", "4°C", "32°C", 1, "medium"),
    ("What is 50% of 200?", "50", "75", "100", "120", 3, "medium"),
    ("Which is the national flower of India?", "Lotus", "Rose", "Sunflower", "Tulip", 1, "medium"),
    ("What is the fastest land animal?", "Horse", "Cheetah", "Tiger", "Lion", 2, "medium"),
    ("Who discovered gravity?", "Newton", "Einstein", "Edison", "Rutherford", 1, "medium"),
    ("What is the capital of USA?", "New York", "Washington DC", "California", "Chicago", 2, "medium"),
    ("Which element has symbol Fe?", "Lead", "Iron", "Zinc", "Gold", 2, "medium"),
    ("What is 18 ÷ 3?", "6", "5", "7", "8", 1, "medium"),
    ("Who discovered India by sea?", "Columbus", "Vasco da Gama", "Magellan", "Cook", 2, "medium"),
    ("What is 9 × 9?", "99", "81", "72", "79", 2, "medium"),
    ("Which is the largest desert?", "Sahara", "Thar", "Arabian", "Gobi", 1, "medium"),
    ("Which vitamin do we get from sunlight?", "A", "B", "C", "D", 4, "medium")
]

# ---------------- HARD QUESTIONS ----------------
hard_questions = [
    ("Who proposed the theory of relativity?", "Newton", "Einstein", "Tesla", "Planck", 2, "hard"),
    ("What is 12³?", "1728", "1440", "1212", "1128", 1, "hard"),
    ("Which element has symbol Au?", "Silver", "Gold", "Platinum", "Copper", 2, "hard"),
    ("What is the capital of Australia?", "Sydney", "Melbourne", "Canberra", "Perth", 3, "hard"),
    ("Who discovered penicillin?", "Alexander Fleming", "Newton", "Curie", "Pasteur", 1, "hard"),
    ("What is the speed of light?", "3×10⁵ m/s", "3×10⁸ m/s", "3×10⁶ m/s", "3×10⁹ m/s", 2, "hard"),
    ("Which is the heaviest naturally occurring element?", "Uranium", "Osmium", "Plutonium", "Lead", 1, "hard"),
    ("Who discovered electricity?", "Faraday", "Edison", "Franklin", "Tesla", 3, "hard"),
    ("What is the boiling point of water in Kelvin?", "100K", "273K", "373K", "400K", 3, "hard"),
    ("Which gas protects us from UV rays?", "Oxygen", "Nitrogen", "Ozone", "Carbon dioxide", 3, "hard"),
    ("Which organelle is the powerhouse of cell?", "Nucleus", "Mitochondria", "Ribosome", "Chloroplast", 2, "hard"),
    ("Who invented the World Wide Web?", "Tim Berners-Lee", "Gates", "Jobs", "Turing", 1, "hard"),
    ("What is Planck’s constant (approx)?", "6.63×10⁻³⁴ Js", "6.63×10⁻²⁰ Js", "9.81 Js", "3.14 Js", 1, "hard"),
    ("Which planet has the most moons?", "Jupiter", "Saturn", "Mars", "Neptune", 2, "hard"),
    ("Which is the deepest ocean?", "Atlantic", "Indian", "Pacific", "Arctic", 3, "hard"),
    ("What is 256 ÷ 16?", "14", "18", "16", "12", 3, "hard"),
    ("Which part of brain controls balance?", "Cerebellum", "Cerebrum", "Medulla", "Spinal cord", 1, "hard"),
    ("Which law explains action & reaction?", "Newton’s 1st", "Newton’s 2nd", "Newton’s 3rd", "Kepler’s law", 3, "hard"),
    ("Who discovered radioactivity?", "Einstein", "Rutherford", "Curie", "Bohr", 3, "hard"),
    ("Which country hosted the first Olympics?", "India", "Greece", "Rome", "France", 2, "hard"),
    ("What is the SI unit of Force?", "Newton", "Pascal", "Joule", "Watt", 1, "hard"),
    ("What is the chemical name of table salt?", "NaCl", "KCl", "CaCl2", "HCl", 1, "hard"),
    ("What is 22/7 called?", "π (Pi)", "e", "Log", "Infinity", 1, "hard"),
    ("Which organ filters blood?", "Heart", "Liver", "Kidney", "Lungs", 3, "hard"),
    ("What is the national currency of Japan?", "Dollar", "Won", "Yen", "Rupee", 3, "hard"),
    ("Which scientist worked on evolution?", "Newton", "Darwin", "Bohr", "Copernicus", 2, "hard"),
    ("What is DNA full form?", "Data Network Array", "Deoxyribonucleic Acid", "Dynamic Neural Architecture", "None", 2, "hard"),
    ("Who gave the law of planetary motion?", "Einstein", "Newton", "Kepler", "Bohr", 3, "hard"),
    ("What is the largest bone in human body?", "Femur", "Tibia", "Spine", "Skull", 1, "hard"),
    ("Which programming language is oldest?", "Python", "Java", "Fortran", "C", 3, "hard")
]

# insert all questions
c.executemany("INSERT INTO questions (question, option1, option2, option3, option4, answer, difficulty) VALUES (?, ?, ?, ?, ?, ?, ?)", easy_questions)
c.executemany("INSERT INTO questions (question, option1, option2, option3, option4, answer, difficulty) VALUES (?, ?, ?, ?, ?, ?, ?)", medium_questions)
c.executemany("INSERT INTO questions (question, option1, option2, option3, option4, answer, difficulty) VALUES (?, ?, ?, ?, ?, ?, ?)", hard_questions)

conn.commit()
conn.close()

print("✅ 30 Questions each for Easy, Medium & Hard added successfully!")
