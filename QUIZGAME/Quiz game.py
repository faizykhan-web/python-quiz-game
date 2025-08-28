questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) London", "B) Berlin", "C) Paris", "D) Rome"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
        "answer": "B"
    },
    {
        "question": "What is 5 + 7?",
        "options": ["A) 10", "B) 11", "C) 12", "D) 13"],
        "answer": "C"
    }
]

score = 0

for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)
    answer = input("Your answer (A, B, C, or D): ").upper()
    
    if answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print(f"\nYou got {score} out of {len(questions)} correct!")
