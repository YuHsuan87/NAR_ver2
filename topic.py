from utils import *
from summarize import *

def find_topic_year(df, topic_index):
    end_index = [402, 817, 1216, 1663, 2050, 2425, 2776]
    for topic in topics:
        # Projects that appear in each year by topic_index
        topic_year_index = {}
        for i in range(103, 111):
            topic_year_index[i] = []
        # Observe the year in which the topic appeared
        topic_year = set()

        for index in topic_index[topic]:
            # print(index)
            if(index <= end_index[0]):
                topic_year.add(103)
                topic_year_index[103].append(index)

            elif(index >end_index[6]):
                topic_year.add(110)
                topic_year_index[110].append(index)

            else:
                for i in range(6):
                    if(index > end_index[i] and index <= end_index[i+1]):
                        topic_year.add(i + 104)
                        topic_year_index[i + 104].append(index)

        # print(f'{topic}:')
        # print(topic_year)
        # print(topic_year_index)

    # print(topic_year_index)
    for key, item in topic_year_index.items():
        print('--------------------------------------------------------------')
        print(key)
        for i in item:
            string = cut_row(df['計畫重點描述'][i])
            
            s_list = summarization(string)

# 找出各主題的index值
def find_topic_index(df_topic, topics):
    topic_index = {}
    for i in range(1, 10):
        topic_index[f'主題{i}'] = []

    for i in range(1, 10):
        for j in range(len(df_topic)):
            if(pd.notna(df_topic[f'主題{i}'][j])):
                topic_index[f'主題{i}'].append(j)

    return topic_index

if __name__ == '__main__':
    df = load_file('data.xlsx')
    df_topic = load_file('data_topic.xlsx')
    topics = [f'主題{i}' for i in range(1, 10)]
    topic_index = find_topic_index(df_topic, topics)
    find_topic_year(df, topic_index)

    
            