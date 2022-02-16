# NAR_ver2
## python 檔案
- model
    - 採用套件: [Ckiptagger](https://ckip.iis.sinica.edu.tw/demo/)
    ```
    pipenv install tensorflow
    pipenv install ckiptagger
    ```
    - file:
    將 model 檔案放至於本地端，我則取名 file 為 data_ner，執行速度較快。
    [下載連結](https://drive.google.com/drive/folders/105IKCb88evUyLKlLondvDBoh7Dy_I1tm)
- **file(透過上述自行建立)**
    - data_ner : 放置 Ckiptagger 的 WS、POS、NER 的model
- **dataset**
    - data_xlsx : 原始資料集，未包含主題4～主題9的標注
    - combined_data.xlsx : 結合**主題4～主題9**的計畫書內容
    - data_topic.xlsx : 僅包含計畫名稱以及計畫主題 
- **function**
    - utils.py : 各程式主要 import 的檔案，具備 load_model、load_file 等等常用功能
    - topic.py : 取得各主題的出現年份及各主題的 index 值
    - summarize.py : 針對文章取出前三重要摘要的句子(Text Summarization)
    - subtopic.py : 針對主題取出次主題
    - output.py : 顯示各實驗(POS、NER、Summarize)的結果
