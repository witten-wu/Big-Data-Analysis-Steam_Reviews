import re
import jieba
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD


class Filter:
    def invoke(self, data):
        pass


class ReFilter(Filter):
    def __init__(self, pattern):
        self.filter_p = re.compile(pattern)

    def invoke(self, data):
        return re.sub(self.filter_p, "", data)  # 去掉所有特殊字符


class CommentFilter(Filter):
    def __init__(self, userdict):
        if (userdict != None):
            jieba.load_userdict(userdict)

    def invoke(self, data):
        return jieba.cut(data, cut_all=False) # 精确模式


class TokenFilter(Filter):
    def __init__(self, stop_words_path):
        self.stop_words = self.get_stop_words(stop_words_path)

    @staticmethod
    def get_stop_words(path):
        stop_words = set()
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                stop_words.add(line.strip('\n'))
        return stop_words

    def invoke(self, data):
        comment = []
        for word in data:
            if word not in self.stop_words:
                comment.append(word.lower()) # 所有英文小写
        return comment

class VectorFilter(Filter):
    def __init__(self, vec_para):
        self.para = vec_para

    def invoke(self, token):
        '''
        用tfidf将词转换为向量，并保留词名
        '''
        vectorizer = TfidfVectorizer(token_pattern=self.para['token_pattern'], max_features=self.para['max_features'], ngram_range=self.para['ngram_range'])
        X = vectorizer.fit_transform(token)
        terms = vectorizer.get_feature_names()
        return X, terms

class CoordinatesFilter(Filter):
    def __init__(self, lsa_para):
        self.svd_model = TruncatedSVD(n_components=lsa_para['n_components'], algorithm=lsa_para['algorithm'], n_iter=lsa_para['n_iter'], random_state=lsa_para['random_state'])

    def invoke(self, vector):
        '''
        用tfidf将词转换为向量，并保留词名
        '''
        self.svd_model.fit(vector)
        return self.svd_model.fit_transform(vector), self.svd_model.transform(vector).dot(np.linalg.inv(np.diag(self.svd_model.singular_values_)))