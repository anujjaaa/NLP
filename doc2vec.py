import gensim, logging
from gensim.models import Word2Vec
from nltk import sent_tokenize, word_tokenize, pos_tag

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

documents = ["Human machine interface for lab abc computer applications",
             "A survey of user opinion of computer system response time",
             "The EPS user interface management system",
             "System and human system engineering testing of EPS",
             "Relation of user perceived response time to error measurement",
             "The generation of random binary unordered trees",
             "The intersection graph of paths in trees",
             "Graph minors IV Widths of trees and well quasi ordering",
             "Graph minors A survey"]

from gensim import utils
# from gensim.models.doc2vec import LabeledSentence
# from gensim.models.deprecated.doc2vec import LabeledSentence
from gensim.models.doc2vec import TaggedDocument
from gensim.models import Doc2Vec
import numpy
import numpy as np
from random import shuffle


class LabeledLineSentence(object):
    def __init__(self, sources):
        self.sources = sources

        flipped = {}

        # make sure that keys are unique
        for key, value in sources.items():
            if value not in flipped:
                flipped[value] = [key]
            else:
                raise Exception('Non-unique prefix encountered')

    def __iter__(self):
        for source, prefix in self.sources.items():
            with utils.smart_open(source) as fin:
                for item_no, line in enumerate(fin):
                    # yield LabeledSentence(utils.to_unicode(line).split(), [prefix + '_%s' % item_no])
                    yield TaggedDocument(utils.to_unicode(line).split(), [prefix + '_%s' % item_no])

    def to_array(self):
        self.sentences = []
        for source, prefix in self.sources.items():
            with utils.smart_open(source) as fin:
                for item_no, line in enumerate(fin):
                    self.sentences.append(TaggedDocument(utils.to_unicode(line).split(), [prefix + '_%s' % item_no]))
                    # self.sentences.append(LabeledSentence(utils.to_unicode(line).split(), [prefix + '_%s' % item_no]))
        return self.sentences

    def sentences_perm(self):
        shuffle(self.sentences)
        return self.sentences


docs = np.savetxt('textosDoc2Vec.txt', documents, fmt='%s')
sources = {'textosDoc2Vec.txt': 'TRAIN'}

sentences = LabeledLineSentence(sources)

model = Doc2Vec(min_count=1, window=5, vector_size=10, sample=1e-4, negative=5, workers=8)
model.build_vocab(sentences.to_array())

for epoch in range(10):
    model.train(sentences.sentences_perm(), total_examples=model.corpus_count, epochs=model.iter)

model.save('./Doc2Vec.d2v')

new_model = Doc2Vec.load('./Doc2Vec.d2v')
new_model
new_model.most_similar('computer')

sentences = []
for i in range(0, len(documents)):
    sentences.append(word_tokenize(str(documents[i])))

import numpy as np

len(np.unique(np.concatenate(sentences)))

array = [np.ndarray.flatten(new_model[sentences[i]]) for i in range(0, len(documents))]
array

new_model.most_similar(positive=['Human', 'error'], negative=['trees'], topn=4)

new_model.similarity('computer', 'system')
