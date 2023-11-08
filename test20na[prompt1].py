# Prompt 1 : Distress [depression]


import numpy as np
import pandas as pd
import openai
openai.api_key = str(np.loadtxt("/Users/jdec0124/Desktop/apikey.txt", dtype=str))

traindata=pd.read_csv("train_data.20na.csv")

for subject in traindata.index[:62]:
    age_answer = traindata.loc[subject,"min_age"]
    sex_answer = traindata.loc[subject,"SEX"]
    
    sad_dep_dict = {
        "yes" : " They have ",
        "no" : " They have not "
        }
    sad_dep_choices = ["yes", "no"]
    sad_dep_answer = traindata.loc[subject,"s_dep_1_sad"]
    if pd.isna(sad_dep_answer):
        sad_dep_answer = "They did not respond on whether they "

    misdaily_dep_dict = {
        "yes" : " There was ",
        "no" : " There was not "
        }
    misdaily_dep_choices = sad_dep_choices
    misdaily_dep_answer = traindata.loc[subject,"s_dep_2_miserable_daily"]
    if pd.isna(misdaily_dep_answer):
        misdaily_dep_answer = "They did not respond on whether there was "

    mismostly_dep_dict = {
        "yes" : "was for most of the day. ",
        "no" : "was not for most of the day. "
        }
    mismostly_dep_choices = sad_dep_choices
    mismostly_dep_answer = traindata.loc[subject,"s_dep_3_miserable_mostly"]
    if pd.isna(mismostly_dep_answer):
        mismostly_dep_answer = "was not recorded how long it lasted as they did not respond to the question. "

    irrit_dep_dict = sad_dep_dict
    irrit_dep_choices = sad_dep_choices
    irrit_dep_answer = traindata.loc[subject,"s_dep_7_irritable"]
    if pd.isna(irrit_dep_answer):
        irrit_dep_answer = "They did not respond on whether they "

    irritdaily_dep_dict = misdaily_dep_dict
    irritdaily_dep_choices = sad_dep_choices
    irritdaily_dep_answer = traindata.loc[subject,"s_dep_8_irritable_daily"]
    if pd.isna(irritdaily_dep_answer):
        irritdaily_dep_answer = "They did not respond on whether there was "

    irritmostly_dep_dict = mismostly_dep_dict
    irritmostly_dep_choices = sad_dep_choices
    irritmostly_dep_answer = traindata.loc[subject,"s_dep_9_irratable_mostly"]
    if pd.isna(irritmostly_dep_answer):
        irritmostly_dep_answer = "was not recorded how long it lasted as they did not respond to the question. "

    anh_dep_dict = sad_dep_dict
    anh_dep_choices = sad_dep_choices
    anh_dep_answer = traindata.loc[subject,"s_dep_13_anhedonia"]
    if pd.isna(anh_dep_answer):
        anh_dep_answer = "They did not respond on whether they "

    anhdaily_dep_dict = misdaily_dep_dict
    anhdaily_dep_choices = sad_dep_choices
    anhdaily_dep_answer = traindata.loc[subject,"s_dep_14_anhedonia_daily"]
    if pd.isna(anhdaily_dep_answer):
        anhdaily_dep_answer = "They did not respond on whether there was "

    anhmostly_dep_dict = mismostly_dep_dict
    anhmostly_dep_choices = sad_dep_choices
    anhmostly_dep_answer = traindata.loc[subject,"s_dep_15_anhedonia_mostly"]
    if pd.isna(anhmostly_dep_answer):
        anhmostly_dep_answer = " was not recorded how long it lasted as they did not respond to the question. "

    tired_dep_dict = {
        "yes" : " they did ",
        "no" : " they did not "
        }
    tired_dep_choices = ["yes", "no"]
    tired_dep_answer = traindata.loc[subject,"s_dep_18a_tired"]
    if pd.isna(tired_dep_answer):
        tired_dep_answer = "They did not respond on whether they "

    appetite_dep_dict = tired_dep_dict
    appetite_dep_choices = tired_dep_choices
    appetite_dep_answer = traindata.loc[subject,"s_dep_18b_appetite"]
    if pd.isna(appetite_dep_answer):
        appetite_dep_answer = "They did not respond on whether they "

    weight_dep_dict = tired_dep_dict
    weight_dep_choices = tired_dep_choices
    weight_dep_answer = traindata.loc[subject,"s_dep_18c_weight"]
    if pd.isna(weight_dep_answer):
        weight_dep_answer = "They did not respond on whether they "

    insomnia_dep_dict = tired_dep_dict
    insomnia_dep_choices = tired_dep_choices
    insomnia_dep_answer = traindata.loc[subject,"s_dep_18d_insomnia"]
    if pd.isna(insomnia_dep_answer):
        insomnia_dep_answer = "They did not respond on whether they "

    hypersom_dep_dict = tired_dep_dict
    hypersom_dep_choices = tired_dep_choices
    hypersom_dep_answer = traindata.loc[subject,"s_dep_18e_hypersomnia"]
    if pd.isna(hypersom_dep_answer):
        hypersom_dep_answer = "They did not respond on whether they "

    agitat_dep_dict = tired_dep_dict
    agitat_dep_choices = tired_dep_choices
    agitat_dep_answer = traindata.loc[subject,"s_dep_18f_agitation"]
    if pd.isna(agitat_dep_answer):
        agitat_dep_answer = "They did not respond on whether they "

    worth_dep_dict = tired_dep_dict
    worth_dep_choices = tired_dep_choices
    worth_dep_answer = traindata.loc[subject,"s_dep_18g_worthless"]
    if pd.isna(worth_dep_answer):
        worth_dep_answer = "They did not respond on whether they "

    concen_dep_dict = tired_dep_dict
    concen_dep_choices = tired_dep_choices
    concen_dep_answer = traindata.loc[subject,"s_dep_18h_concentration"]
    if pd.isna(concen_dep_answer):
        concen_dep_answer = "They did not respond on whether they "

    sadduration_dep_dict = {
        "less than 2 weeks" : "less than 2 weeks",
        "2 weeks or more" : "2 weeks or more"
        }
    sadduration_dep_choices = ["less than 2 weeks", "2 weeks or more"]
    sadduration_dep_answer = traindata.loc[subject,"s_dep_5_miserable_duration"]
    if pd.isna(sadduration_dep_answer):
        sadduration_dep_answer = "an unkown amount (question was skipped)"
    

    irritduration_dep_choices = sadduration_dep_choices
    irritduration_dep_answer = traindata.loc[subject,"s_dep_11_irritable_duration"]
    if pd.isna(irritduration_dep_answer):
        irritduration_dep_answer = "an unkown amount (question was skipped)"

    anhduration_dep_choices = sadduration_dep_choices
    anhduration_dep_answer = traindata.loc[subject,"s_dep_16_anhedonia_duration"]
    if pd.isna(anhduration_dep_answer):
        anhduration_dep_answer = "an unkown amount (question was skipped)"

    family_dep_choices = ["not at all", "a little", "a medium amount", "a great deal"]
    family_dep_answer = traindata.loc[subject,"s_dep_20a_impact_family"]
    if pd.isna(family_dep_answer):
        family_dep_answer = "an unkown amount (question was skipped)"

    friend_dep_choices = family_dep_choices
    friend_dep_answer = traindata.loc[subject,"s_dep_20b_impact_friendships"]
    if pd.isna(friend_dep_answer):
        friend_dep_answer = "an unkown amount (question was skipped)"

    school_dep_choices = family_dep_choices
    school_dep_answer = traindata.loc[subject,"s_dep_20c_impact_school_work"]
    if pd.isna(school_dep_answer):
        school_dep_answer = "an unkown amount (question was skipped)"

    leisure_dep_choices = family_dep_choices
    leisure_dep_answer = traindata.loc[subject,"s_dep_20d_impact_leisure"]
    if pd.isna(leisure_dep_answer):
        leisure_dep_answer = "an unkown amount (question was skipped)"


    irritimprove_dep_choices = ["easily", "with difficulty/only briefly", "not at all"]
    irritimprove_dep_answer = traindata.loc[subject,"s_dep_10_irritable_improved"]
    if pd.isna(irritimprove_dep_answer):
        irritimprove_dep_answer = "an unkown amount (question was skipped)"

    mischeer_dep_choices = irritimprove_dep_choices
    mischeer_dep_answer = traindata.loc[subject,"s_dep_4_miserable_cheered_up"]
    if pd.isna(mischeer_dep_answer):
        mischeer_dep_answer = "an unkown amount (question was skipped)"
    
    content = "Below are the responses of a youth on a psychological questionnaire. They are a " + str(age_answer) 
    content = content + " year old " + sex_answer
    content = content + sad_dep_dict[sad_dep_answer] + "experienced sadness within the past 4 weeks."
    content = content + misdaily_dep_dict[misdaily_dep_answer] + "a period of time within the past 4 weeks where they were miserable daily."
    content = content + " When they were miserable, it " + mismostly_dep_dict[mismostly_dep_answer]
    content = content + irrit_dep_dict[sad_dep_answer] + "experienced irritability within the past 4 weeks. "
    if irritdaily_dep_answer in irritdaily_dep_dict:
        content = content + irritdaily_dep_dict[irritdaily_dep_answer] + "a period of time within the past 4 weeks where they were irritable daily."
    else:
        content = content + " They did not respond on whether there was a period of time within the past 4 weeks where they were irritable daily. " 
    if irritmostly_dep_answer in irritmostly_dep_dict:
        content = content + " When they were irritable, it " + irritmostly_dep_dict[irritmostly_dep_answer]
    else:
        content = content + "  When they were irritable, it was not recorded how long it lasted as they did not respond to the question. "
    content = content + anh_dep_dict[anh_dep_answer] + "experienced anhedonia within the past 4 weeks."
    if anhdaily_dep_answer in anhdaily_dep_dict:
        content = content + anhdaily_dep_dict[anhdaily_dep_answer] + "a period of time within the past 4 weeks where they experienced anhedonia daily."
    else:
        content = content + " They did not respond on whether there was a period of time within the past 4 weeks where they experienced anhedonia daily. " 
    if anhmostly_dep_answer in anhmostly_dep_dict:
        content = content + " When experiencing anhedonia, it " + anhmostly_dep_dict[anhmostly_dep_answer]
    else:
        content = content + "  When experiencing anhedonia, it was not recorded how long it lasted as they did not respond to the question. "
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
    content = content + ". They are cheered up " + mischeer_dep_answer + " when miserable."
    content = content + " Given this information, how much has their sadness, irritability or loss of interest upset or distressed them? Please respond with \"not at all\", \"a little\", \"a medium amount\", or \"a great deal\". Limit response to 4 words."


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
    traindata.loc[subject,"openai_answer"]= answer




#I use the below to run separatly -> experience less timeouts


responses = []

for subject in traindata.index[:62]:
    content = content
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
    traindata.loc[subject,"openai_answer"]= answer














#remove capitalization and punctuation
import re
def remove_caps_and_punct(text):
     text = text.lower()
     text = re.sub(r'[^\w\s]', '', text)
     return text

traindata['openai_answer'] = traindata['openai_answer'].apply(remove_caps_and_punct)


#create a subset of specified columns
columns = ['s_dep_19_distress', 'openai_answer', 'openai_answer1', 'openai_answer2', 'openai_answer3', 'openai_answer4']
subset = traindata[columns]
subset

columns = ['s_dep_19_distress', 'openai_final_answer']
subset = traindata[columns]
subset


#create a column that is the majority.
columns = ['openai_answer', 'openai_answer1', 'openai_answer2', 'openai_answer3', 'openai_answer4']
traindata['openai_final_answer'] = traindata[columns].mode(axis=1).iloc[:, 0]


#let's look at the percentage os openai response that matches the youth
same_vals = (traindata['s_dep_19_distress'] == traindata['openai_answer']).sum()
rows = len(traindata)
percentage = (same_vals / rows) * 100
percentage


### (3.5) - The percentages are drastically lower once adding in NA's --> could be phrasing of propmt?
### With only using one response 
# we got 19.35% correct openai response
### With best out of 5
# we got 22.58% correct openai response
### With explanations (ran once)
# we got 3.23% correct openai response -> this decreased quite a bit from the other two.


#save csv
traindata.to_csv("openai_traindata_DepDistressExplainprompt.csv")

#--------------Explanations-----------------

    content = "Below are the responses of a youth on a psychological questionnaire. They are a " + str(age_answer) 
    content = content + " year old " + sex_answer
    content = content + sad_dep_dict[sad_dep_answer] + "experienced sadness within the past 4 weeks."
    content = content + misdaily_dep_dict[misdaily_dep_answer] + "a period of time within the past 4 weeks where they were miserable daily."
    content = content + " When they were miserable, it " + mismostly_dep_dict[mismostly_dep_answer]
    content = content + irrit_dep_dict[sad_dep_answer] + "experienced irritability within the past 4 weeks. "
    if irritdaily_dep_answer in irritdaily_dep_dict:
        content = content + irritdaily_dep_dict[irritdaily_dep_answer] + "a period of time within the past 4 weeks where they were irritable daily."
    else:
        content = content + " They did not respond on whether there was a period of time within the past 4 weeks where they were irritable daily. " 
    if irritmostly_dep_answer in irritmostly_dep_dict:
        content = content + " When they were irritable, it " + irritmostly_dep_dict[irritmostly_dep_answer]
    else:
        content = content + "  When they were irritable, it was not recorded how long it lasted as they did not respond to the question. "
    content = content + anh_dep_dict[anh_dep_answer] + "experienced anhedonia within the past 4 weeks."
    if anhdaily_dep_answer in anhdaily_dep_dict:
        content = content + anhdaily_dep_dict[anhdaily_dep_answer] + "a period of time within the past 4 weeks where they experienced anhedonia daily."
    else:
        content = content + " They did not respond on whether there was a period of time within the past 4 weeks where they experienced anhedonia daily. " 
    if anhmostly_dep_answer in anhmostly_dep_dict:
        content = content + " When experiencing anhedonia, it " + anhmostly_dep_dict[anhmostly_dep_answer]
    else:
        content = content + "  When experiencing anhedonia, it was not recorded how long it lasted as they did not respond to the question. "
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
    content = content + ". They are cheered up " + mischeer_dep_answer + " when miserable."
    content = content + " Given this information, how much has their sadness, irritability or loss of interest upset or distressed them? Respond with 2 sentences. Please respond in the first sentence with \"not at all\", \"a little\", \"a medium amount\", or \"a great deal\" only. In the second sentence give your explanation. Limit first sentence to only 3 words"



for subject in traindata.index[:62]:
    content = content
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



