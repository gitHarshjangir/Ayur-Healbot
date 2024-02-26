from tkinter import *
import PIL
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import StringVar, Label, OptionMenu, Button, Text, END, ttk, messagebox
from tkinter import Tk, StringVar, Label, Button, OptionMenu, Text
from tkinter import ttk, messagebox
import numpy as np
import pandas as pd
import subprocess

l1=['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering','chills','joint_pain',
    'stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting','burning_micturition','spotting_ urination','fatigue',
    'weight_gain','anxiety','cold_hands_and_feets','mood_swings','weight_loss','restlessness','lethargy','patches_in_throat',
    'irregular_sugar_level','cough','high_fever','sunken_eyes','breathlessness','sweating','dehydration','indigestion',
    'headache','yellowish_skin','dark_urine','nausea','loss_of_appetite','pain_behind_the_eyes','back_pain','constipation',
    'abdominal_pain','diarrhoea','mild_fever','yellow_urine','yellowing_of_eyes','acute_liver_failure','fluid_overload',
    'swelling_of_stomach','swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
    'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs','fast_heart_rate',
    'pain_during_bowel_movements','pain_in_anal_region','bloody_stool','irritation_in_anus','neck_pain','dizziness','cramps',
    'bruising','obesity','swollen_legs','swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
    'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips','slurred_speech','knee_pain','hip_joint_pain',
    'muscle_weakness','stiff_neck','swelling_joints','movement_stiffness','spinning_movements','loss_of_balance','unsteadiness','weakness_of_one_body_side',
    'loss_of_smell','bladder_discomfort','foul_smell_of urine','continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
    'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain','abnormal_menstruation','dischromic _patches',
    'watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum','rusty_sputum','lack_of_concentration','visual_disturbances',
    'receiving_blood_transfusion','receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen','history_of_alcohol_consumption',
    'fluid_overload','blood_in_sputum','prominent_veins_on_calf','palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
    'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose','yellow_crust_ooze']

disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
        'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
        ' Migraine','Cervical spondylosis',
        'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
'Heart attack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
'Impetigo']

l2=[]
for x in range(0,len(l1)):
    l2.append(0)

# TESTING DATA
tr=pd.read_csv("Testing.csv")
tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

X_test= tr[l1]
y_test = tr[["prognosis"]]
np.ravel(y_test)

# TRAINING DATA
df=pd.read_csv("Training.csv")

df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)


#MAIN 

X= df[l1]

y = df[["prognosis"]]
np.ravel(y)

def message():
    if (Symptom1.get() == "None" and  Symptom2.get() == "None" and Symptom3.get() == "None" and Symptom4.get() == "None" and Symptom5.get() == "None"):
        messagebox.showinfo("OPPS!!", "ENTER  SYMPTOMS PLEASE")
    else :
        NaiveBayes()

def NaiveBayes():
    from sklearn.naive_bayes import MultinomialNB
    gnb = MultinomialNB()
    gnb=gnb.fit(X,np.ravel(y))
    from sklearn.metrics import accuracy_score
    y_pred = gnb.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred, normalize=False))

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = gnb.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(disease[predicted] == disease[a]):
            h='yes'
            break

    if (h=='yes'):
        t3.delete("1.0", END)
        t3.insert(END, disease[a])
    else:
        t3.delete("1.0", END)
        t3.insert(END, "No Disease")



#ROOT FUNCTION



root = tk.Tk()
root.title("Harsh final project")
root.attributes("-fullscreen", True)

image_path = "bg4.png"
image = Image.open(image_path)
resized_image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
photo = ImageTk.PhotoImage(resized_image)
background_label = tk.Label(root, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
background_label.lower()




Symptom1 = StringVar()
Symptom1.set(None)
Symptom2 = StringVar()
Symptom2.set(None)
Symptom3 = StringVar()
Symptom3.set(None)
Symptom4 = StringVar()
Symptom4.set(None)
Symptom5 = StringVar()
Symptom5.set(None)


w2 = tk.Label(root, justify=CENTER, text="Ayur Healbot")
w2.config(font=("ariel", 37))
w2.place(x=555, y=25)

#SYMPTOM LABLE

S1Lb = Label(root, text="Symptom 1")
S1Lb.config(font=("Elephant", 15), bg='orange')
S1Lb.place(x=200, y=200)

S2Lb = Label(root, text="Symptom 2")
S2Lb.config(font=("Elephant", 15), bg='orange')
S2Lb.place(x=400, y=200)

S3Lb = Label(root, text="Symptom 3")
S3Lb.config(font=("Elephant", 15), bg='orange')
S3Lb.place(x=600, y=200)

S4Lb = Label(root, text="Symptom 4")
S4Lb.config(font=("Elephant", 15), bg='orange')
S4Lb.place(x=800, y=200)


S5Lb = Label(root, text="Symptom 5")
S5Lb.config(font=("Elephant", 15), bg='orange')
S5Lb.place(x=1000,y=200)

#OPTION MENU
def filter_options(combo_box, search_text):
    options = combo_box['values']
    filtered_options = [option for option in options if search_text.lower() in option.lower()]
    combo_box['values'] = filtered_options
    combo_box.set('')  # Clear existing selection

def update_symptom_variable(combo_box, symptom_var):
    selected_option = combo_box.get()
    symptom_var.set(selected_option)

def reset_selection(symptom_var, search_var, combo_box):
    symptom_var.set(None)
    search_var.set('')
    combo_box['values'] = OPTIONS
    combo_box.set('')

OPTIONS = sorted(l1)
def set_yellow_background(widget):
    widget.configure(background="orange")
#MENU 1
S1En = OptionMenu(root, Symptom1,*OPTIONS)
S1En.place(x=220, y=237)
set_yellow_background(S1En)

reset_button1 = Button(root, text="R", height=1, width=1, command=lambda: reset_selection(Symptom1, search_var1, S1En))
reset_button1.config(font=("Elephant", 10))
reset_button1.place(x=202, y=276)

search_var1 = tk.StringVar()
search_entry1 = ttk.Entry(root, textvariable=search_var1)
search_entry1.place(x=220, y=265)  # Adjust placement as needed

S1En = ttk.Combobox(root, textvariable=Symptom1, values=OPTIONS)
S1En.place(x=220, y=285)
set_yellow_background(S1En)

search_entry1.bind('<KeyRelease>', lambda event: filter_options(S1En, search_var1.get()))
S1En.bind("<<ComboboxSelected>>", lambda event: update_symptom_variable(S1En, Symptom1))

#MENU 2
S2En = OptionMenu(root, Symptom2,*OPTIONS)
S2En.place(x=420,y=237)
set_yellow_background(S2En)

reset_button2 = Button(root, text="R", height=1, width=1, command=lambda: reset_selection(Symptom2, S2En_search_var, S2En))
reset_button2.config(font=("Elephant", 10))
reset_button2.place(x=402, y=274)

S2En_search_var = tk.StringVar()
S2En_search_entry = ttk.Entry(root, textvariable=S2En_search_var)
S2En_search_entry.place(x=420, y=265)  # Adjust placement as needed

S2En = ttk.Combobox(root, textvariable=Symptom2, values=OPTIONS)
S2En.place(x=420, y=285)
set_yellow_background(S2En)

S2En_search_entry.bind('<KeyRelease>', lambda event: filter_options(S2En, S2En_search_var.get()))
S2En.bind("<<ComboboxSelected>>", lambda event: update_symptom_variable(S2En, Symptom2))


#MENU 3

S3En = OptionMenu(root, Symptom3,*OPTIONS)
S3En.place(x=620,y=237)
set_yellow_background(S3En)

reset_button3 = Button(root, text="R", height=1, width=1, command=lambda: reset_selection(Symptom3, S3En_search_var, S3En))
reset_button3.config(font=("Elephant", 10))
reset_button3.place(x=602, y=274)

S3En_search_var = tk.StringVar()
S3En_search_entry = ttk.Entry(root, textvariable=S3En_search_var)
S3En_search_entry.place(x=620, y=265)  # Adjust placement as needed

S3En = ttk.Combobox(root, textvariable=Symptom3, values=OPTIONS)
S3En.place(x=620, y=285)
set_yellow_background(S3En)

S3En_search_entry.bind('<KeyRelease>', lambda event: filter_options(S3En, S3En_search_var.get()))
S3En.bind("<<ComboboxSelected>>", lambda event: update_symptom_variable(S3En, Symptom3))

#MENU 4

S4En = OptionMenu(root, Symptom4,*OPTIONS)
S4En.place(x=820 ,y=237)
set_yellow_background(S4En)

reset_button4 = Button(root, text="R", height=1, width=1, command=lambda: reset_selection(Symptom4, S4En_search_var, S4En))
reset_button4.config(font=("Elephant", 10))
reset_button4.place(x=802, y=274)

S4En_search_var = tk.StringVar()
S4En_search_entry = ttk.Entry(root, textvariable=S4En_search_var)
S4En_search_entry.place(x=820, y=265)  # Adjust placement as needed

S4En = ttk.Combobox(root, textvariable=Symptom4, values=OPTIONS)
S4En.place(x=820, y=285)
set_yellow_background(S4En)

S4En_search_entry.bind('<KeyRelease>', lambda event: filter_options(S4En, S4En_search_var.get()))
S4En.bind("<<ComboboxSelected>>", lambda event: update_symptom_variable(S4En, Symptom4))

#MENU 5
S5En = OptionMenu(root, Symptom5,*OPTIONS)
S5En.place(x=1020, y=237)
set_yellow_background(S5En)

reset_button5 = Button(root, text="R", height=1, width=1, command=lambda: reset_selection(Symptom5, S5En_search_var, S5En))
reset_button5.config(font=("Elephant", 10))
reset_button5.place(x=1002, y=274)

S5En_search_var = tk.StringVar()
S5En_search_entry = ttk.Entry(root, textvariable=S5En_search_var)
S5En_search_entry.place(x=1020, y=265) 

S5En = ttk.Combobox(root, textvariable=Symptom5, values=OPTIONS)
S5En.place(x=1020, y=285)
set_yellow_background(S5En)

S5En_search_entry.bind('<KeyRelease>', lambda event: filter_options(S5En, S5En_search_var.get()))
S5En.bind("<<ComboboxSelected>>", lambda event: update_symptom_variable(S5En, Symptom5))

# Function to reset the selections
def set_yellow_background(widget):
    widget.configure(background="green")
def reset_selections():
    Symptom1.set(None)
    Symptom2.set(None)
    Symptom3.set(None)
    Symptom4.set(None)
    Symptom5.set(None)
    t3.delete("1.0", END)

    # Clear search entries
    search_var1.set('')
    S2En_search_var.set('')
    S3En_search_var.set('')
    S4En_search_var.set('')
    S5En_search_var.set('')

    # Clear OptionMenu values
    S1En['values'] = OPTIONS
    S2En['values'] = OPTIONS
    S3En['values'] = OPTIONS
    S4En['values'] = OPTIONS
    S5En['values'] = OPTIONS

    # Clear ComboBox values
    S1En['values'] = OPTIONS
    S2En['values'] = OPTIONS
    S3En['values'] = OPTIONS
    S4En['values'] = OPTIONS
    S5En['values'] = OPTIONS

# BUTTONS

# Reset button
reset_button = Button(root, text="Reset", height=2, width=10, command=reset_selections)
reset_button.config(font=("Elephant", 15))
reset_button.place(x=990, y=450)
set_yellow_background(reset_button)






def set_green_background(widget):
    widget.configure(bg="white")

#BUTTONS

lr = Button(root, text="Disease",height=2, width=10, command=message)
lr.config(font=("Elephant", 15))
lr.place(x=200, y= 350)


def open_runprogram():
    subprocess.Popen(['python', 'med.py'])

#Exit Button 
    
def exit_program():
    root.destroy()



bot_button = Button(root, text="MEDICINE", height=2, width=10, command=open_runprogram)
bot_button.config(font=("Elephant", 15), bg="Green")
bot_button.place(x=200, y=450)


t3 = Text(root, height=2, width=30, wrap=WORD)  
t3.config(font=("Elephant", 15))
t3.place(x=450, y=350)  



set_green_background(t3)


def exit_program():
    result = messagebox.askyesno("Exit Program", "Are you sure you want to exit?")
    if result:
        root.destroy()

# BUTTONS
# ... (Previous code)

# Exit button
def set_pink_background(widget):
    widget.configure(bg="green")

exit_button = Button(root, text="Exit", height=2, width=10, command=exit_program)
exit_button.config(font=("Elephant", 15), bg="green")
exit_button.place(x=550, y=450)
set_pink_background(exit_button)


root.mainloop()