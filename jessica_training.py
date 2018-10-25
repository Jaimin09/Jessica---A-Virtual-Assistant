import numpy as np
from chat_utils import *
from helper_functions import *

from keras.layers import Bidirectional, LSTM, Dense, Activation, RepeatVector, Lambda, Concatenate, Dot, Input, Multiply
from keras.models import Model, load_model
from keras.optimizers import Adam
import keras.backend as K
import tensorflow as tf

##--------------------------Dealing with vocabs------------------------------------------

words_vocab = get_vocab('all_words_mine.txt')
Tq = 20

ques_data = np.genfromtxt('questions.txt', dtype = 'str', delimiter = '\n', encoding = 'utf8')
ques1, ques_oh1 = convert_string_data_to_onehot(ques_data[:5000], words_vocab, Tq)
ques2, ques_oh2 = convert_string_data_to_onehot(ques_data[5000:], words_vocab, Tq)


ques_oh = np.vstack((ques_oh1, ques_oh2))
ques = np.vstack((ques1, ques2))
print("Onehot file shape:", ques_oh.shape)

sent_vocab, inv_sent_vocab, sent_ind, sent_oh = get_everything_ans_sentences('answers.txt')


##----------------------------- Model -------------------------------------------------

repeator = RepeatVector(Tq)
concatenator = Concatenate(axis = -1)
densor = Dense(1, activation = 'relu')
activator = Activation('softmax')
dotor = Dot(axes = 1)

def one_step_attension(a, s_prev):
    # a = hidden state of Bi-LSTM of shape (m, Tx, 2*n_a)
    # s_prev = previous hidden state of post attension LSTM layer (creating as post_att.. = LSTM) of shape (m, n_s)
    
    s_prev = repeator(s_prev)           # so that its shape becomes (m, Tx, n_s) to concatenate with a
    
    concat = concatenator([a, s_prev])
    
    energy = densor(concat)
    
    alpha = activator(energy)
    
    context = dotor([alpha, a])
    
    return context


n_a = 64
n_s = 2*n_a
post_activation_LSTM_cell = LSTM(n_s, return_state = True)
output_layer = Dense(sent_oh.shape[1], activation='softmax')

def model(Tx, ques_vocab_size, n_s):
    
    X = Input(shape=(Tx, ques_vocab_size))
    s0 = Input(shape=(n_s,), name='s0')
    c0 = Input(shape=(n_s,), name='c0')
    s = s0
    c = c0
    
    a = Bidirectional(LSTM(n_a, return_sequences = True))(X)
    
    context = one_step_attension(a, s)

    s, _, c = post_activation_LSTM_cell(context, initial_state = [s, c])       # s= hidden state, c= cell state

    out = output_layer(s)
        
    model = Model(inputs = [X, s0, c0], outputs = out)
    
    return model

##--------------------------------------Training--------------------------------------------

jess_model = model(Tq, len(words_vocab), n_s)

out = jess_model.compile(optimizer=Adam(lr=0.005, beta_1=0.9, beta_2=0.999, decay=0.01),
                    metrics=['accuracy'],
                    loss='categorical_crossentropy')


m = ques_data.shape[0]
n_s = 128
s0 = np.zeros((m, n_s))
c0 = np.zeros((m, n_s))

jess_model.fit([ques_oh, s0, c0], sent_oh, epochs = 2, batch_size= 64)

## ------------------------------------Saving------------------------------------------
jess_model.save("jessica_model.h5")

