import json

with open('questions.jsonl') as f:
    data = [json.loads(line) for line in f]

print(data)
# this code is used to calculate how often a question is evoked at a place where a discourse relation has been
# instantiated

m = 2391

for dictionary in data:
    for key, value in dictionary.items():
        if value == ['NoRel:nan']:
            m = m - 1

print(m)

# code snippet to calculate number of different 'wh-questions'

wh_dict = {'What': 0, 'Who': 0, 'Where': 0, "When": 0, 'Why': 0}

for dictionary in data:
    question = dictionary['question_text']
    for wh_word in wh_dict.keys():
        if question.startswith(wh_word):
            wh_dict[wh_word] += 1

print(wh_dict)

# how many questions have been answered?

n = 2391

for dictionary in data:
    answer = dictionary['answer_text']
    if answer is None:
        n = n - 1

print(n)


