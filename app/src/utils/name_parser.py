import nltk
from nltk.corpus import stopwords
stop = stopwords.words('english')


def get_names(text):
    
    names = []

    #Removing all the stop words and segmenting the text body into sentences
    text = " ".join([i for i in text.split() if i not in stop])
    sentences = nltk.sent_tokenize(text)
    
    #tokenizing each sentence
    sentences = [nltk.word_tokenize(sent) for sent in sentences]

    #POS Tagging each word in each sentence (DT=determiner,JJ=adjective,NN=noun)
    sentences = [nltk.pos_tag(sent) for sent in sentences]

    for tagged_sentence in sentences:
        for chunk in nltk.ne_chunk(tagged_sentence):
            if type(chunk) == nltk.tree.Tree:
                if chunk.label() == 'PERSON':
                    names.append(' '.join([c[0] for c in chunk]))
    if len(names) == 0:
        return ""
    return names[0]
