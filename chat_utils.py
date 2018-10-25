import numpy as np
from keras.utils import to_categorical
import keras.backend as K
from helper_functions import _all_functions_dictionary_

def get_vocab(file_name):
    total = np.genfromtxt(file_name, delimiter = '\n', dtype = 'str', encoding = 'utf8')
    
    total_words = []
    for total_sent in total:
        for word in total_sent.split():
            total_words.append(word.lower())

    total_vocab = sorted(list(set(total_words)))  
    print("total words in vacab:",len(total_vocab))
    total_vocab = {word:i for i, word in enumerate(total_vocab)}
    
    return total_vocab

def get_max_length(X):
    max_words = 0
    for sentence in X:
        sent_indices = [word.lower() for word in sentence.split()]
        if len(sent_indices)> max_words:
            max_words = len(sent_indices)
            
    return max_words

def convert_to_one_hot(Y, C):
    Y = np.eye(C)[np.array(Y).reshape(-1)]
    return Y

def convert_string_data_to_onehot(dataset, total_vocab, Tx):
    m = np.array(dataset).shape[0]
    X = np.zeros((m, Tx),dtype = 'int')
    i = 0
    for sent in dataset:
        j = 0
        for word in sent.split():
            X[i, j] = total_vocab[word.lower()]
            j += 1
        i += 1

    Xoh = np.array(list(map(lambda x: to_categorical(x, num_classes=len(total_vocab)), X)))
    
    return X, Xoh

def convert_example_to_indices(example, total_vocab, Tx):
    X = np.zeros((1, Tx), dtype = 'int')
    i = 0
    for word in example.split():
        X[:, i] = total_vocab[word]
        i += 1
        
    return X

def get_everything_ans_sentences(file_name):
    ans_data = np.genfromtxt(file_name, dtype = 'str', delimiter = '\n', encoding = 'utf8')
    
    inv_sent_vocab = {i:sent for i, sent in enumerate(sorted(set(ans_data)))}
    sent_vocab = {sent:i for i, sent in inv_sent_vocab.items()}
    
    sent_ind = []
    for sent in ans_data:
        sent_ind.append(sent_vocab[sent])
    
    sent_ind = np.array(sent_ind)    
    sent_oh = convert_to_one_hot(sent_ind, C = len(sent_vocab))
    
    func_vocab = _all_functions_dictionary_()
    
    for i in range(len(inv_sent_vocab)):
        for string, func in func_vocab.items():
            if inv_sent_vocab[i] == string:
                inv_sent_vocab[i] = func_vocab[string]
    
    sent_vocab = {sent:i for i, sent in inv_sent_vocab.items()}
    
    print("Indices file shape:", sent_ind.shape)
    print("Onehot file shape:", sent_oh.shape)
    print("Total number of sentences in sent_vocab :", len(sent_vocab))
    
    return sent_vocab, inv_sent_vocab, sent_ind, sent_oh

def remove_unknown(sentence, words_vocab):
    count = 0
    flag = 1
    
    sentence = sentence.split()
    sentence.append('0')
    sentence_words = sentence
    for i in range(len(sentence_words)):
        if flag == 0:
            sentence[i-1] = '0'
        flag = 0
        for words in words_vocab:
            if sentence_words[i] == words:
                count += 1
                flag = 1
                
    sent_final = []
    for wrd in sentence:
        if wrd != '0':
            sent_final.append(wrd)
    sentence = ' '.join(sent_final)
    return  sentence

'''
def check_word_exist(sentence, words_vocab):
    exist = False
    count = 0
    for word in sentence.split():
        for words in words_vocab:
            if word == words:
                count += 1
    if count ==  len(sentence.split()):
        exist = True
    return exist


def get_embedding_from_dictionary(dictionary1, dictionary2, word_to_emb_vec):
    word_emb = {}
    dictionary = sorted(set(np.hstack((dictionary1, dictionary2))))
    for word in dictionary:
        word_emb[word] = word_to_emb_vec[word]
    print("Total number of words in embedding dictionary is :", len(word_emb))
    return word_emb'''

'''def read_glove_vecs(glove_file):
    with open(glove_file, 'r', encoding="utf8") as f:
        words = set()
        word_to_vec_map = {}
        for line in f:
            line = line.strip().split()
            curr_word = line[0]
            words.add(curr_word)
            word_to_vec_map[curr_word] = np.array(line[1:], dtype=np.float64)
        
        i = 1
        words_to_index = {}
        index_to_words = {}
        for w in sorted(words):
            words_to_index[w] = i
            index_to_words[i] = w
            i = i + 1
    return words_to_index, index_to_words, word_to_vec_map'''