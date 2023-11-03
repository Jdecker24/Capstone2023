### 0% NA's training data





#-----------------Outbursts(DMDD)---------------------------

import numpy as np
import pandas as pd
import openai

openai.api_key = str(np.loadtxt("/Users/jdec0124/Desktop/apikey.txt", dtype=str))
traindata=pd.read_csv("train_data.csv")


for subject in traindata.index[:29]:
    age_answer = traindata.loc[subject,"min_age"]
    sex_answer = traindata.loc[subject,"SEX"]
    
    angry_irrit_mood_choices = ["never", "occasionally", "once or twice a week", "three or more times a week", "every day"]
    angry_irrit_answer = traindata.loc[subject,"s_dmdd_1_frequency_irritable_angry_mood"]
    easily_irrit_dict = {
       "no" : "not easily irritated",
       "a little" : "easily irritated a little",
       "a lot" : "easily irritated a lot"
    }
    easily_irrit_choices = ["no", "a little", "a lot"]
    intensely_irrit_choices = easily_irrit_choices

    easily_irrit_answer = traindata.loc[subject,"s_dmdd_8_easily_irritated"]
    intensely_irrit_answer = traindata.loc[subject,"s_dmdd_9_intense_irritability"]

    intensely_irrit_dict = {
       "no" : "don't experience intense irritability",
       "a little" : "experience intense irritability a little",
       "a lot" : "experience intense irritability a lot"
    }
       
    content = "Below are the responses of a youth on a psychological questionnaire. They are a " + str(age_answer)
    content = content + " year old " + sex_answer
    content = content + ". They have an angry/irritable mood " + angry_irrit_answer
    content = content + ". They are " + easily_irrit_dict[easily_irrit_answer]
    content = content + ". They " + intensely_irrit_dict[intensely_irrit_answer]
    content = content + ".  Given these responses, what are the frequency of outbursts? Please respond with \"never\", \"occasionally\", \"once or twice a week\", \"three or more times a week\", \"every day\". Limit response to 10 words."



    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": content
                }
            ],
        temperature=1,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
         )


    answer = response["choices"][0]["message"]["content"]
    traindata.loc[subject,"openai_answer5"]= answer

    

#remove capitalization and punctuation
import re
def remove_caps_and_punct(text):
     text = text.lower()
     text = re.sub(r'[^\w\s]', '', text)
     return text

traindata['openai_answer5'] = traindata['openai_answer5'].apply(remove_caps_and_punct)


#create a subset of specified columns
columns = ['s_dmdd_2_frequency_outbursts', 'openai_answer', 'openai_answer2', 'openai_answer3', 'openai_answer4', 'openai_answer5']
subset = traindata[columns]
subset

columns = ['s_dmdd_2_frequency_outbursts', 'openai_answer']
subset = traindata[columns]
subset


#create a column that is the majority.
columns = ['openai_answer', 'openai_answer2', 'openai_answer3', 'openai_answer4', 'openai_answer5']
traindata['openai_final_answer'] = traindata[columns].mode(axis=1).iloc[:, 0]



#let's look at the percentage os openai response that matches the youth
same_vals = (traindata['s_dmdd_2_frequency_outbursts'] == traindata['openai_final_answer']).sum()
rows = len(traindata)
percentage = (same_vals / rows) * 100
percentage
# we got 31.03% correct openai response

#save csv
traindata.to_csv("openai_traindata_OutburstsDMDD5.csv")


#------------Using the gpt 4 model---------------- (Ran into an issue here gave me output that had nothing to do with our data)

    response = openai.ChatCompletion.create(
      model="gpt-4",
      messages=[
        {
          "role": "user",
          "content": ""
        }
      ],
      temperature=1,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
)
 
 
    answer = response["choices"][0]["message"]["content"]
    traindata.loc[subject,"openai_answer1"]= answer

#remove capitalization and punctuation
import re
def remove_caps_and_punct(text):
     text = text.lower()
     text = re.sub(r'[^\w\s]', '', text)
     return text

traindata['openai_answer'] = traindata['openai_answer'].apply(remove_caps_and_punct)

#looking at a subset
columns = ['s_dmdd_2_frequency_outbursts', 'openai_answer']
subset = traindata[columns]
subset


#let's look at the percentage os openai response that matches the youth
same_vals = (traindata['s_dmdd_2_frequency_outbursts'] == traindata['openai_answer']).sum()
rows = len(traindata)
percentage = (same_vals / rows) * 100
percentage
# we got 34.48% correct openai response     (3% increase from no explanation best out of 5)

#save csv
traindata.to_csv("openai_traindata_OutburstsDMDDgpt4.csv")


#------------using the explanations----------------

    content = "Below are the responses of a youth on a psychological questionnaire. They are a " + str(age_answer)
    content = content + " year old " + sex_answer
    content = content + ". They have an angry/irritable mood " + angry_irrit_answer
    content = content + ". They are " + easily_irrit_dict[easily_irrit_answer]
    content = content + ". They " + intensely_irrit_dict[intensely_irrit_answer]
    content = content + ".  Given these responses, what are the frequency of outbursts? Please respond in two sentences. In the first sentence respond with \"never\", \"occasionally\", \"once or twice a week\", \"three or more times a week\", \"every day\". Limit first sentence to 7 words. In the second sentence give your explanation."



    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": content
                }
            ],
        temperature=1,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
         )

    answer = response["choices"][0]["message"]["content"]
    segments = answer.split('.')


    traindata.loc[subject, "openai_answer"] = segments[0].strip()
    traindata.loc[subject, "openai_answer_explanation"] = segments[1].strip()




#remove capitalization and punctuation
import re
def remove_caps_and_punct(text):
     text = text.lower()
     text = re.sub(r'[^\w\s]', '', text)
     return text

traindata['openai_answer'] = traindata['openai_answer'].apply(remove_caps_and_punct)

#looking at a subset
columns = ['s_dmdd_2_frequency_outbursts', 'openai_answer']
subset = traindata[columns]
subset


#let's look at the percentage os openai response that matches the youth
same_vals = (traindata['s_dmdd_2_frequency_outbursts'] == traindata['openai_answer']).sum()
rows = len(traindata)
percentage = (same_vals / rows) * 100
percentage
# we got 34.48% correct openai response     (3% increase from no explanation best out of 5)

#save csv
traindata.to_csv("openai_traindata_OutburstsDMDDexplain.csv")



#-----------------------------------------------------------------------------







    



#--------------Irritability(Dep)-----------------------------------------

import numpy as np
import pandas as pd
import openai
openai.api_key = str(np.loadtxt("/Users/jdec0124/Desktop/apikey.txt", dtype=str))

traindata=pd.read_csv("train_data.csv")

for subject in traindata.index[:29]:
    age_answer = traindata.loc[subject,"min_age"]
    sex_answer = traindata.loc[subject,"SEX"]
     
    irrit_exp_dict = {
        "yes" : "experience irritability.",
        "no" : "don't experience irritability."
    }
 
    irrit_exp_choices = ["yes", "no"]
    irrit_exp_answer = traindata.loc[subject,"s_dep_7_irritable"]
 
    daily_irrit_dict = {
        "yes" : "irritable daily.",
        "no" : "not irritable daily."
    }
 
 
    daily_irrit_choices = irrit_exp_choices
    daily_irrit_answer = traindata.loc[subject,"s_dep_8_irritable_daily"]
 
    most_irrit_dict = {
        "yes" : "irritable most of the time.",
        "no" : "not irritable most of the time."
    }
 
    most_irrit_choices = irrit_exp_choices
    most_irrit_answer = traindata.loc[subject,"s_dep_9_irratable_mostly"]
 
    friends_imp_dict = {
        "easily" : "easily.",
        "with difficulty/only briefly" : "only briefly and with difficulty.",
        "not at all" : "not at all."
    }
 
    friends_imp_choices = ["easily", "with difficulty/only briefly", "not at all"]
    friends_imp_answer = traindata.loc[subject,"s_dep_10_irritable_improved"]
 
  
    content = "Below are the responses of a youth on a psychological questionnaire. They are a " + str(age_answer)
    content = content + " year old " + sex_answer
    content = content + " They " + irrit_exp_dict[irrit_exp_answer]
    content = content + " They are " + daily_irrit_dict[daily_irrit_answer]
    content = content + " They are " + most_irrit_dict[most_irrit_answer]
    content = content + " Their irritability is improved by friends " + friends_imp_dict[friends_imp_answer]
    content = content + "How long of a duration are they irritable? Please only respond with \"less than 2 weeks\" or \"2 weeks or  more\". Limit response to 5 words."
 
    response = openai.ChatCompletion.create(
       model="gpt-3.5-turbo",
       messages=[
         {
           "role": "user",
           "content": content
         }
       ],
       temperature=1,
       max_tokens=1000,
        top_p=1,
       frequency_penalty=0,
       presence_penalty=0
     )
 
 
    answer = response["choices"][0]["message"]["content"]
    traindata.loc[subject,"openai_answer1"]= answer


#remove capitalization and punctuation
import re
def remove_caps_and_punct(text):
     text = text.lower()
     text = re.sub(r'[^\w\s]', '', text)
     return text

traindata['openai_answer'] = traindata['openai_answer'].apply(remove_caps_and_punct)


#create a subset of specified columns
columns = ['s_dep_11_irritable_duration', 'openai_answer', 'openai_answer2', 'openai_answer3', 'openai_answer4', 'openai_answer5']
subset = traindata[columns]
subset

columns = ['s_dep_11_irritable_duration', 'openai_answer']
subset = traindata[columns]
subset


#create a column that is the majority.
columns = ['openai_answer', 'openai_answer2', 'openai_answer3', 'openai_answer4', 'openai_answer5']
traindata['openai_final_answer'] = traindata[columns].mode(axis=1).iloc[:, 0]



#let's look at the percentage os openai response that matches the youth
same_vals = (traindata['s_dep_11_irritable_duration'] == traindata['openai_final_answer']).sum()
rows = len(traindata)
percentage = (same_vals / rows) * 100
percentage
# we got 51.72% correct openai response

#save csv
traindata.to_csv("openai_traindata_IrritibilityDepExplain.csv")



#-----------Using gpt 4 instead---------------

    response = openai.ChatCompletion.create(
      model="gpt-4",
      messages=[
        {
          "role": "user",
          "content": ""
        }
      ],
      temperature=1,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
)
 
 
    answer = response["choices"][0]["message"]["content"]
    traindata.loc[subject,"openai_answer1"]= answer


#---------Using explanations-----------------
 
    content = "Below are the responses of a youth on a psychological questionnaire. They are a " + str(age_answer)
    content = content + " year old " + sex_answer
    content = content + " They " + irrit_exp_dict[irrit_exp_answer]
    content = content + " They are " + daily_irrit_dict[daily_irrit_answer]
    content = content + " They are " + most_irrit_dict[most_irrit_answer]
    content = content + " Their irritability is improved by friends " + friends_imp_dict[friends_imp_answer]
    content = content + "How long of a duration are they irritable? Please respond with only two sentences. In the first sentence only respond with \"less than 2 weeks\" or \"2 weeks or more\". Limit first sentence to 4 words. In the second sentence please give your explination."

     
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {
          "role": "user",
          "content": content
        }
      ],
      temperature=1,
      max_tokens=1000,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    answer = response["choices"][0]["message"]["content"]
    segments = answer.split('.')


    traindata.loc[subject, "openai_answer"] = segments[0].strip()
    traindata.loc[subject, "openai_answer_explanation"] = segments[1].strip()




#remove capitalization and punctuation
import re
def remove_caps_and_punct(text):
     text = text.lower()
     text = re.sub(r'[^\w\s]', '', text)
     return text

traindata['openai_answer'] = traindata['openai_answer'].apply(remove_caps_and_punct)

#let's look at the percentage os openai response that matches the youth
same_vals = (traindata['s_dep_11_irritable_duration'] == traindata['openai_answer']).sum()
rows = len(traindata)
percentage = (same_vals / rows) * 100
percentage
# we got 44.83% correct openai response           (about a 7% decrease from the best out of 5 and no expl.)

#save csv
traindata.to_csv("openai_traindata_IrritibilityDep5.csv")

    

#-----------------------------------------------------------------------------------------





    


#------------Distress(Dep)-------------------------------------------
import numpy as np
import pandas as pd
import openai
openai.api_key = str(np.loadtxt("/Users/jdec0124/Desktop/apikey.txt", dtype=str))

traindata=pd.read_csv("train_data.csv")

for subject in traindata.index[:29]:
    age_answer = traindata.loc[subject,"min_age"]
    sex_answer = traindata.loc[subject,"SEX"]
    
    sad_dep_dict = {
        "yes" : " They have ",
        "no" : " They have not "
        }
    sad_dep_choices = ["yes", "no"]
    sad_dep_answer = traindata.loc[subject,"s_dep_1_sad"]

    misdaily_dep_dict = {
        "yes" : " There was ",
        "no" : " There was not "
        }
    misdaily_dep_choices = sad_dep_choices
    misdaily_dep_answer = traindata.loc[subject,"s_dep_2_miserable_daily"]

    mismostly_dep_dict = {
        "yes" : "was for most of the day. ",
        "no" : "was not for most of the day. "
        }
    mismostly_dep_choices = sad_dep_choices
    mismostly_dep_answer = traindata.loc[subject,"s_dep_3_miserable_mostly"]

    irrit_dep_dict = sad_dep_dict
    irrit_dep_choices = sad_dep_choices
    irrit_dep_answer = traindata.loc[subject,"s_dep_7_irritable"]

    irritdaily_dep_dict = misdaily_dep_dict
    irritdaily_dep_choices = sad_dep_choices
    irritdaily_dep_answer = traindata.loc[subject,"s_dep_8_irritable_daily"]

    irritmostly_dep_dict = mismostly_dep_dict
    irritmostly_dep_choices = sad_dep_choices
    irritmostly_dep_answer = traindata.loc[subject,"s_dep_9_irratable_mostly"]

    anh_dep_dict = sad_dep_dict
    anh_dep_choices = sad_dep_choices
    anh_dep_answer = traindata.loc[subject,"s_dep_13_anhedonia"]

    anhdaily_dep_dict = misdaily_dep_dict
    anhdaily_dep_choices = sad_dep_choices
    anhdaily_dep_answer = traindata.loc[subject,"s_dep_14_anhedonia_daily"]

    anhmostly_dep_dict = mismostly_dep_dict
    anhmostly_dep_choices = sad_dep_choices
    anhmostly_dep_answer = traindata.loc[subject,"s_dep_15_anhedonia_mostly"]

    tired_dep_dict = {
        "yes" : " they did ",
        "no" : " they did not "
        }
    tired_dep_choices = ["yes", "no"]
    tired_dep_answer = traindata.loc[subject,"s_dep_18a_tired"]

    appetite_dep_dict = tired_dep_dict
    appetite_dep_choices = tired_dep_choices
    appetite_dep_answer = traindata.loc[subject,"s_dep_18b_appetite"] 

    weight_dep_dict = tired_dep_dict
    weight_dep_choices = tired_dep_choices
    weight_dep_answer = traindata.loc[subject,"s_dep_18c_weight"]

    insomnia_dep_dict = tired_dep_dict
    insomnia_dep_choices = tired_dep_choices
    insomnia_dep_answer = traindata.loc[subject,"s_dep_18d_insomnia"]

    hypersom_dep_dict = tired_dep_dict
    hypersom_dep_choices = tired_dep_choices
    hypersom_dep_answer = traindata.loc[subject,"s_dep_18e_hypersomnia"]

    agitat_dep_dict = tired_dep_dict
    agitat_dep_choices = tired_dep_choices
    agitat_dep_answer = traindata.loc[subject,"s_dep_18f_agitation"]

    worth_dep_dict = tired_dep_dict
    worth_dep_choices = tired_dep_choices
    worth_dep_answer = traindata.loc[subject,"s_dep_18g_worthless"]

    concen_dep_dict = tired_dep_dict
    concen_dep_choices = tired_dep_choices
    concen_dep_answer = traindata.loc[subject,"s_dep_18h_concentration"]

  
    sadduration_dep_choices = ["less than 2 weeks", "2 weeks or more"]
    sadduration_dep_answer = traindata.loc[subject,"s_dep_5_miserable_duration"]

    irritduration_dep_choices = sadduration_dep_choices
    irritduration_dep_answer = traindata.loc[subject,"s_dep_11_irritable_duration"]

    anhduration_dep_choices = sadduration_dep_choices
    anhduration_dep_answer = traindata.loc[subject,"s_dep_16_anhedonia_duration"]

    family_dep_choices = ["not at all", "a little", "a medium amount", "a great deal"]
    family_dep_answer = traindata.loc[subject,"s_dep_20a_impact_family"]

    friend_dep_choices = family_dep_choices
    friend_dep_answer = traindata.loc[subject,"s_dep_20b_impact_friendships"]

    school_dep_choices = family_dep_choices
    school_dep_answer = traindata.loc[subject,"s_dep_20c_impact_school_work"]

    leisure_dep_choices = family_dep_choices
    leisure_dep_answer = traindata.loc[subject,"s_dep_20d_impact_leisure"]


    irritimprove_dep_choices = ["easily", "with difficulty/only briefly", "not at all"]
    irritimprove_dep_answer = traindata.loc[subject,"s_dep_10_irritable_improved"]

    irritimprove_dep_choices = irritimprove_dep_choices
    irritimprove_dep_answer = traindata.loc[subject,"s_dep_4_miserable_cheered_up"]
    

    content = "Below are the responses of a youth on a psychological questionnaire. They are a " + str(age_answer) 
    content = content + " year old " + sex_answer
    content = content + sad_dep_dict[sad_dep_answer] + "experienced sadness within the past 4 weeks."
    content = content + misdaily_dep_dict[misdaily_dep_answer] + "a period of time within the past 4 weeks where they were miserable daily."
    content = content + " When they were miserable, it " + mismostly_dep_dict[mismostly_dep_answer]
    content = content + irrit_dep_dict[sad_dep_answer] + "experienced irritability within the past 4 weeks."
    content = content + irritdaily_dep_dict[irritdaily_dep_answer] + "a period of time within the past 4 weeks where they were irritable daily."
    content = content + " When they were irritable, it " + irritmostly_dep_dict[irritmostly_dep_answer]
    content = content + anh_dep_dict[anh_dep_answer] + "experienced anhedonia within the past 4 weeks."
    content = content + anhdaily_dep_dict[anhdaily_dep_answer] + "a period of time within the past 4 weeks where they experienced anhedonia daily."
    content = content + " When they experience anhedonia, it " + irritmostly_dep_dict[irritmostly_dep_answer]
    content = content + " During the period when they were sad, irritable or lacked interest " + tired_dep_dict[tired_dep_answer] + "feel tired all the time,"
    content = content + appetite_dep_dict[appetite_dep_answer] + "experience a change in appetite,"
    content = content + weight_dep_dict[weight_dep_answer] + "have a big change in weight,"
    content = content + insomnia_dep_dict[insomnia_dep_answer] + "have trouble falling and staying asleep,"
    content = content + hypersom_dep_dict[hypersom_dep_answer] + "sleep too much,"
    content = content + agitat_dep_dict[agitat_dep_answer] + "feel agitated for much of the time,"
    content = content + worth_dep_dict[worth_dep_answer] + "feel worthless much of the time, and "
    content = content + concen_dep_dict[concen_dep_answer] + "find it unusually hard to to concentrate."
    content = content + " During the past 4 weeks their period of sadness lasted " + sadduration_dep_answer
    content = content + ". During the past 4 weeks their period of irritability lasted " + irritduration_dep_answer
    content = content + ". During the past 4 weeks their period of anhedonia lasted " + anhduration_dep_answer
    content = content + ". When they were sad, irritable or lacked interest it impacted their relationship with family " + family_dep_answer
    content = content + ", with making and keeping friends " + friend_dep_answer
    content = content + ", their school work " + school_dep_answer
    content = content + ", and their leisure activities " + leisure_dep_answer
    content = content + ". Their irritability is improved by friends and activities " + irritimprove_dep_answer
    content = content + ". They are cheered up " + irritimprove_dep_answer + " when miserable."
    content = content + " Given this information, how much has their sadness, irritability or loss of interest upset or distressed them? Please respond with \"not at all\", \"a little\", \"a medium amount\", or \"a great deal\". Limit response to 4 words."

    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {
          "role": "user",
          "content": content
        }
      ],
      temperature=1,
      max_tokens=1000,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )


    answer = response["choices"][0]["message"]["content"]
    traindata.loc[subject,"openai_answer5"]= answer


#remove capitalization and punctuation
import re
def remove_caps_and_punct(text):
     text = text.lower()
     text = re.sub(r'[^\w\s]', '', text)
     return text

traindata['openai_answer5'] = traindata['openai_answer5'].apply(remove_caps_and_punct)


#create a subset of specified columns
columns = ['s_dep_19_distress', 'openai_answer', 'openai_answer2', 'openai_answer3', 'openai_answer4', 'openai_answer5']
subset = traindata[columns]
subset

columns = ['s_dep_19_distress', 'openai_answer']
subset = traindata[columns]
subset


#create a column that is the majority.
columns = ['openai_answer', 'openai_answer2', 'openai_answer3', 'openai_answer4', 'openai_answer5']
traindata['openai_final_answer'] = traindata[columns].mode(axis=1).iloc[:, 0]



#let's look at the percentage os openai response that matches the youth
same_vals = (traindata['s_dep_19_distress'] == traindata['openai_final_answer']).sum()
rows = len(traindata)
percentage = (same_vals / rows) * 100
percentage
# we got 68.97% correct openai response

#save csv
traindata.to_csv("openai_traindata_DepDistress.csv")


#-------------------Using thge gpt 4 model-------------------

    response = openai.ChatCompletion.create(
      model="gpt-4",
      messages=[
        {
          "role": "user",
          "content": content
        }
      ],
      temperature=1,
      max_tokens=1000,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )


    answer = response["choices"][0]["message"]["content"]
    traindata.loc[subject,"openai_answer5"]= answer


#-------------------Using explanation ending instead----------------------

    content = "Below are the responses of a youth on a psychological questionnaire. They are a " + str(age_answer) 
    content = content + " year old " + sex_answer
    content = content + sad_dep_dict[sad_dep_answer] + "experienced sadness within the past 4 weeks."
    content = content + misdaily_dep_dict[misdaily_dep_answer] + "a period of time within the past 4 weeks where they were miserable daily."
    content = content + " When they were miserable, it " + mismostly_dep_dict[mismostly_dep_answer]
    content = content + irrit_dep_dict[sad_dep_answer] + "experienced irritability within the past 4 weeks."
    content = content + irritdaily_dep_dict[irritdaily_dep_answer] + "a period of time within the past 4 weeks where they were irritable daily."
    content = content + " When they were irritable, it " + irritmostly_dep_dict[irritmostly_dep_answer]
    content = content + anh_dep_dict[anh_dep_answer] + "experienced anhedonia within the past 4 weeks."
    content = content + anhdaily_dep_dict[anhdaily_dep_answer] + "a period of time within the past 4 weeks where they experienced anhedonia daily."
    content = content + " When they experience anhedonia, it " + irritmostly_dep_dict[irritmostly_dep_answer]
    content = content + " During the period when they were sad, irritable or lacked interest " + tired_dep_dict[tired_dep_answer] + "feel tired all the time,"
    content = content + appetite_dep_dict[appetite_dep_answer] + "experience a change in appetite,"
    content = content + weight_dep_dict[weight_dep_answer] + "have a big change in weight,"
    content = content + insomnia_dep_dict[insomnia_dep_answer] + "have trouble falling and staying asleep,"
    content = content + hypersom_dep_dict[hypersom_dep_answer] + "sleep too much,"
    content = content + agitat_dep_dict[agitat_dep_answer] + "feel agitated for much of the time,"
    content = content + worth_dep_dict[worth_dep_answer] + "feel worthless much of the time, and "
    content = content + concen_dep_dict[concen_dep_answer] + "find it unusually hard to to concentrate."
    content = content + " During the past 4 weeks their period of sadness lasted " + sadduration_dep_answer
    content = content + ". During the past 4 weeks their period of irritability lasted " + irritduration_dep_answer
    content = content + ". During the past 4 weeks their period of anhedonia lasted " + anhduration_dep_answer
    content = content + ". When they were sad, irritable or lacked interest it impacted their relationship with family " + family_dep_answer
    content = content + ", with making and keeping friends " + friend_dep_answer
    content = content + ", their school work " + school_dep_answer
    content = content + ", and their leisure activities " + leisure_dep_answer
    content = content + ". Their irritability is improved by friends and activities " + irritimprove_dep_answer
    content = content + ". They are cheered up " + irritimprove_dep_answer + " when miserable."
    content = content + " Given this information, how much has their sadness, irritability or loss of interest upset or distressed them? Respond with 2 lines. Please respond in the first line with \"not at all\", \"a little\", \"a medium amount\", or \"a great deal\" only. In the second line give your explanation. Limit first line to only 3 words"

    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {
          "role": "user",
          "content": content
        }
      ],
      temperature=1,
      max_tokens=1000,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    answer = response["choices"][0]["message"]["content"]
    segments = answer.split('.')


    traindata.loc[subject, "openai_answer"] = segments[0].strip()
    traindata.loc[subject, "openai_answer_explanation"] = segments[1].strip()


#---------------------------------------------------------------------------------------











#------------------------------Worry(gad)-----------------------------



import numpy as np
import pandas as pd
import openai
openai.api_key = str(np.loadtxt("/Users/jdec0124/Desktop/apikey.txt", dtype=str))

traindata=pd.read_csv("train_data.csv")

for subject in traindata.index[:29]:
    age_answer = traindata.loc[subject,"min_age"]
    sex_answer = traindata.loc[subject,"SEX"]
    

    past_gad_choices = ["no more than others", "a little more than others", "a lot more than others"]
    past_gad_answer = traindata.loc[subject,"s_gad_4a_past_behaviour"]

    school_gad_choices = past_gad_choices
    school_gad_answer = traindata.loc[subject,"s_gad_4b_school_work"]

    disaster_gad_choices = past_gad_choices
    disaster_gad_answer = traindata.loc[subject,"s_gad_4c_disasters_accidents"]

    health_gad_choices = past_gad_choices
    health_gad_answer = traindata.loc[subject,"s_gad_4d_own_health"]

    badthings_gad_choices = past_gad_choices
    badthings_gad_answer = traindata.loc[subject,"s_gad_4e_bad_things_others"]

    future_gad_choices = past_gad_choices
    future_gad_answer = traindata.loc[subject,"s_gad_4f_the_future"]

    friends_gad_choices = past_gad_choices
    friends_gad_answer = traindata.loc[subject,"s_gad_4g_keeping_friends"]

    death_gad_choices = past_gad_choices
    death_gad_answer = traindata.loc[subject,"s_gad_4h_death"]

    bullied_gad_choices = past_gad_choices
    bullied_gad_answer = traindata.loc[subject,"s_gad_4i_bullied"]

    weight_gad_choices = past_gad_choices
    weight_gad_answer = traindata.loc[subject,"s_gad_4j_appearance_weight"]

    mostdays_gad_dict = {
        "yes" : ". They were ",
        "no" : ". They were not "
        }
    mostdays_gad_choices = ["yes", "no"]
    mostdays_gad_answer = traindata.loc[subject,"s_gad_6_worried_most_days"]

    control_gad_dict = {
        "yes" : ". It was ",
        "no" : ". It was not "
        }
    control_gad_choices = mostdays_gad_choices
    control_gad_answer = traindata.loc[subject,"s_gad_7_worry_difficult_control"]

    content = "Below are the responses of a youth on a psychological questionnaire. They are a " + str(age_answer) 
    content = content + " year old " + sex_answer
    content = content + ". They worry about their past behavior " + past_gad_answer
    content = content + ". They worry about school and examinations " + school_gad_answer
    content = content + ". They worry about disasters and accidents " + disaster_gad_answer
    content = content + ". They worry about their own health " + health_gad_answer
    content = content + ". They worry about bad things happening " + badthings_gad_answer
    content = content + ". They worry about the future " + future_gad_answer
    content = content + ". They worry about making and keeping friends " + friends_gad_answer
    content = content + ". They worry about death and dying " + death_gad_answer
    content = content + ". They worry about being bullied and teased " + bullied_gad_answer
    content = content + ". They worry about their weight and appearance " + weight_gad_answer
    content = content + mostdays_gad_dict[mostdays_gad_answer] + "worried on most days in the last 6 months"
    content = content + control_gad_dict[control_gad_answer] + "easy to control their worryness."
    content = content + "Given this information, do they excessively worry? You must only respond with \"not\", \"perhaps\", or \"definitely\". Limit response to 1 word."

    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {
          "role": "user",
          "content": content
        }
      ],
      temperature=1,
      max_tokens=1000,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )


    answer = response["choices"][0]["message"]["content"]
    traindata.loc[subject,"openai_answer5"]= answer


#remove capitalization and punctuation
import re
def remove_caps_and_punct(text):
     text = text.lower()
     text = re.sub(r'[^\w\s]', '', text)
     return text

traindata['openai_answer5'] = traindata['openai_answer5'].apply(remove_caps_and_punct)


#create a subset of specified columns
columns = ['s_gad_3_excessive_worry', 'openai_answer', 'openai_answer2', 'openai_answer3', 'openai_answer4', 'openai_answer5']
subset = traindata[columns]
subset

columns = ['s_gad_3_excessive_worry', 'openai_answer']
subset = traindata[columns]
subset


#create a column that is the majority.
columns = ['openai_answer', 'openai_answer2', 'openai_answer3', 'openai_answer4', 'openai_answer5']
traindata['openai_final_answer'] = traindata[columns].mode(axis=1).iloc[:, 0]



#let's look at the percentage os openai response that matches the youth
same_vals = (traindata['s_gad_3_excessive_worry'] == traindata['openai_final_answer']).sum()
rows = len(traindata)
percentage = (same_vals / rows) * 100
percentage
# we got 72.41% correct openai response

#save csv
traindata.to_csv("openai_traindata_gadWorry.csv")



#----------------Using gpt 4 model------------------

    response = openai.ChatCompletion.create(
      model="gpt-4",
      messages=[
        {
          "role": "user",
          "content": content
        }
      ],
      temperature=1,
      max_tokens=1000,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )


    answer = response["choices"][0]["message"]["content"]
    traindata.loc[subject,"openai_answer5"]= answer



#-----------------Asking for explanation-----------------

    content = "Below are the responses of a youth on a psychological questionnaire. They are a " + str(age_answer) 
    content = content + " year old " + sex_answer
    content = content + ". They worry about their past behavior " + past_gad_answer
    content = content + ". They worry about school and examinations " + school_gad_answer
    content = content + ". They worry about disasters and accidents " + disaster_gad_answer
    content = content + ". They worry about their own health " + health_gad_answer
    content = content + ". They worry about bad things happening " + badthings_gad_answer
    content = content + ". They worry about the future " + future_gad_answer
    content = content + ". They worry about making and keeping friends " + friends_gad_answer
    content = content + ". They worry about death and dying " + death_gad_answer
    content = content + ". They worry about being bullied and teased " + bullied_gad_answer
    content = content + ". They worry about their weight and appearance " + weight_gad_answer
    content = content + mostdays_gad_dict[mostdays_gad_answer] + "worried on most days in the last 6 months"
    content = content + control_gad_dict[control_gad_answer] + "easy to control their worryness."
    content = content + "Given this information, do they excessively worry? Please respond with two sentences only. In the first sentence you must only respond with \"not\", \"perhaps\", or \"definitely\". Limit first sentence to 1 word. In the second sentence give your explanation."

    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {
          "role": "user",
          "content": content
        }
      ],
      temperature=1,
      max_tokens=1000,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    answer = response["choices"][0]["message"]["content"]
    segments = answer.split('.')


    traindata.loc[subject, "openai_answer"] = segments[0].strip()
    traindata.loc[subject, "openai_answer_explanation"] = segments[1].strip()


#---------------------------------------------------------------------------------------------









#-----------------------(bdd)-----------------------------------


import numpy as np
import pandas as pd
import openai
openai.api_key = str(np.loadtxt("/Users/jdec0124/Desktop/apikey.txt", dtype=str))

traindata=pd.read_csv("train_data.csv")

for subject in traindata.index[:29]:
    age_answer = traindata.loc[subject,"min_age"]
    sex_answer = traindata.loc[subject,"SEX"]

    appear_bdd_dict = {
        "no" : ". They don't have any ",
        "a little" : ". They have a little ",
        "a lot" : ". They have a lot of "
        }
    appear_bdd_choices = ["no", "a little", "a lot"]
    appear_bdd_answer = traindata.loc[subject,"s_bdd_1_concerns_appearance"]

    skincond_bdd_dict = appear_bdd_dict
    skincond_bdd_choices = appear_bdd_choices
    skincond_bdd_answer = traindata.loc[subject,"s_bdd_2a_skin_condition"]

    skincolor_bdd_dict = appear_bdd_dict
    skincolor_bdd_choices = appear_bdd_choices
    skincolor_bdd_answer = traindata.loc[subject,"s_bdd_2b_skin_colour"]

    hair_bdd_dict = appear_bdd_dict
    hair_bdd_choices = appear_bdd_choices
    hair_bdd_answer = traindata.loc[subject,"s_bdd_2c_hair_colour_or_condition"]

    bulk_bdd_dict = appear_bdd_dict
    bulk_bdd_choices = appear_bdd_choices
    bulk_bdd_answer = traindata.loc[subject,"s_bdd_2d_muscle_bulk"]

    body_bdd_dict = appear_bdd_dict
    body_bdd_choices = appear_bdd_choices
    body_bdd_answer = traindata.loc[subject,"s_bdd_2e_body_shape_or_size"]

    face_bdd_dict = appear_bdd_dict
    face_bdd_choices = appear_bdd_choices
    face_bdd_answer = traindata.loc[subject,"s_bdd_2f_facial_features"]
    
    other_bdd_dict = appear_bdd_dict
    other_bdd_choices = appear_bdd_choices
    other_bdd_answer = traindata.loc[subject,"s_bdd_2g_other_body_part"]

    asym_bdd_dict = appear_bdd_dict
    asym_bdd_choices = appear_bdd_choices
    asym_bdd_answer = traindata.loc[subject,"s_bdd_2h_asymmetry"]

    compothers_bdd_dict = {
        "no" : " not at all.",
        "a little" : " a little.",
        "a lot" : " a lot."
        }
    compothers_bdd_choices = appear_bdd_choices
    compothers_bdd_answer = traindata.loc[subject,"s_bdd_4a_compares_self_with_others"]

    checks_bdd_dict = compothers_bdd_dict
    checks_bdd_choices = appear_bdd_choices
    checks_bdd_answer = traindata.loc[subject,"s_bdd_4b_checking_own_appearance"]

    effort_bdd_dict = compothers_bdd_dict
    effort_bdd_choices = appear_bdd_choices
    effort_bdd_answer = traindata.loc[subject,"s_bdd_4c_effort_improving_appearance"]

    hide_bdd_dict = compothers_bdd_dict
    hide_bdd_choices = appear_bdd_choices
    hide_bdd_answer = traindata.loc[subject,"s_bdd_4d_hiding_appearance"]

    seek_bdd_dict = compothers_bdd_dict
    seek_bdd_choices = appear_bdd_choices
    seek_bdd_answer = traindata.loc[subject,"s_bdd_4e_seeking_reassurance"]

    improve_bdd_dict = compothers_bdd_dict
    improve_bdd_choices = appear_bdd_choices
    improve_bdd_answer = traindata.loc[subject,"s_bdd_4f_improve_body_shape"]

    surg_bdd_dict = compothers_bdd_dict
    surg_bdd_choices = appear_bdd_choices
    surg_bdd_answer = traindata.loc[subject,"s_bdd_4g_surgery_requested_or_used"]

    
    worrytime_bdd_choices = ["little or no time", "less than an hour", "about an hour", "a few hours", "many hours"]
    worrytime_bdd_answer = traindata.loc[subject,"s_bdd_5a_time_spent_worrying_appearance"]

    


    content = "Below are the responses of a youth on a psychological questionnaire. They are a " + str(age_answer) 
    content = content + " year old " + sex_answer
    content = content + appear_bdd_dict[appear_bdd_answer] + "concern about their appearance. "
    content = content + skincond_bdd_dict[skincond_bdd_answer] + "concern about a skin condition. "
    content = content + skincolor_bdd_dict[skincolor_bdd_answer] + "concern about their skin color. "
    content = content + hair_bdd_dict[hair_bdd_answer] + "concern about their hair color or a hair condition. "
    content = content + bulk_bdd_dict[bulk_bdd_answer] + "concern about their muscle bulk. "
    content = content + body_bdd_dict[body_bdd_answer] + "concern about their body shape or size. "
    content = content + face_bdd_dict[face_bdd_answer] + "concern about their facial features. "
    content = content + other_bdd_dict[other_bdd_answer] + "concern about other body parts. "
    content = content + asym_bdd_dict[asym_bdd_answer] + "concern about asymmetry. "
    content = content + "They repeatedly compare themselves with others" + compothers_bdd_dict[compothers_bdd_answer]
    content = content + " They repeatedly check their appearance" + checks_bdd_dict[checks_bdd_answer]
    content = content + " They put a lot of effort into imporving their appearance" + effort_bdd_dict[effort_bdd_answer]
    content = content + " They hide their appearance" + hide_bdd_dict[hide_bdd_answer]
    content = content + " They seek reassurance about their appearance" + seek_bdd_dict[hide_bdd_answer]
    content = content + " They put a lot of effort into improving their muscle mass or body shape" + improve_bdd_dict[improve_bdd_answer]
    content = content + " They have used or requested cosmetic surgery" + improve_bdd_dict[improve_bdd_answer]
    content = content + " They spend " + worrytime_bdd_answer + " worrying about their appearance. "
    content = content + "Given this information, how much time do they spend hiding or improving their appearance? Please respond with \"little or no time\", \"less than an hour\", \"about an hour\", \"a few hours\", or \"many hours\". Limit response to 5 words."


    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {
          "role": "user",
          "content": content
        }
      ],
      temperature=1,
      max_tokens=1000,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )


    answer = response["choices"][0]["message"]["content"]
    traindata.loc[subject,"openai_answer5"]= answer


#remove capitalization and punctuation
import re
def remove_caps_and_punct(text):
     text = text.lower()
     text = re.sub(r'[^\w\s]', '', text)
     return text

traindata['openai_answer5'] = traindata['openai_answer5'].apply(remove_caps_and_punct)


#create a subset of specified columns
columns = ['s_bdd_5b_time_spent_hiding_improving_appearance', 'openai_answer', 'openai_answer2', 'openai_answer3', 'openai_answer4', 'openai_answer5']
subset = traindata[columns]
subset

columns = ['s_bdd_5b_time_spent_hiding_improving_appearance', 'openai_answer']
subset = traindata[columns]
subset


#create a column that is the majority.
columns = ['openai_answer', 'openai_answer2', 'openai_answer3', 'openai_answer4', 'openai_answer5']
traindata['openai_final_answer'] = traindata[columns].mode(axis=1).iloc[:, 0]



#let's look at the percentage os openai response that matches the youth
same_vals = (traindata['s_bdd_5b_time_spent_hiding_improving_appearance'] == traindata['openai_final_answer']).sum()
rows = len(traindata)
percentage = (same_vals / rows) * 100
percentage
# we got 17.24% correct openai response - Not that great

#save csv
traindata.to_csv("openai_traindata_bddTimeAppearance.csv")



#----------------Using got 4 model------------------

    response = openai.ChatCompletion.create(
      model="gpt-4",
      messages=[
        {
          "role": "user",
          "content": content
        }
      ],
      temperature=1,
      max_tokens=1000,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )


    answer = response["choices"][0]["message"]["content"]
    traindata.loc[subject,"openai_answer5"]= answer




#------------------USing Explanation-----------------

    content = "Below are the responses of a youth on a psychological questionnaire. They are a " + str(age_answer) 
    content = content + " year old " + sex_answer
    content = content + appear_bdd_dict[appear_bdd_answer] + "concern about their appearance. "
    content = content + skincond_bdd_dict[skincond_bdd_answer] + "concern about a skin condition. "
    content = content + skincolor_bdd_dict[skincolor_bdd_answer] + "concern about their skin color. "
    content = content + hair_bdd_dict[hair_bdd_answer] + "concern about their hair color or a hair condition. "
    content = content + bulk_bdd_dict[bulk_bdd_answer] + "concern about their muscle bulk. "
    content = content + body_bdd_dict[body_bdd_answer] + "concern about their body shape or size. "
    content = content + face_bdd_dict[face_bdd_answer] + "concern about their facial features. "
    content = content + other_bdd_dict[other_bdd_answer] + "concern about other body parts. "
    content = content + asym_bdd_dict[asym_bdd_answer] + "concern about asymmetry. "
    content = content + "They repeatedly compare themselves with others" + compothers_bdd_dict[compothers_bdd_answer]
    content = content + " They repeatedly check their appearance" + checks_bdd_dict[checks_bdd_answer]
    content = content + " They put a lot of effort into imporving their appearance" + effort_bdd_dict[effort_bdd_answer]
    content = content + " They hide their appearance" + hide_bdd_dict[hide_bdd_answer]
    content = content + " They seek reassurance about their appearance" + seek_bdd_dict[hide_bdd_answer]
    content = content + " They put a lot of effort into improving their muscle mass or body shape" + improve_bdd_dict[improve_bdd_answer]
    content = content + " They have used or requested cosmetic surgery" + improve_bdd_dict[improve_bdd_answer]
    content = content + " They spend " + worrytime_bdd_answer + " worrying about their appearance. "
    content = content + "Given this information, how much time do they spend hiding or improving their appearance? Respond with two sentences. For the first sentence please respond with \"little or no time\", \"less than an hour\", \"about an hour\", \"a few hours\", or \"many hours\" only. Limit first sentence to 5 words. In the second sentence give your explanation."


    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {
          "role": "user",
          "content": content
        }
      ],
      temperature=1,
      max_tokens=1000,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    answer = response["choices"][0]["message"]["content"]
    segments = answer.split('.')


    traindata.loc[subject, "openai_answer"] = segments[0].strip()
    traindata.loc[subject, "openai_answer_explanation"] = segments[1].strip()





   
    
    
    

   

    
    










