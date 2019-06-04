import csv
import string

with open('../raw/multi.txt', 'r', errors='ignore') as file:
	data = file.readlines()

with open('../input/multi.csv', mode='w') as csv_file:
	writer = csv.DictWriter(csv_file, fieldnames=['utterance', 'slots'])
	writer.writeheader()

	words = []
	for i in range(len(data)):
		if i % 2 == 0: #sentence
			new_words = data[i].split(' ')[:-1]
			for word in new_words:
				words.append(word.lower().translate(str.maketrans('', '', string.punctuation)))
		else: #tag
			tags = data[i][:-2].lower().split(' ')
			writer.writerow({'utterance': ' '.join(words), 'slots': ' '.join(tags)})
			words = []
