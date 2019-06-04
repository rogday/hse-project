import csv
import string

with open('../raw/train_dialogues.txt', 'r', errors='ignore') as file:
	data = file.readlines()

with open('../input/dialogues.csv', mode='w') as csv_file:
	writer = csv.DictWriter(csv_file, fieldnames=['question', 'answer'])
	writer.writeheader()

	for k in range(len(data)):
		sentence = data[k].lower().translate(str.maketrans('', '', string.punctuation))[:-1]

		if k % 2 == 0:
			question = sentence
		else:
			answer = sentence
			#print(question, answer, sep = '\n', end = '\n\n')
			writer.writerow({'question': question,  'answer': answer})