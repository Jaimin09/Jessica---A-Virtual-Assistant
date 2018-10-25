from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
from keras.models import load_model
from chat_utils import *
from helper_functions import *
import webbrowser
import speech_recognition as sr
import winsound

app = Flask(__name__)

def get_model():
    global model, graph
    model = load_model('jessica_model.h5')
    graph = tf.get_default_graph()
    print("* Model Loaded successfully !")

print("* Loading Model ...")
get_model()

words_vocab = get_vocab('all_words_mine.txt')
ques_data = np.genfromtxt('questions.txt', dtype = 'str', delimiter = '\n', encoding = 'utf8')
_, inv_sent_vocab, _, _ = get_everything_ans_sentences('answers.txt')

m = ques_data.shape[0]
Tq = 20
n_s = 128
s0 = np.zeros((m, n_s))
c0 = np.zeros((m, n_s))

@app.route("/predict", methods = ['POST'])
def predict():
    
    message = request.get_json(force = True)
    data = message['data'] 
    if data == "":
        r = sr.Recognizer()
        winsound.PlaySound('chime-short.wav', winsound.SND_FILENAME)
        
        with sr.Microphone() as source:
            print("Say something!")
            r.pause_threshold = 0.6
            audio = r.listen(source)
        winsound.PlaySound('chime.wav', winsound.SND_FILENAME)
        print("audio recorded!")
        msg_data = remove_profanity(r.recognize_google(audio).lower())
        try:
            print("You said: " + msg_data)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
        my_msg = msg_data
    else:
        my_msg = data
        msg_data = data
   
    data = remove_profanity(msg_data)
    data = filter_zero(data)
    pred_output = check_post(data)
    data = filter_three(filter_two(filter_one((data))))
    
    data = remove_unknown(data, words_vocab)
    if not pred_output:
        if len(data.split()) < 21 :
            data = convert_example_to_indices(data, words_vocab, Tq)
            data = convert_to_one_hot(data, C= len(words_vocab)).reshape(1, Tq, len(words_vocab))
            with graph.as_default():
                prediction = model.predict([data, s0, c0])
                prob = max(max(prediction))
                print(prob)
                if prob < 0.60:
                    pred_output = "Good for you !"
                else:
                    prediction = np.argmax(prediction, axis = -1)
                    for i in prediction:                        
                        if isinstance(inv_sent_vocab[i], str) == True :
                            pred_output = inv_sent_vocab[i]
                        else :
                            pred_output = inv_sent_vocab[i]()

        else:
            pred_output = "Sorry ! but can you short it down ? Please ."
    
        
    response = {
            'prediction' : "Jessica: " + pred_output,
            'my_msg' : "You: "+ my_msg
        }

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
