# random jokes generator application

import random

jokes = ["Why do pyython programmers prefer dark mode? Because light attracts bugs!",
         "Why do programmers prefer iOS development? Because they can't handle Android's Java!", 
         "Why did the programmer quit his job? Because he didn't get arrays!",
         "Why do Java developers wear glasses? Because they don't see sharp!",
         "why did the scarecrow win an award? Because he was outstanding in his field!"
         "Why don't avengers use the hulk to advertise? Because he always smashes the competition!"
         "Why do you call fake spaghetti? An impasta!",
         "Why don't skeleton s fight each other? They don't have the guts!",
         "Why did the computer go to therapy? It had too many bytes!",
         "Why was the math book sad? Because it had too many problems!",
         "Why don't oysters donate to charity? Because they are shellfish!",
]

print("Welcome to python joke Generator! press Enter to hear a joke. Type 'q' to quit.\n" )

while True:
    user_input = input("press Enter for a joke or 'q' to quit:")
    if user_input.lower() == 'q':
        print("Thanks for using the joke generator! Goodbye!")
        break
    else:
        joke = random.choice(jokes)
        print(f"Here's a joke for you: {joke}\n")