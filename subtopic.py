from unittest import result
from utils import *


if __name__ == '__main__':
    df = load_file('combined_data.xlsx')

    sub_topics = {}
    for i in range(103, 111):
        sub_topics[i] = []
    # print(sub_topics)

    for i in range(len(df)):
        if(pd.notna(df['主題9'][i])):
            string = df['次主題9'][i]
            string = string.replace('##', ',')
            wordlist = string.split(',')
            # print(df['年度'][i]) 
            # print(wordlist)
            for word in wordlist:
                sub_topics[df['年度'][i]].append(word)

    # print(sub_topics)

    # remove duplicate
    for key, wordlist in sub_topics.items():
        print(f'{key}:')
        tmp_list = set(wordlist)
        wordlist = list(tmp_list)
        for word in wordlist:
            print(word, end = ',')
        print() 
    
