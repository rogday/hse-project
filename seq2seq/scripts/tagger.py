from ludwig.api import LudwigModel
import string

class Tagger:
  def __init__(self):
    self.model = LudwigModel.load('../../tags/tagger')

  def get_tags(self, sentence):
    sentence = sentence.strip().lower().translate(str.maketrans('', '', string.punctuation))
    return self.model.predict(data_dict={'utterance': [sentence]})['slots_predictions'].values[0]

  def __del__(self):
  	self.model.close()