questions = [
    ["Which of these is not a fruit", "Apple", "Mango", "Carrot", "Banana", 3],
    ["How many hours are there in a day", "12", "24", "48", "60", 2],
    ["What is the national animal of India", "Lion", "Tiger", "Elephant", "Leopard", 2],
    ["What is the capital of India?", "Mumbai", "Delhi", "Kolkata", "Chennai", 2],
    ["Which planet is called the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", 3],
    ["Who wrote the Indian national anthem?", "Bankim Chandra", "Gandhi", "Tagore", "Bose", 3],
    ["Which gas do plants use for photosynthesis?", "Oxygen", "Carbon Dioxide", "Hydrogen", "Nitrogen", 2],
    ["What is the boiling point of water?", "50°C", "90°C", "100°C", "150°C", 3],
    ["Which animal is known as the Ship of the Desert?", "Horse", "Donkey", "Camel", "Elephant", 3],
    ["Which is the largest planet in our solar system?", "Earth", "Mars", "Saturn", "Jupiter", 4],
    ["What is the full form of CPU?", "Central Print Unit", "Central Process Unit", "Central Processing Unit", "Computer Personal Unit", 3],
    ["Which country is known as the Land of the Rising Sun?", "China", "India", "Japan", "Thailand", 3],
    ["Who was the first Prime Minister of India?", "Rajendra Prasad", "Gandhi", "Nehru", "Patel", 3],
    ["Which organ purifies our blood?", "Lungs", "Heart", "Kidney", "Liver", 3],
    ["Which is the smallest bone in the human body?", "Femur", "Stapes", "Ulna", "Tibia", 2]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]
print("WELCOME TO KBC")
for i in range(len(questions)):
    q=questions[i]
    print(f"Question for {levels[i]} rs on your tv screen\n")
    print(f"{q[0]}\nOPTIONS\n")
    print(f"1-{q[1]}        2-{q[2]}\n3-{q[3]}        4-{q[4]}\n")
    ans=int(input ("Enter your option : "))
    if ans==q[-1]:
        print("correct")
        print(f"You won {levels[i]}rs\n")
        if i==4:
            money=10000
        elif i==9:
            money=320000
        elif i==14:
            money=7000000
    else:
        print("Wrong answer")
        break
print("Money taking home=",money)