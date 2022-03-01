import random
from test import words
def remove_char(ch,pa):
    wrd = []
    for word in pa:
         if ch not in word:
             wrd.append(word)
    return wrd
def remove_char2(ch,pa):
    wrd = []
    for word in pa:
         if ch in word:
             wrd.append(word)
    return wrd
def rem3(letter,pos,pa):
    wrd=[]
    for word in pa:
        if word[pos] ==letter:
           wrd.append(word)
    return wrd
def guess(guess_word,answer,possible_answers):
    if answer == guess_word:
        print("Yay you found the answer!!")
        return []
    # print(possible_answers)
    #check if guess is a valid word
    if guess_word in words :
        #taking letters from guess
        for letter in guess_word:
            #print(len(possible_answers))
            #print(possible_answers)
            #the letter is in answer
            if letter in answer:
                possible_answers = remove_char2(letter,possible_answers)
                pos = guess_word.index(letter)
                # the letter is correctly placed
                if letter == answer[pos]:
                    possible_answers=rem3(letter,pos,possible_answers)
            # letter not in answer
            else:
                possible_answers=remove_char(letter,possible_answers)
            #print(possible_answers)
    else :
        print("NOT a Valid Word")
    return possible_answers

answer= random.choice(words)
flag =1
possible_ans = words
while possible_ans !=[]:
    user_guess=input("enter guess : ")
    possible_ans = guess(user_guess,answer,possible_ans)
    print(possible_ans)