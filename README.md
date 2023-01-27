# Named Entity Recognition using Hidden Markov Model

This repo contains codes to implement Hidden Markov Model in Named Entity Recognition analysis. 
Named Entity Recognition (NER) or sometimes referred to entity extraction or identification - is a process of identifying and categorizing key entities in the text. An entity itself can referred to any information such as person, location, or any word or series of words. NER is a part of Natural Processing Langugage (NLP) - a subfield of artifical intelligence used to analysis the human natural language. 

Here, Named Entity Recognition process was done by implementing Hidden Markov Model (HMM). HMM is a probabilistic model that usually applied in a simple sequential machine learning problems. The model itself uses the 'hidden' information or states from the data identify the entity. 

## How to use this repo
To be noted, the codes can only be used for the text written in Indonesian. You can used it for the another language if you have the dataset. 
Here, I used the Post-Tagging public dataset that can be downloaded [here](http://panl10n.net/english/OutputsIndonesia2.htm (One Million POS Tagged Corpus of Bahasa Indonesia) ). The file should named *UI-1M-tagged.txt*
It is been a long time since I downloaded the dataset, so I am not sure if it still available or not.

To run this repo:
1. If you have *UI-1M-tagged.txt* file, use it and run the file **ner_train.py** first
2. The file **ner_train.py** will generate some pickle files. These pickle files contain information about the data pattern
3. Run **ner_hmm.py** file to use the NER model
4. It will ask you to input the text written in Indonesian
5. The output will show each words and the post-tag belonging to it