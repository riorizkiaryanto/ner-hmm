import warnings
warnings.filterwarnings("ignore")
import pickle
import operator

class ner_hmm():
    def __init__(self, input_string):
        self.input = input_string
        self.src_path = "src"

        with open(self.src_path + "/" + 'lib_emission_prob.p', "rb") as f:
            result = pickle.load(f)
            f.close()
        
        self.emission_prob = result

        with open(self.src_path + "/" + 'lib_transition_prob.p', "rb") as f:
            result = pickle.load(f)
            f.close()
        
        self.transition_prob = result

    def ner(self):
        list_words = self.input.lower().split()

        emission_prob = self.emission_prob
        transition_prob = self.transition_prob

        viterbi_matrix = {}
        result = ""
        for i, item in enumerate(list_words):
            viterbi_matrix[item] = {}
            try:
                if i == 0: 
                    prev_tag = "start"
                else: 
                    pass

                for k in emission_prob[item].keys():
                    transition = transition_prob[prev_tag][k]
                    viterbi_matrix[item][k] = emission_prob[item][k] * transition

                prev_tag = max(viterbi_matrix[item].items(), key=operator.itemgetter(1))[0]
                
            except Exception as e:
                # print(e)
                prev_tag = "nn" # to cover out of dictionary word, will be tagged as "nn"

            post_tagger_result = result + item + "/" + prev_tag + " "
            print(post_tagger_result)


if __name__ == "__main__":
    input = input("Enter your text: ")
    ner_hmm(input).ner()

