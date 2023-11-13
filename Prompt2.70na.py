import numpy as np
import pandas as pd
import openai

openai.api_key = str(np.loadtxt("/Users/jdec0124/Desktop/apikey.txt", dtype=str))

traindata=pd.read_csv("train_data2.70na.csv")

for subject in traindata.index[:76]:
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
    content = content + control_gad_dict[control_gad_answer] + "easyto control their worryness."
    content = content + "Given this information, do they excessively worry? You must only respond with \"no\", \"perhaps\", or \"definitely\". Limit response to 1 word."

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
    content = content + "Given this information, do they excessively worry? Please respond with two sentences only. In the first sentence you must only respond with \"no\", \"perhaps\", or \"definitely\". Limit first sentence to 1 word. In the second sentence give your explanation."

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
same_vals = (traindata['s_gad_3_excessive_worry'] == traindata['openai_answer']).sum()
rows = len(traindata)
percentage = (same_vals / rows) * 100
percentage

#### One Time : 50.66%
#save csv
traindata.to_csv("openai_traindata_Prompt2_1.csv")

#### Best out of 5 : 64%
#save csv
traindata.to_csv("openai_traindata_Prompt2_Bo5.csv")

#### Explanation : %
#save csv
traindata.to_csv("openai_traindata_Prompt2_Explanation.csv")




