from gensim.summarization.summarizer import summarize
from utils import *
from snownlp import SnowNLP
import os

def split(content):
    end_flag = ['，', '。', ';', '?', '!', '、']
    result = ''
    tmp_str = ''
    for i in range(len(content)):
        if(content[i] in end_flag):
            result += tmp_str + '\n'
            tmp_str = ''
        else:
            if(content[i] == ' '):
                continue
            tmp_str += content[i]
    return result

# 中文使用 gensim、snownlp 需要針對文章進行切割
def divide(content : list):
    result = ''
    for key in content:
        result += key + ' '
    return result

# 將結果的空格消除
def clean(result : str):
    result = result.replace(' ', '')
    return result

# run gensim and snownlp
def summarization(content):
    # print(content)
    content = split(content)
    # print(content)
    ws, _, _ = load_model()
    ws_result = ws([content])
    sentence = ws_result[0]
    div_sentence = divide(sentence)
    # print(divide(sentence))

    # result = summarize(div_sentence)
    # result  = clean(result)
    # print('gensim:')
    # print(result)

    s = SnowNLP(div_sentence)
    s_list = s.summary(3)
    for index in range(len(s_list)):
        s_list[index] = clean(s_list[index])
    # print('Summarize:')
    print(s_list)
    return s_list

if __name__ == '__main__':
    # os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
    df = load_file('data.xlsx')
    for i in range(1):
        print('---------------------------------------------------------------')
        # content= cut_row(df['計畫重點描述'][i])
        content = u'''名導明金成8日因心因性休克猝逝，他的追思靈堂今（10）日開放弔唁，與他合作過的演員林依晨、温昇豪、六月等人都到場致意，多年好友庹宗康也在稍早現身，受訪時忍不住情緒淚崩，坦言很擔心明金成妻子Patty（林沛締）的身體狀況。'''
        summarization(content)