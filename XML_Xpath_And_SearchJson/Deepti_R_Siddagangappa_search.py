import json, re
import sys
from collections import OrderedDict
import string

all = []



def main():

    d={}
    out=[]
    outfile=open('out_file.json', 'w+')
    helper_function = set(string.punctuation) - set("'")
    helper_function = ''.join(x for x in list(helper_function))
    helper_function =string.maketrans(helper_function,' '*len(helper_function))

    json_obj = json.load(open(sys.argv[1],'r'))
    string_in_chk = sys.argv[2].split()
    total_len = len(string_in_chk)

    for i in json_obj['data']:
        for j in i['paragraphs']:
            for k in j['qas']:
                number_of_matches = 0
                list_qa_data_set = k['question']
                list_qa_data_set = list_qa_data_set.strip()
                list_qa_data_set = list_qa_data_set.encode('ascii','ignore').translate(helper_function)

                list_qa_data_set = list_qa_data_set.strip().split()

                for iterator1 in string_in_chk:
                    for iterator2 in list_qa_data_set:
                        iterator1 = iterator1.lower()
                        iterator2 = iterator2.lower()
                        if iterator1 == iterator2:
                            number_of_matches = number_of_matches + 1
                            break
                if number_of_matches == total_len:
                    all.append(k['question'])

                out.append(OrderedDict([("id", k['id']) , ("question", k['question']) ,("answer",k['answers'][0]['text'])]))

                json.dump(out, outfile,indent=3)




main()
