## Prompt 1 : 


import numpy as np
import pandas as pd
import openai
openai.api_key = str(np.loadtxt("/Users/jdec0124/Desktop/apikey.txt", dtype=str))

traindata=pd.read_csv("train_data.70na.csv")

for subject in traindata.index[:67]:
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

    mischeer_dep_choices = irritimprove_dep_choices
    mischeer_dep_answer = traindata.loc[subject,"s_dep_4_miserable_cheered_up"]

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
    content = content + ". They are cheered up " + mischeer_dep_answer + " when miserable."
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
    traindata.loc[subject,"openai_answer4"]= answer


########ExplanationContent/Ending##################

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
    content = content + ". They are cheered up " + mischeer_dep_answer + " when miserable."
    content = content + " Given this information, how much has their sadness, irritability or loss of interest upset or distressed them? Respond with 2 sentences. Please respond in the first sentence with \"not at all\", \"a little\", \"a medium amount\", or \"a great deal\" only. In the second sentence give your explanation. Limit first sentence to only 3 words"

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

#create a column that is the majority.
columns = ['openai_answer', 'openai_answer1', 'openai_answer2', 'openai_answer3', 'openai_answer4']
traindata['openai_final_answer'] = traindata[columns].mode(axis=1).iloc[:, 0]

#let's look at the percentage os openai response that matches the youth
same_vals = (traindata['s_dep_19_distress'] == traindata['openai_answer']).sum()
rows = len(traindata)
percentage = (same_vals / rows) * 100
percentage

#### One Time : 68.66%
#save csv
traindata.to_csv("openai_traindata_DepDistress70(1).csv")

#### Best out of 5 : 68.66%
#save csv
traindata.to_csv("openai_traindata_Prompt1(Bo5).csv")

#### Explanation : 53.73%
#save csv
traindata.to_csv("openai_traindata_Prompt1(Explanation).csv")




