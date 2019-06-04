from ludwig.api import LudwigModel
import string

def get_tags(sentence):
	tagger = LudwigModel.load('../tagger')

	sentence = sentence.strip().lower().translate(str.maketrans('', '', string.punctuation))
	ret = tagger.predict(data_dict={'utterance': [sentence]})['slots_predictions'].values

	tagger.close()

	return ret