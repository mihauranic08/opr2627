import requests
import pprint
import random

questions = []
answers = [[], [], [], [], [],
           [], [], [], [], []]
answersI = ""

urlTrivia = "https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=multiple"

data = requests.get(urlTrivia).json()
results = data["results"]

for i, q in enumerate(results):
    answersI = q["incorrect_answers"]
    for iA in answersI:
        answers[i].append(iA)
    answers[i].append(q["correct_answer"])

pprint.pprint(results)
pprint.pprint(answers)

for group in answers:
    print()
    for i in range(4): #for answwers per set
        print(group.pop(random.randint(0, 3-i)))