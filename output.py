from enum import unique
from unittest import result
from utils import *
from summarize import summarization


if __name__ == '__main__':
    ws, pos, ner = load_model()
    df = load_file('data.xlsx')
    string = cut_row(df['計畫重點描述'][379])
    # print(df['中文關鍵詞'][377])
    print('Orginal:')
    print(string)

    # WS
    # string convert to list
    ws_result = ws([string])
    # print(ws_result)

    # POS
    pos_result = pos(ws_result)
    # print(pos_result)
    pos_contrast = []
    for i in range(len(pos_result[0])):
        pos_contrast.append((ws_result[0][i],pos_result[0][i]))
    print('POS:')
    # print(pos_contrast)
    N_list = find_N(pos_contrast)
    # print(N_list)

    # NER
    ner_result = ner(ws_result, pos_result)
    print('NER:')
    # print(ner_result)
    for word in ner_result[0]:
        print(word)
    # release model memory
    del ws, pos, ner

    s_lists = summarization(string)

    final_keyword = []
    for s_list in s_lists:
        for noun in N_list:
            if(s_list.find(noun) != -1):
                final_keyword.append(noun)

    unique_set = set(final_keyword)
    final_keyword = list(unique_set)
    print('-------------------------------------------')
    print(final_keyword)
