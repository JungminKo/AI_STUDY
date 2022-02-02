## KONLPY
- Hannanum 
- Kkma
- Komor
- Okt

```Python
from konlpy.tag import Hannanum
hannanum = Hannanum() 
print(hannanum.morphs('삼십 대의 내가 십 대, 이십 대의 나를 만났다'))
# ['삼십', '대', '의', '나', '가', '십', '대', ',', '이십', '대', '의', '나', '를', '만나', '아다']


from konlpy.tag import Kkma
kkma = Kkma()
print(kkma.morphs('삼십 대의 내가 십 대, 이십 대의 나를 만났다'))
# ['삼십', '대', '의', '내가', '십', '대', ',', '이십', '대', '의', '나', '를', '만나', '었', '다']

from konlpy.tag import Komoran
komoran = Komoran()
print(komoran.morphs('삼십 대의 내가 십 대, 이십 대의 나를 만났다'))
# ['삼십', '대', '의', '내', '가', '십', '대', ',', '이십', '대', '의', '나', '를', '만나', '았', '다']

from konlpy.tag import Okt
okt = Okt()
print(okt.morphs('삼십 대의 내가 십 대, 이십 대의 나를 만났다'))
# ['삼십', '대의', '내', '가', '십', '대', ',', '이십', '대의', '나를', '만났다']
```

## text processing
```Python
import pandas as pd
df = pd.read_csv("./NoWayHome_Review.csv")

df['1'] = df['1'].str.replace('[^가-힣A-z ]','') # remove text except Korean, English, spacing
words = " ".join(df['1'].astype('str').tolist())

# morphological analysis(형태소 분석)
from konlpy.tag import Okt
okt = Okt()
words1 = okt.morphs(words,stem=True)

# stopwords
stop_words = '''이 의 을 들 에 가 를 다 는 은 도 것 로 으로 에서 때 부터 않다 또
              과 중 더 와 점 그리고 고 이다 에게 면 아 하다 있다 되다 없다 수 그 만 내 안'''
stop_words = stop_words.split()
result = []
for word in words1:
    if word not in stop_words:
        result.append(word)

# count word frequency
from collections import Counter
count = Counter(result)
count.most_common(100)
```

## Wordcloud
```Python
from wordcloud import WordCloud
import matplotlib.pyplot as plt

wc = WordCloud(font_path='c:/Windows/Fonts/malgun.ttf',background_color="white", max_font_size=60)
cloud = wc.generate_from_frequencies(dict(count))
plt.figure(figsize=(12, 8))
plt.imshow(cloud)
plt.axis("off")
plt.show()
```

## Word2Vec
```Python
def processing(sentence):
    stopwords = '''이 의 을 들 에 가 를 다 는 은 도 것 로 으로 에서 때 부터 않다 또
              과 중 더 와 점 그리고 고 이다 에게 면 아 하다 있다 되다 없다 수 그 만 내 안'''
    words = okt.morphs(sentence,stem=True)
    result = []
    for word in words:
        if word not in stop_words:
            result.append(word)
    return result
    
    
## morphological analysis for each sentence
sentence_list = df['1'].astype('str').apply(processing).to_list()


from gensim.models import Word2Vec
model = Word2Vec(sentences=sentence_list, window=5, min_count=5, workers=4, sg=0)
model.wv.most_similar('스파이더맨')
```




### Extra : Crawling movie comments from Naver Movie 
(Code Reference: https://kimdingko-world.tistory.com/77) 

```Python
import requests
from bs4 import BeautifulSoup

## movie : spiderman no way home
url_pre = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=208077&type=after&onlyActualPointYn=N&onlySpoilerPointYn=N&order=sympathyScore&page='
id_list = []
id_pre = '_filtered_ment_'

## Check if it's working
for page in range(10):
    print('\n',page+1,"페이지\n")
    site = url_pre+str(page+1)  
    res = requests.get(site)

    soup = BeautifulSoup(res.content,'html.parser')
    
    score_list = []
    scores = soup.find_all('div','star_score')
    for score in scores:
        score_list.append(score.get_text())
    
    for i in range(10):
        id_list.append(id_pre+str(i))

    mydata = []    
    for id in id_list:    
        mydata.append(soup.find('span',{'id':id}).get_text())
        
    for score, line in zip(score_list, mydata):
        print(score.strip(), line.strip())
        
## store the information about rating and comments of movie in final_data 
id_list = []
id_pre = '_filtered_ment_'
final_data = []

for page in range(150): # page number
    site = url_pre+str(page+1) 
    res = requests.get(site)

    soup = BeautifulSoup(res.content,'html.parser')
    
    score_list = []
    scores = soup.find_all('div','star_score')
    for score in scores:
        score_list.append(score.get_text())
    
    for i in range(10):
        id_list.append(id_pre+str(i))

    mydata = []    
    for id in id_list:    
        mydata.append(soup.find('span',{'id':id}).get_text())

    for score, line in zip(score_list, mydata):
        final_data.append([score.strip(), line.strip()])

## save to csv file
import pandas as pd

final_df = pd.DataFrame(final_data)
final_df.to_csv("./NoWayHome_Review.csv", index=False, encoding='utf-8-sig')
```
