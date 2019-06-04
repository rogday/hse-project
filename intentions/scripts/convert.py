import csv
import string

def preprocess(word):
	return word.lower().translate(str.maketrans('', '', string.punctuation))

with open('../raw/goals.txt', 'r', errors='ignore') as file:
	data = file.readlines()

with open('../input/goals.csv', mode='w') as csv_file:
	writer = csv.DictWriter(csv_file, fieldnames=['utterance', 'intentions'])
	writer.writeheader()

	for i in range(len(data)):
		if i % 2 == 0: #sentence
			words = list(map(preprocess, data[i].split(' ')[:-1]))
			print(words)
		else: #intentions
			intentions = list(map(preprocess, data[i][:-2].lower().split(' ')))
			print(intentions)
			writer.writerow({'utterance': ' '.join(words), 'intentions': ' '.join(intentions)})
