from tagger import Tagger
import csv
import string

with open('../raw/train_dialogues.txt', 'r', errors='ignore') as file:
	data = file.readlines()

tagger = Tagger()

with open('../input/dialogues.csv', mode='w') as csv_file:
	writer = csv.DictWriter(csv_file, fieldnames=['question', 'answer'])
	writer.writeheader()

	def replace(array, shift, tag, i, k):
		print(array, shift, tag ,i, k)
		for j in range(i - shift + 1, k - shift):
			array.pop(i - shift)
		array[i - shift] = '_' + tag + '_'
		return shift + (k - i) - 1

	for k in range(len(data)):
		sentence = data[k].lower().translate(str.maketrans('', '', string.punctuation))[:-1]
		tags = tagger.get_tags(sentence)
		tags.append('o')

		words = sentence.split(' ')
		words.append('lul')

		lastTag = ''
		index = -1
		shift = 0
		for i in range(len(tags)):
			if tags[i][0] == 'o':
				if lastTag != '':
					shift = replace(words, shift, lastTag, index, i)
				lastTag = ''
			elif tags[i][0] == 'b':
				if lastTag != '':
					shift = replace(words, shift, lastTag, index, i)
				lastTag = tags[i][2:]
				index = i
			elif tags[i][0] == 'i' and lastTag != tags[i][2:]: #model can fuck up
				if lastTag != '': 
					shift = replace(words, shift, lastTag, index, i)
				lastTag = tags[i][2:]
				index = i

		if k % 2 == 0:
			question = ' '.join(words[:-1])
		else:
			answer = ' '.join(words[:-1])
			#print(question, answer, sep = '\n', end = '\n\n')
			writer.writerow({'question': question,  'answer': answer})