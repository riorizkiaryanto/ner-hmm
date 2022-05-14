import warnings
warnings.filterwarnings("ignore")
import pickle, nltk
from collections import Counter

class train():
    def __init__(self):
        self.path = "src"
        self.filename = "UI-1M-tagged.txt"

    def dict_sentences(self):
        # create a corpus (list) contain all sentences in the training file
        corpus = None
        with open(self.path + "/" + self.filename) as train:
            corpus = train.read().split("./.")

        new_corpus = ["start/start " + item.lower() + "end/end" for item in corpus]
        return new_corpus

    def dict_emission(self):
        # count occurences each word with its tag
        new_corpus = self.dict_sentences()
        emission = [i for item in new_corpus for i in item.split()]
        emission_count = dict(Counter(emission))

        with open(self.path + "/" + "lib_emission_count.p", "wb") as f:
            pickle.dump(emission_count, f, protocol=pickle.HIGHEST_PROTOCOL)
            f.close()

        return emission_count
        
    def dict_emission_tag(self):
        # create dictionary of each word with all possibility tags, and its probability
        emission_count = self.dict_emission()

        total_word_count = sum(emission_count.values())

        emission_prob = {}
        for k, v in emission_count.items():
            try:
                word, postag = k.split("/")[0], k.split("/")[1]
                if k not in emission_prob.keys():
                    emission_prob[word] = {}
                    emission_prob[word][postag] = v / total_word_count
                else:
                    emission_prob[word][postag] = v / total_word_count
            except:
                # there are numbers in the training file, and it will be excluded
                pass

        with open(self.path + "/" + "lib_emission_prob.p", "wb") as f:
            pickle.dump(emission_prob, f, protocol=pickle.HIGHEST_PROTOCOL)
            f.close()

        return emission_prob
    
    def transition_dict(self):
        corpus  = self.dict_sentences()
        emission_prob = self.dict_emission_tag()

        unigram_tags, bigram_tags = [], []

        for item in corpus:
            try:
                tags = [i.split("/")[1] for i in item.split()]
                unigram_tags.extend(tags)
                bigram_tags.extend(list(nltk.ngrams(tags, 2)))
            except:
                pass

        unigram_count = dict(Counter(unigram_tags))
        bigram_count = dict(Counter(bigram_tags))

        transition_prob = {}
        for k, v in bigram_count.items():
            try:
                first_tag, second_tag = k[0], k[1]
                if first_tag not in transition_prob.keys():
                    transition_prob[first_tag] = {}
                    transition_prob[first_tag][second_tag] = v / unigram_count[first_tag]
                else:
                    transition_prob[first_tag][second_tag] = v / unigram_count[first_tag]
            except:
                pass

        with open(self.path + "/" + "lib_transition_prob.p", "wb") as f:
            pickle.dump(transition_prob, f, protocol=pickle.HIGHEST_PROTOCOL)
            f.close()

        return transition_prob

    def train_all_files(self):
        self.dict_sentences()
        self.dict_emission()
        self.dict_emission_tag()
        self.transition_dict()



train = train()
train.train_all_files()