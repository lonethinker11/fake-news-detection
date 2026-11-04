# -------------- making the dataset json from trainset ------------------------------------------------------------------
# ------------------------------++++++++++++++++++++++++++++++++++++++++++++++++++


import json

with open('train.json','r') as file:
    p_dataset = json.load(file)

d = {}

for datas in range(len(p_dataset)):
    item = p_dataset[datas]                                 #  <-------------- one dictionary int the list is item
    if 'claim' in item:
        claim = item['claim']
    if 'justification' in item:
        justification = item['justification']
    if 'questions' in item:
        questions = item['questions']                       #  <-------------- value of questions key , i.e the list 
    e = [item['required_reannotation'],f"Evidence :- {justification} , "]
                                                                     

    for things in range(len(questions)):
        if 'answers' in questions[things]:                  
            evidence_list =  questions[things]['answers']
            for i in range(len(evidence_list)):
                if 'boolean_explanation' in evidence_list[i]:
                    e[1]+=f"{evidence_list[i]['boolean_explanation']} , "
                else:
                    e[1]+=f"{evidence_list[i]['answer']} , "

                

    d[f"claim :- {claim} , "] = e

with open('dataset.json','w') as file:
    json.dump(d,file,indent=4)


#---------------------------------------- making the dataset csv ---------------------------------------------------
# ------------------+++++++++++++++++++++++++

import pandas as pd

with open('dataset.json','r') as file:
    dataset = json.load(file)

df = pd.DataFrame(columns=['text','label'])

text = []
label = []

for datas in dataset:
    item = dataset[datas]
    text.append(datas+item[1])
    label.append(item[0])

df['text'] = text
df['label'] = label

df.to_csv('dataset.csv',index = False)