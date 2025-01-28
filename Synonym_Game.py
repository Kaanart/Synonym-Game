#main with UI | test 7 | V8

#Imports
import random 
import time 
from tkinter import *

#Declerations
score = 0

my_dic = {
    'nice':'kind',
    'to mean':'to signify',
    'pretty':'beautiful',
    'long':'extensive',
    'enchanting':'stunning',
    'anger':'infuriate',
    'brave':'courageous',
    'calm':'tranquil',
    'scary':'eerie',
    'eager':'keen',
    
    'like':'admire',
    'smart':'intelligent',
    'predicament':'dilemma',
    'story':'tale',
    'tell (secretive)':'disclose',
    'accurate':'precise',
    'grasp':'seize',
    'idea':'concept',
    'remarkable':'excellent',
    'happy':'delighted',
    
    'use':'utilise',
    'show':'display',
    'explain':'elaborate',
    'angry':'furious',
    'moody':'short-tempered',
    }

my_dic2 = {'sad':'meloncholy',
    'scared':'frightened',
    'bent':'crooked',
    'famous':'renowned',
    'funny':'amusing',
    
    'reveal':'expose',
    'stop (first synonym/second synonym)':'cease/halt',
    'section':'portion',
    'naughty':'mischievous',
    'little (smaller)':'miniature',
    'lazy':'slothful',
    'interesting':'fascinating',
    'hurry':'hasten',
    'hide':'conceal',
    'difference (to differ strikingly)':'contrast',
    
    'incredible':'astonishing',
    'admit':'acknowledge',
    'ask':'inquire',
    'dangerous':'hazardaus',
    'obtain':'acquire',
    'sustain':'maintain',
    'strange':'peculiar',
    'decide':'determine',
    'neat':'dapper',
    'frail':'feeble'}

list_of_picked = []

window = Tk()

global user_txt

#Code

def forbutton():
    btn2['state'] = 'disabled'
    global user_input
    
    user_input = user_txt.get()
    
    user_txt['state'] = 'disabled'
    if user_txt.get() not in list_of_picked:
        list_of_picked.append(a)
    if user_txt.get() == b.get(searchable_a):
        lbl2.config(text ="You got it right! Keep going!", fg='black', font=("Cambria", 24))
        lbl2.place(x=500, y=300)
        time.sleep(0)
        global score
        score += 1
        lbl.config(text=(f'Score: {score}/25'), fg='black', font=("Cambria", 24))
        lbl.place(x=500, y=100)
    elif user_txt.get() != b.get(searchable_a):
        score == 0
        lbl2.config(text=(f"Bzzzzt, correct answer was '{b[searchable_a]}'."), fg='black', font=("Cambria", 24))
        lbl2.place(x=500, y=300)
        lbl.config(text=(f'Score: {score}/25'), fg='black', font=("Cambria", 24))
        lbl.place(x=500, y=100)
        time.sleep(0)
    
    
def mainFunc():   
    btn_for_group.place_forget()
    group_lbl.place_forget()
    user_txt2.place_forget()
    btn.place_forget()
    btn_n_question.place(x=1150, y=500)
    intro_text.place_forget()
    global user_txt
    user_txt = Entry(window, text="This is Entry Widget", bd=5)
    user_txt.place(x=950, y=640)
    user_txt['state'] = 'normal'
    user_txt.focus_set()
    
    global a
    global searchable_a
    a = random.sample(list(my_dic),1) 
    searchable_a = ' '.join(map(str,a))

    global lbl
    lbl = Label(window, text="Kaan's Synonym Game :)", fg='black', font=("Cambria", 24))
    lbl.place(x=870, y=150)

    global lbl2
    lbl2 = Label(window, text=(f"What is the synonym for '{searchable_a}'?"), fg='black', font=("Cambria", 30))
    lbl2.place(x=800, y=300)
    
    global btn2
    btn2 = Button(window, text="Check my Answer!", fg='blue', command = forbutton )
    btn2.place(x=960, y=540)


def next_question_func():
    global a
    global searchable_a
    btn2['state'] = 'normal'
    a = random.sample(list(b),1) 
    searchable_a = ' '.join(map(str,a))
    if len(list_of_picked) == 25:
        btn_n_question.place_forget()
        btn2.place_forget()
        lbl2.config(text=('Congratulations, you have finished your set. To play again or try another group, relaunch.'), fg='black', wraplengt=800, font=("Cambria", 30))
    elif a in list_of_picked:
        while a in list_of_picked:
            a = random.sample(list(b),1) 
            searchable_a = ' '.join(map(str,a))
    if a not in list_of_picked:   
        lbl2.config(text=(f"What is the synonym for '{searchable_a}'?"), fg='black', font=("Cambria", 30))
        lbl2.place(x=800, y=300)
        user_txt['state'] = 'normal'
        user_txt.delete(0, 'end')
    lbl4 = Label(text=(f'{list_of_picked}'),fg='black', font=("Cambria", 12),wraplengt=300)
    lbl4.place(x=100, y=400)
    lbl3.place(x=100, y=300)
    
global btn
intro_text = Label(window, text="Hello dear user, this is a synonym memorising program/game created to help students express themselves better and to of course learn synonyms. Please enjoy! ", fg='black', font=("Cambria", 30), wraplengt=1000)
intro_text.place(x=650, y=150)
btn_n_question = Button(window, text="Next question", fg='blue',height= 6, width=15, command = next_question_func)

def group_func():
    global b
    if user_txt2.get() == '1':
        user_txt2['state'] = 'disabled'
        b = my_dic
        btn.place(x=960, y=540)
    if user_txt2.get() == '2':
        user_txt2['state'] = 'disabled'
        b = my_dic2
        btn.place(x=960, y=540)
    elif user_txt2.get() != '1' or user_txt2.get() != '2':
        group_lbl.config(text=('Please enter either 1 or 2.'), fg='black', font=("Cambria", 20))
    
    
user_txt2 = Entry(window, text="", bd=5)
user_txt2.place(x=100, y=400)

group_lbl = Label(text=('Please select Group 1/2, type 1 or 2. Each group has 25 words which will be asked.'), fg='black', font=("Cambria", 20), wraplengt=400)
group_lbl.place(x=100, y=250)

btn_for_group = Button(window, text="Confirm", fg='blue', command = group_func)
btn_for_group.place(x=100, y=500)

lbl3 = Label(text=('Tried Words:'), fg='black', font=("Cambria", 30))
lbl4 = Label(text=(f'{list_of_picked}'),fg='black', font=("Cambria", 12),wraplengt=300)

btn = Button(window, text="Let's Start!", fg='orange', height= 3, width=15, font=('Cambria', 24), command = mainFunc)
window.title('Synonym Game for Students | PP | Kaan Artun Uysal')
window.geometry("1920x1080+10+10")  #1920,1080 aka resolution
window.mainloop()








