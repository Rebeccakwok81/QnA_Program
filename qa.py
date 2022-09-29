from question import Question

test = [
    "1 + 1 = ?\n(a) 0\n(b) 1 \n(c) 2\n",
    "1 km equals how many miles?\n(a) 0.621371\n(b) 0.621373\n(c) 0.621377\n",
    "What is my fav colour\n(a) white\n(b) blue\n(c) all\n"
]

questions = [
    Question(test[0],"c"),
    Question(test[1],"a"),
    Question(test[2],"c")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.description)
        if answer == question.answer:
            score += 1

    print(f"You got {score} score(s) in {len(questions)} questions!")

run_test(questions)