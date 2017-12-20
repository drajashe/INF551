
from collections import Counter

import json, re
import sys


def main():
    list_ques = ["how","many","much","when","where","which","what","who","whom"]
    Count_how=0
    Count_how_many=0
    Count_how_much=0
    Count_what=0
    Count_when=0
    Count_where=0
    Count_which = 0
    Count_who = 0
    Count_whom =0
    question_All=[]

    json_data = json.load(open(sys.argv[1],'r'))

    for i in json_data['data']:
        for j in i['paragraphs']:
            for k in j['qas']:
                list_qa_data_set = k['question']
                #print list_qa_data_set
                list_qa_data_set = list_qa_data_set.lower()
                list_qa_data_set = list_qa_data_set.strip()
                list_qa_data_set = list_qa_data_set.replace(',', ' ')
                list_qa_data_set = list_qa_data_set.split()[:2]

                question_All.append(list_qa_data_set)

    for i in range(len(question_All)):

        if (question_All[i][0] == list_ques[0]) and question_All[i][1] == list_ques[1]:
            Count_how_many += 1
        elif (question_All[i][0] == list_ques[0]) and question_All[i][1] == list_ques[2]:
            Count_how_much += 1
        elif question_All[i][0] == list_ques[0]:
            Count_how += 1
        elif question_All[i][0] == list_ques[3]:
            Count_when += 1
        elif question_All[i][0] == list_ques[4]:
            Count_where += 1
        elif question_All[i][0] == list_ques[5]:
            Count_which += 1
        elif question_All[i][0] == list_ques[6]:
            Count_what += 1
        elif question_All[i][0] == list_ques[7] :
            Count_who += 1
        elif question_All[i][0] == list_ques[8]:
            Count_whom += 1



    Count_how = Count_how + Count_how_many + Count_how_much

    final_dict = {list_ques[0]:Count_how,list_ques[0]+'_'+list_ques[1]:Count_how_many,list_ques[0]+"_"+list_ques[2]:Count_how_much,list_ques[3]:Count_when,list_ques[6]:Count_what,list_ques[4]:Count_where,list_ques[5]:Count_which,list_ques[7]:Count_who,list_ques[8]:Count_whom}
    with open('out.json', 'w') as output:

        json.dump(final_dict, output)




main()
