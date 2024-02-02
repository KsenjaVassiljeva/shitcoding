import html
import json
import random

with open('quastion.json') as f:
    data = json.load(f)

questions = data['results']
amount = len(questions)
correct_answers = 0

for n, question in enumerate(questions, 1):
    print(f"{n}/{amount}: {html.unescape(question['question'])}")

    answers = []
    answers.append(html.unescape(question['correct_answer']))
    
    for a in question['incorrect_answers']:
        answers.append(html.unescape(a))

    random.shuffle(answers)
    
    print('Answers:\n\t', '\n\t'.join(answers), sep='')
    user_answer = input('Your answer: ')

    if user_answer.lower() == html.unescape(question['correct_answer']).lower():
        print("Correct!\n")
        correct_answers += 1
    else:
        print(f"Wrong! The correct answer is: {html.unescape(question['correct_answer'])}\n")
        
print(f"You got {correct_answers} out of {amount} questions correct.")    