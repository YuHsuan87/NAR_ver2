from ckiptagger import WS, POS, NER
# WS: word-segmentation 斷詞
# POS: part-of-speech tagging 詞性標注
# NER: nemed-entity-recognition 專有名詞識別

import pandas as pd

# load ckiptagger_model
def load_model():
    ws = WS('./data_ner')
    pos = POS('./data_ner')
    ner = NER('./data_ner')
    return ws, pos, ner

def load_file(file_name):
    df = pd.read_excel(file_name)
    return df
 
def cut_row(string):
    return string.replace('_x000D_', '')

# find the pos -> Nouns list
def find_N(pos_result):
    result = []
    for key in pos_result:
        if(key[1] == 'Na' or key[1] == 'Nc'):
            result.append(key[0])
    return result

if __name__ == '__main__':
    ws, pos, ner = load_model()
    df = load_file('data.xlsx')
    string = cut_row(df['計畫重點描述'][3076])
    # string = '行政院今天宣布日本福島5縣食品有條件解禁，總統蔡英文則保證「台灣不會進口核食」，福島5縣食品會於邊境逐批檢驗。日本產經新聞在台支局長矢板明夫認為，蔡英文此舉讓中國國家習近平「吃了一個大大的啞巴虧」。'
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
    print(pos_contrast)

    # NER
    ner_result = ner(ws_result, pos_result)
    print(ner_result)
    # for word in ner_result[0]:
    #     print(word)

    # release model memory
    del ws, pos, ner

