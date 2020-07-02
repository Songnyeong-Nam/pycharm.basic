from dataclasses import dataclass

import nltk
import re
from nltk.tokenize import word_tokenize
from konlpy.tag import Okt
from nltk import FreqDist

import pandas as pd
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt

@dataclass()
class Entity:
    def __init__(self):
       self._context = ''
       self._fname = ''
       self._target = ''

    @property
    def context(self) -> str: return self._context
    @context.setter
    def context(self, context): self._context = context

    @property
    def fname(self) -> str: return self._fname
    @fname.setter
    def fname(self,fname): self._fname = fname

    @property
    def target(self) -> str: return self._target
    @target.setter
    def target(self,target): self._target = target



class Service:
    def __init__(self):
        self.texts = []
        self.tokens = []
        self.okt = Okt()
        self.stopwords = []
        self.freqtxt = []

    def extract_text(self,payload):
        print('>> text 문서에서 token 추출')
        filename = payload.context + payload.frame
        with open(filename, 'r', encoding='utf-8') as f:
            self.texts = f.read()
        print(f'1단계 결과물 : {self.texts[:300]}')

    def tokenize(self):
        print('>> 2. corpus에서 token 추출')
        texts = self.texts.replace('\n', ' ')
        tokenizer = re.compile(r'[^ㄱ-힣]')
        # ^는 not 과 start 의 두 가지 개념이 있다.
        # [^]는 not, ^[] 는 start의 의미로 표현된다.
        self.texts = tokenizer.sub(' ', texts)
        # 한글이 아닌 것은 '' 처리해서
        print(f'단계 : slef.texts[:300]')

    def conversion_token(self):
        print('>> 3. 한글 token 변환')
        self.tokens = word_tokenize(self.texts)
        print(f'3단계 결과물 : {self.tokens[:300]}')

    def compound_noun(self):
        print('>> 4. 복합명사화')
        arr_ = []    #동사/명사의 구분은 다운받은 딕셔너리를 통해 판별한다.
        for token in self.tokens:
            token_pos = self.okt.pos(token)
            _=[txt_tags[0] for txt_tags in token_pos
               if txt_tags[1] == 'Noun']
        if len("".join(_)) > 1:
            noun_tokens.append("".join(_))
        self.texts = " ".join((noun_tokens))
        print(f'4단계 {}')

    def extract_stopword(self) :
        print('>> 5. 노이즈 코퍼스(=스탑워드) token 추출')

    def filtering_text_with_stopword(self):
        print('>> 6. 노이즈 필터링 후 시그널(meaningful word) 추출')

    def frequent_text(self):
        print('>> 7. 시그널의 사용빈도 정렬')

    def wordcloud(self):
        print('>> 8. visualize')

class Controller:
    def __init__(self):
        pass

    def download_dictionary(self):
        nltk.download('all')

    def data_analysis(self):
        entity = Entity()
        service = Service()
        entity.context = './data' 
        entity.fname = 'kr-Report_2018.txt'

        service.extract_text(entity)
        service.tokenize()
        service.conversion_token()      #한글에만 적용
        service.compound_noun()         #명사만 compound 시킴
        service.extract_stopword()      # 통계에 필요없는 단어
        service.filtering_text_with_stopword() # 통계에
        service.frequent_text()         #빈도수 체크
        service.wordcloud()


def print_menu():
    print('0,Exit\n')
    print('1,Download Dic\n')
    return input('choose menu\n')

app = Controller()
while 1 :
    menu = print_menu()
    if menu == '1':
    if menu == '2':
    if menu == '3':
    if menu == '4':
    if menu == '5':

    if menu =='0':
        break
