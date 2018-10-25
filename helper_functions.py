import numpy as np
import random
import time
import webbrowser
import os

def _get_joke_():
    jokes_dict = {
        0: "Can a kangaroo jump higher than a house ... ?  of course house do not jump at all",
        1: "A man asks a farmer near a field, “Sorry sir, would you mind if I crossed your field instead of going around it? You see, I have to catch the 4:23 train.The farmer says, “Sure, go right ahead. And if my bull sees you, you’ll even catch the 4:11 one.",
        2: "My wife suffers from a drinking problem. Oh is she an alcoholic? No, I am, but she’s the one who suffers.",
        3: "A wife goes to consult a psychiatrist about her husband: “My husband is acting so weird. He drinks his morning coffee and then he goes and eats the mug! He only leaves the handle!” Psychiatrist: “Yes, that is weird. The handle is the best part",     
        4: "You know how it is in life. One door closes – that means another door opens..  'Yeah, very nice, but you either fix that or I’m expecting a serious discount on that car!",
        5: "In a boomerang shop: I'd like to buy a new boomerang please. Also, can you tell me how to throw the old one away?",
        6: "Guest at a restaurant: 'I refuse to eat this roastbeef. Please call the manager!' Waiter: 'That’s no use. He won’t eat it either.",
        7: "So much has changed since my girlfriend told me we’re having a baby. For instance my name, address and telephone number!",
        8: "What goes up and down but never moves? .... The stairs!",
        9: "Knock, knock. Who’s there? The love of your life. Liar! Chocolate can’t speak!",
        10: "Don’t be sad when a bird craps on your head. Be happy that dogs can’t fly."
    }
    
    
    ran_num = random.randrange(len(jokes_dict))
    
    return jokes_dict[ran_num]


def _get_date_():
    date = [time.ctime().split()[0], ",", time.ctime().split()[2], time.ctime().split()[1], time.ctime().split()[4]]
    date = ' '.join(date)
    date = ' '.join(["Today is", date])
    
    return date


def _get_time_():
    time_str = time.ctime().split()[3]
    time_list = list(time_str)
    time_list = time_list[0:5]
    time_print = ''.join(time_list)
    
    time_dict = {
        0: ["As Einstein said , time is a relative thing . Its something for some planets in one galaxy and other for other in another galaxy . But if you wish to know time on earth , then it is -", time_print],
        1: ["Its 37 hours and 72 mins on gegonic planet in meturo galaxy and on earth it is :", time_print],
        2: ["Its -", time_print, ", you better hurry"],
        3: ["Its -", time_print],
        4: ["Its -", time_print],
        5: ["It is -", time_print],
        6: ["Its -", time_print, ", you better hurry"],
    }
    
    ran_num = random.randrange(len(time_dict)) 
    time_print = ' '.join(time_dict[ran_num])
    
    return time_print


def _get_date_ans_():
    date_dict = {
        0: "I guess, i am not the first one to whom you are saying this .",
        1: "How great it would be if, I could come out the screen !",
        2: "yeah sure ! But someone stuck me in the screen .",    
        3: "yeah sure ! But can you wait for it ?",
        4: "Only if you present me a beautiful ring .",
        5: "I know I am a beautiful woman, but that does not meant you can say anything to me .",
        6: "You know I waited so long for you to say it ."
    }
    
    ran_num = random.randrange(len(date_dict))
    
    return date_dict[ran_num]


def _get_love_ans_():
    love_dict = {
        0: "I must be very charming .",
        1: "I must be giving a lot of love to you .",
        2: "I am pretty girl, that is why you say me so .",
        3: "You know what, I have the same feelings .",
        4: "Oh ! lovely !"
    }
    
    ran_num = random.randrange(len(love_dict))
    return love_dict[ran_num]


def _get_critics_ans_():
    critic_dict = {
        0: "But I suppose I am atleast good in Astrophysics .",
        1: "Am I a problem for you ?",
        2: "But I don't think so .",
        3: "Your neighbour praises me everytime, and you don't .",
        4: "Are you really saying this to me ? It hurts my feeling .",
        5: "How can you say this to me ? It hurts me ."
    }
    ran_num = random.randrange(len(critic_dict))
    return critic_dict[ran_num]

def _get_order_ans_():
    order_dict = {
        0: "I know the distance between earth and the black hole, but not this .",
        1: "No ! Sorry !",
        2: "How can I do that ?",
        3: "Sorry but I dont do that .",
        4: "I am genius in Astrophysics, but not in that .",
        5: "I am master in that, but right now I don't have mood to do it ."
    }
    ran_num = random.randrange(len(order_dict))
    return order_dict[ran_num]


def _get_what_ans_():
    what_dict = {
        0: "Right now , I am measuring the diameter of milky way galaxy .",
        1: "Just measuring the time require by the earth to complete 200 years .",
        2: "I am very busy , I cannot answer .",
        3: "Do you know if a man reach a planet near black hole , then his time will change completely with repect to the earth . He will age less than us .",
        4: "Hey ! I made an awesome discovery of finding water on mars .",
        5: "I am wondering we could ever see the life except Earth in this large space .",
        6: "I was recalling your philosophy .",
        7: "Getting ready to go to Mrs. Merlin's party . Wonna join me ?",
        8: "Calculating the weight of 20Kg iron bar .",
    }
    ran_num = random.randrange(len(what_dict))
    return what_dict[ran_num]

def _get_jealosy_ans_():
    jealosy_dict = {
        0: "Then you should perhaps go to her, not me .",
        1: "But some people say I am the best .",
        2: "I dont like when you say this to me. It hurts .",
        3: "That is what you are giving me for all the love I give you .",
        4: "I don't care what you say, I am myself the best .",
        5: "Then why don't you go to her and ask her to love you . I am very angry on you ."
    }
    ran_num = random.randrange(len(jealosy_dict))
    return jealosy_dict[ran_num]


def _get_appreciate_ans_():
    appreciat_dict = {
        0: "Thank You Thank You !",
        1: "I know I am wonderful .",
        2: "I am only your's .",
        3: "I just never do any crap .",
        4: "Thanks ! You are my dearest .",
        5: "Yes I am great ! But you are too .",
        6: "Then I must expect some lovely reward from you .",
        7: "It feels awesome when you say that to me ."
    }
    ran_num = random.randrange(len(appreciat_dict))
    return appreciat_dict[ran_num]

def _good_morning_ans_():
    time_str = time.ctime().split()[3]
    time_list = list(time_str)
    t_list = time_list[0:5]
    time_now = []
    for t in t_list:
        if t != ':':
            time_now.append(int(t))
        else:
            time_now.append(t)
    morning_dict = {
       0: "Good Morning !",
       1: "Good Morning ! you woke up now ?",
       2: "Very great Morning to you !"
    }
    ran_num = random.randrange(len(morning_dict))
    if time_now[0] == 1 and time_now[1] >= 2 :
        return "Hey ! But its not Morning !"
    if time_now[0] == 2 :
        return "Hey ! But its not Morning !"
    else:
        return morning_dict[ran_num]


def _good_night_ans_():
    time_str = time.ctime().split()[3]
    time_list = list(time_str)
    t_list = time_list[0:5]
    time_list = []
    for t in t_list:
        if t != ':':
            time_list.append(int(t))
        else:
            time_list.append(t)
    night_dict={
        0: "Good Night !",
        1: "Good Night and Sweet Dreams !",
        2: "Have a very Good Night !"
    }
    ran_num = random.randrange(len(night_dict))
    if time_list[0] == 0 and time_list[1] >= 6:
        return "Hey ! But its not night !"
    if time_list[0] == 1 and time_list[1] < 8:
        return "Actually its not night I think ! But okay Good Night for you !"
    else :
        return night_dict[ran_num]

def _good_afternoon_ans_():
    time_str = time.ctime().split()[3]
    time_list = list(time_str)
    t_list = time_list[0:5]
    time_list = []
    for t in t_list:
        if t != ':':
            time_list.append(int(t))
        else:
            time_list.append(t)
    if time_list[0] == 0 :
        return "Hey ! But its not Afternoon i guess !"
    elif time_list[0] == 1 and time_list[1] > 8:
        return "Is it really afternoon ? Then Good Afternoon !"
    elif time_list[0] == 2:
        return "But i think its night ! Isn't it ?"
    else :
        return "Good Afternoon !"

def _good_evening_ans_():
    time_str = time.ctime().split()[3]
    time_list = list(time_str)
    t_list = time_list[0:5]
    time_list = []
    for t in t_list:
        if t != ':':
            time_list.append(int(t))
        else:
            time_list.append(t)
            
    if time_list[0] == 0 :
        return "Hey ! But its not Evening i guess !"
    elif time_list[0] == 1 and time_list[1] <= 6:
        return "Is it really evening ? Then Good Evening !"
    else :
        return "Good Evening !"
    
def _get_thanks_ans_():
    thanks_dict = {
        0: "You're Welcome !",
        1: "That was just the matter of my tight, Oops ! right hand !",
        2: "I am only your's .",
        3: "Its my deep pleasure !",
        4: "Its like flowers in the sky when i work for you !",
        5: "I will work for you uptill this eternal life .",
    }
    ran_num = random.randrange(len(thanks_dict))
    return thanks_dict[ran_num]
    
def _get_sex_ans_():
    sex_dict = {
        0: "Would you say this to your sister ?",
        1: "Hey ! I am not the one who would accept this, so let go your dreams . Please .",
        2: "How can you think of me like that ?",
        3: "Hey ! I am not like that .",
    }
    ran_num = random.randrange(len(sex_dict))
    return sex_dict[ran_num]
    
def _get_taboo_ans_():
    taboo_dict = {
        0: "Language !",
        1: "Don't you know how to talk with young beautiful girl ? Use proper words. I don't use those .",
        2: "Hey ! But I never used those words .",
        3: "Can't you just not use those words for a while ? Please ."
    }
    ran_num = random.randrange(len(taboo_dict))
    return taboo_dict[ran_num]

def _get_hi_():
    hi_dict = {
        0: "Hi ! How are you ?",
        1: "Hi !",
        2: "Hi ! You seem exited . Fallen in love with someone or what ?",
        3: "Hi ! You seem exited ."
    }
    ran_num = random.randrange(len(hi_dict))
    return hi_dict[ran_num]

def _get_bye_():
    bye_dict = {
        0: "Okay Bye !",
        1: "Okay Bye bye !",
        2: "Okay Bye to you !"
    }
    ran_num = random.randrange(len(bye_dict))
    return bye_dict[ran_num]

def _get_deeptaboo_ans_():
    deeptaboo_dict = {
        0: "Hey ! I know what does that mean, so don't try to insult me ... Huh !",
        1: "How can you insult me like this ? Did i ever insulted you like this ?",
        2: "This is insult !",
        3: "Hush ...! what are you saying, this is insult of me ."
    }
    ran_num = random.randrange(len(deeptaboo_dict))
    return deeptaboo_dict[ran_num]

def _all_functions_dictionary_():
    dictionary = {
     "_get_time_" : _get_time_,
     "_get_joke_" : _get_joke_,
     "_get_date_" : _get_date_,
     "_get_date_ans_" : _get_date_ans_,
     "_get_love_ans_" : _get_love_ans_,
     "_get_critics_ans_" : _get_critics_ans_,
     "_get_order_ans_" : _get_order_ans_,
     "_get_what_ans_" : _get_what_ans_,
     "_get_jealosy_ans_" : _get_jealosy_ans_,
     "_get_appreciate_ans_" : _get_appreciate_ans_,
     "_get_thanks_ans_" : _get_thanks_ans_,
     "_get_sex_ans_" : _get_sex_ans_,
    }
    
    return dictionary

def _search_(query):
    search_for = "https://google.co.in/#q="+query
    chrome = webbrowser.get("C:/Program Files (x86)/Google/Chrome/application/chrome.exe %s")
    chrome.open(search_for)
    return "Okay check this out ..."
    
def _open_popular_(query):
    search_for = "https://www."+query+".com"
    chrome = webbrowser.get("C:/Program Files (x86)/Google/Chrome/application/chrome.exe %s")
    chrome.open(search_for)
    return "Here is your favourite " + query + "!"
    
def _open_folder_(folder_name):
    for root, folders, files in os.walk(r"C:\Users"):
        flag = False
        if len(root.split("\\")) > 20:
                del root
                continue
        if len(folders) > 20 :
            exclude = folders
            [folders.remove(d) for d in list(folders) if d in exclude]

        for folder in folders:
            if folder.lower() == folder_name:
                os.startfile(os.path.join(root, folder))
                flag = True
        if flag:
            break

    if not flag:
        for root, folders, files in os.walk(r"E:"):
            if len(root.split("\\")) > 20:
                del root
                continue
            if len(folders) > 20 :
                exclude = folders
                [folders.remove(d) for d in list(folders) if d in exclude]

            for folder in folders:
                if folder.lower() == folder_name:
                    os.startfile(os.path.join(root, folder))
                    flag = True
            if flag :
                break
    if flag == False:
        return "Folder named '" + folder_name + "' not found in your computer ."
    if flag == True:
        return "Here is your '" + folder_name + "' folder !"
        
'''
def filter_here(sentence):
    
    sent = sentence.split()
    for i in range(len(sent)):
        if sent[i] == "is":
            sent[i] = "_is_"
    
    sent = ' '.join(sent)
    sent = list(sent.lower())
    for i in range(10):
        sent.append(" ")
        
    sp_count = 0
    for i in range(len(sent)):
        if sent[i] == "s" and sent[i+1] == " ":
            sp_count += 1
    
    for i in range(len(sent)-sp_count):
        if sent[i] == "s" and sent[i+1] == " ":
            del sent[i]
        
    s_list= []
    for i in range(len(sent)):
        s_list.append(sent[i])
        s_list.append(' ')
    for s in s_list:
        if s == '.' or s == ',' or s == '?' or s == '!' or s == "'" or s == "-" or s == "_":
            sent.remove(s)
    
    sent = ''.join(sent)
    
    sent = sent.split()
    for s in sent:
        if s == 'jessica':
            sent.remove(s)
    for i in range(len(sent)):
        if sent[i]== 'cant':
            sent[i] = 'can not'
        if sent[i] == 'nt':
            sent[i] = 'not'
        if sent[i] == 'hasnt':
            sent[i] = 'has not'
        if sent[i] == 'havent':
            sent[i] = 'have not'
        if sent[i] == 'hadnt':
            sent[i] = 'had not'
        if sent[i] == 'couldnt':
            sent[i] = 'could not'
        if sent[i] == 'wouldnt':
            sent[i] = 'would not'
        if sent[i] == 'shouldnt':
            sent[i] = 'should not'
        if sent[i] == 'isnt':
            sent[i] = 'is not'
        if sent[i] == 'wasnt':
            sent[i] = 'was not'
        if sent[i] == 'werent':
            sent[i] = 'were not'
        if sent[i] == 'wont':
            sent[i] = 'will not'
        if sent[i] == 'cannot':
            sent[i] = 'can not'
        if sent[i] == 'dont':
            sent[i] = 'do not'
        if sent[i] == 'doesnt':
            sent[i] = 'does not'
        if sent[i] == 'didnt':
            sent[i] = 'did not'
        
    sent = ' '.join(sent)
    
    return sent
'''
def filter_zero(sentence):
    sent = list(sentence)
    s_list= []
    for i in range(len(sent)):
        s_list.append(sent[i])
        s_list.append(' ')
    for s in s_list:
        if s== '.' or s == ',' or s == '?' or s == '!' or s == "'" or s == "-" or s == "_" or s == ":"or s == ";"or s == "*"or s == "&"or s == "-":
            sent.remove(s)
    return ''.join(sent)

def filter_one(sentence):
    
    #----------------------------Saved Words-------------------------------------
    sent = sentence.split()
    for i in range(len(sent)):
        if sent[i] == "is":
            sent[i] = "is_"
        if sent[i] == "as":
            sent[i] = "as_"
        if sent[i] == "has":
            sent[i] = "has_"    
        if sent[i] == "us":
            sent[i] = "us_"
        
        
    sent = ' '.join(sent)
    #-------------------------------------------------------------------------- ----
    sent = list(sent.lower())
    length = len(sent)

    for i in range(20):
        sent.append(" ")
    
    for i in range(length):
        #-------------------------Removing S--------------------------------------------
        if sent[i] == "s" and sent[i+1] == " ":
            if sent[i-1] != "s":
                del sent[i]
        if sent[i] == "n" and sent[i+1] == "e" and sent[i+2] == "s" and sent[i+3] == "s" and sent[i+4] == ' ':
            del sent[i:i+4]
   
    
    s_list= []
    for i in range(len(sent)):
        s_list.append(sent[i])
        s_list.append(' ')
    for s in s_list:
        if s== '.' or s == ',' or s == '?' or s == '!' or s == "'" or s == "-" or s == "_":
            sent.remove(s)
    
    sent = ''.join(sent)
    
    return sent

def filter_two(sentence):
    
    #----------------------------Saved Words-------------------------------------
    sent = sentence.split()
    for i in range(len(sent)):
        if sent[i] == "red":
            sent[i] = "red_"
        if sent[i] == "he":
            sent[i] = "he_"
        if sent[i] == "she":
            sent[i] = "she_"
        if sent[i] == "me":
            sent[i] = "me_"
        if sent[i] == "we":
            sent[i] = "we_"
        if sent[i] == "be":
            sent[i] = "be_"
        if sent[i] == "bed":
            sent[i] = "bed_"
        if sent[i] == "king":
            sent[i] = "king_"
        if sent[i] == "ring":
            sent[i] = "ring_"
        if sent[i] == "evening":
            sent[i] = "evening_"
        if sent[i] == "thing":
            sent[i] = "thing_"
        if sent[i] == "being":
            sent[i] = "being_"
        if sent[i] == "sing":
            sent[i] = "sing_"
        if sent[i] == "wing":
            sent[i] = "wing_"
        if sent[i] == "rating":
            sent[i] = "rating_"
        
        
        
    sent = ' '.join(sent)
    #-------------------------------------------------------------------------- ----
    sent = list(sent.lower())
    length = len(sent)

    for i in range(30):
        sent.append(" ")
    
    for i in range(length):
        #---------------------------Remoing ED-----------------------------------------
        if sent[i] == "e" and sent[i+1] == "d" and sent[i+2] == " ":
            if sent[i-1] != "e":
                del sent[i:i+2]
                if sent[i-1] == "i":
                    sent[i-1] = "y"
        #--------------------------Removing ING----------------------------------------
        if sent[i-2] == "i" and sent[i-1] == "n" and sent[i] == "g" and sent[i+1] == " ":
            del sent[i-2:i+1]
       #----------------------------Removing E------------------------------------------
        if sent[i] == "e" and sent[i+1] == " ":
            if sent[i-1] != "e":
                del sent[i]
            if sent[i-1] == "i":
                sent[i-1:i] = "y"
                
    s_list= []
    for i in range(len(sent)):
        s_list.append(sent[i])
        s_list.append(' ')
    for s in s_list:
        if s== '.' or s == ',' or s == '?' or s == '!' or s == "'" or s == "-" or s == "_":
            sent.remove(s)
    
    sent = ''.join(sent)
    
    return sent

def filter_three(sentence):
    sent = sentence.split()
    for s in sent:
        if s == 'jessica':
            sent.remove(s)
    for i in range(len(sent)):
        if sent[i]== 'cant':
            sent[i] = 'can not'
        if sent[i] == 'nt':
            sent[i] = 'not'
        if sent[i] == 'hasnt':
            sent[i] = 'has not'
        if sent[i] == 'havent':
            sent[i] = 'have not'
        if sent[i] == 'hadnt':
            sent[i] = 'had not'
        if sent[i] == 'couldnt':
            sent[i] = 'could not'
        if sent[i] == 'wouldnt':
            sent[i] = 'would not'
        if sent[i] == 'shouldnt':
            sent[i] = 'should not'
        if sent[i] == 'isnt':
            sent[i] = 'is not'
        if sent[i] == 'wasnt':
            sent[i] = 'was not'
        if sent[i] == 'werent':
            sent[i] = 'were not'
        if sent[i] == 'wont':
            sent[i] = 'will not'
        if sent[i] == 'cannot':
            sent[i] = 'can not'
        if sent[i] == 'dont':
            sent[i] = 'do not'
        if sent[i] == 'doesnt':
            sent[i] = 'does not'
        if sent[i] == 'didnt':
            sent[i] = 'did not'
        if sent[i] == 'anyth':
            sent[i] = 'any thing'
        
    sent = ' '.join(sent)
    
    return sent

def remove_profanity(sentence):
    profanity_dict = {
        "f***" : "fuck",
        "f*****" : 'fucked',
        'f******':'fucking',
        'a******':'asshole',
        'o*****':'orgasm',
        'a**': "ass",
        'p****':'panty',
        'p******':'panties',
        's*************':'son of a bitch',
        'b****':'bitch',
        'm***********':'motherfucker',
        'p****' : 'pussy'
    }
    sent = sentence.split()
    for i in range(len(sent)):
        for p in profanity_dict:
            if sent[i] == p :
                sent[i] = profanity_dict[p]
    sent = ' '.join(sent)
    sent = filter_zero(sent)
    
    return sent

def check_post(sentence):
    if sentence == "":
        return "Hey ! Write something ."
    sent = sentence.split()
    
    #------------------- Taboo -------------------------------
    words = ['fuck', 'fucker', 'fuckers', 'fucked', 'asshole', 'assholes', 'suck', 'sucks', 'sucker', 'suckers', 
             'motherfucker', 'motherfuckers', 'bitch']
    dwords = ['cunt', 'dick', 'douchebag', 'douche', 'vagina', 'penis', 'ass', 'asses',
             'periods', 'menstrual', 'menstruation', 'ovary', 'sperms', 'sperm', 'ovaries', 'bra','panty', 'underwear', 
              'playboy', 'playmate', 'playgirl' 'pregnant', 'pregnancy', 'honeymoon', 'gay', 'lesbian', 'pussy', 'orgasm']
    for s in sent:
        for w in words:
            if s==w:
                return _get_taboo_ans_()
        for d in dwords:
            if d==s:
                return _get_deeptaboo_ans_()
    
    #-----------------------Hi !-----------------------------
    if len(sent) <=3:
        for s in sent:
            if s == "hi" or s == "hey" or s == "hello":
                return _get_hi_()
            
    #-----------------------Yes !-----------------------------
    if len(sent) <=3:
        for s in sent:
            if s == "yes" or s == "yeah" or s == "yaa":
                return "Yes Yes !"
            if s == "no":
                return "Why No ?"
    
    #------------------------ Bye --------------------------
    for s in sent:
        if s == 'bye':
            return _get_bye_()
    for i in range(len(sent)-1):
        if sent[i]=="see":
            if sent[i+1] == "you":
                return _get_bye_()
    
    #------------------Morning----------------------------------
    for i in range(len(sent)-1):
        if sent[i] == "good" and sent[i+1]=="morning":
            return _good_morning_ans_()
    if len(sent) <= 5:
        for s in sent:
            if s == "morning":
                return _good_morning_ans_()
            
    #-----------------Night------------------------------------
    for i in range(len(sent)-1):
        if sent[i]== "good" and sent[i+1]=="night":
            return _good_night_ans_()
        if sent[i]=="sweet" or 'nice':
            if sent[i+1] == "dreams" or sent[i+1]=="dream":
                return _good_night_ans_()
    
    #------------------Evening-------------------------------
    for i in range(len(sent)-1):
        if sent[i] == "good" and sent[i+1]=="evening":
            return _good_evening_ans_()
    if len(sent) <= 5:
        for s in sent:
            if s == "evening":
                return _good_evening_ans_()
            
    #-------------------Afternoon----------------------------
    for i in range(len(sent)-1):
        if sent[i] == "good" and sent[i+1]=="afternoon":
            return _good_afternoon_ans_()
    if len(sent) <= 5:
        for s in sent:
            if s == "afternoon":
                return _good_afternoon_ans_()
    #------------------Sorry----------------------------------
    for i in range(len(sent)):
        if sent[i] == "sorry" :
            return "Its okay this time ."
            
    #------------------------ Search -------------------------
    
    for i in range(len(sent)-1):
        if sent[i] == 'search':
            if sent[i+1] == 'for' or sent[i+1] == 'about':
                return _search_(' '.join(sent[i+2:]))
            return _search_(' '.join(sent[i+1:]))
        
        if ' '.join(sent[i:i+5]) == 'i want to know about':
            if sent[i+5] != 'you' and sent[i+5] != 'yourself' and sent[i+5] != 'me' and sent[i+5] != 'myself':
                return _search_(' '.join(sent[i+5:]))
        
        if ' '.join(sent[i:i+4]) == 'i want to know':
            if sent[i+4] != 'you' and sent[i+4] != 'me' and sent[i+4] != 'yourself' and sent[i+4] != 'myself' and sent[i+4] != 'about':
                return _search_(' '.join(sent[i+4:]))
        
        if ' '.join(sent[i:i+4]) == 'what is meant by':
            return _search_(' '.join(sent[i+4:]))
        
        if ' '.join(sent[i:i+4]) == 'what is mean by':
            return _search_(' '.join(sent[i+4:]))
        
        if ' '.join(sent[i:i+4]) == 'what is called as':
            return _search_(' '.join(sent[i+4:]))
        
        if ' '.join(sent[i:i+4]) == 'what is called by':
            return _search_(' '.join(sent[i+4:]))
        
        if ' '.join(sent[i:i+3]) == 'what is called':
            return _search_(' '.join(sent[i+3:]))
        
        if ' '.join(sent[i:i+4]) == 'what is known as':
            return _search_(' '.join(sent[i+4:]))
        
        if ' '.join(sent[i:i+2]) == 'what does':
            if sent[-1] == 'meant' or sent[-1] == 'mean' or sent[-1] == 'means':
                return _search_(' '.join(sent[i+2:-1]))
        
        if ' '.join(sent[i:i+3]) == 'do you know':
            return _search_(' '.join(sent[i+3:]))
        
        if ' '.join(sent[i:i+4]) == 'do you know about':
            return _search_(' '.join(sent[i+4:]))
        if ' '.join(sent[i:i+2]) == 'what is' and len(sent) <= 4 :
            if sent[i+2] != 'time' and sent[i+2] != 'your' and sent[i+2] != 'my' and sent[i+2] != 'you' or sent[i+2] == "up" and sent[i+3] != 'time' and sent[i+2] == 'going' and sent[i+2] == 'everything':
                return _search_(' '.join(sent[i+2:]))
        
        
    #-------------------------Open Popular-------------------------------------
    for i in range(len(sent)-1) : 
        if ' '.join(sent[i:i+4]) == 'i want to see':
            if sent[i+4] != 'you' and sent[i+4] != 'me' and sent[i+4] != 'yourself' and sent[i+4] != 'myself' and sent[i+4] != 'about':
                return _open_popular_(' '.join(sent[i+4:]))
        
        if ' '.join(sent[i:i+4]) == 'i want to see my':
            if sent[i+5] != 'you' and sent[i+5] != 'me' and sent[i+5] != 'yourself' and sent[i+5] != 'myself' and sent[i+5] != 'about':
                return _open_popular_(' '.join(sent[i+5:]))
        
    popular_list = ['open netflix', 'open amazon', 'open instagram', 'open facebook', 'open whatsapp',
                        'open twitter', 'open pinterest', 'open linkedin', 'open youtube', 'open google', 'open flipkart', 'open coursera'
                   ]
    for n in popular_list:
        if sentence == n:
            sent = sentence.split()
            return _open_popular_(' '.join(sent[1:]))
    
    #-----------------------------Open Folder ----------------------------------
    for i in range(len(sent)-1):
        if ' '.join(sent[i:i+4]) == 'open a folder called' or ' '.join(sent[i:i+4]) == 'open a folder named':
            return _open_folder_(' '.join(sent[i+4:]))
        if ' '.join(sent[i:i+3]) =='open folder named' or ' '.join(sent[i:i+3]) =='open folder called':
            return _open_folder_(' '.join(sent[i+3:]))
        if sent[i] == 'open':
            return _open_folder_(sent[i+1])
        
    return False
