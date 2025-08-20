# multiple choice game application

questions = [
    { 
        "question": "1. in python what does 'f' in an f-string stand for?",
        "options": ["a) format", "b) function", "c) file", "d) float", "d) for"],
        "answer": "a"
    },

    {
        "question": "2. In which movie features the quote 'May the Force be with you'?",
        "options": ["a) Star Wars", "b) The Matrix", "c) Inception", "d) Avatar"],
        "answer": "a"  
    },

    {  "question": "3. What is the capital of wakanda in the Marvel Cinematic Universe?",
        "options": ["a) Wakanda City", "b) New York", "c) Atlantis", "d) Asgard"],
        "answer": "a"
    },

    {
        "question": "4. What is the name of the fictional African country in Black Panther?",
        "options": ["a) Zamunda", "b) Wakanda", "c) Genosha", "d) Elbonia"],
        "answer": "b"
    },

    {
        "question": "5. In which movie does the character 'Jack Sparrow' appear?",
        "options": ["a) The Lord of the Rings", "b) Pirates of the Caribbean", "c) Harry Potter", "d) The Dark Knight"],
        "answer": "b"
    },

    {
        "question": "6. In python, what keyword is used to define a function?",
        "options": ["a) def", "b) function", "c) func", "d) define"],
        "answer": "a"
    },

    {
        "question": "7. What is the largest planet in our solar system?",
        "options": ["a) Earth", "b) Mars", "c) Jupiter", "d) Saturn"],  
        "answer": "c"
    }
]

score = 0

print("🎯 welcome to the python & Fun Trivia Quiz!\n")

for q in questions:
    print(q["question"])
    for option in q["options"]:
        print(option)
    
    answer = input("Your answer (a, b, c, or d): ").lower()
    
    if answer == q["answer"]:
        print("Correct! ✅\n")
        score += 1
    else:
        print(f"Wrong! ❌ The correct answer is {q['answer']}.\n")

print(f"🎉 you got {score}/{len(questions)} correct!")