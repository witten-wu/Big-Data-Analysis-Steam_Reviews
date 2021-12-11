# 提供一些工具
import pandas as pd
import numpy as np
import umap.umap_ as umap
from matplotlib import pyplot as plt

def read_data(path):
    return pd.read_csv(path)

def umap_paint(X_topics, umap_para):    
    embedding = umap.UMAP(n_neighbors=umap_para['n_neighbors'], min_dist=umap_para['min_dist'], random_state=umap_para['random_state']).fit_transform(X_topics)
    plt.figure(figsize=(7,5))
    plt.scatter(embedding[:, 0], embedding[:, 1], s = 10, edgecolor='none')
    plt.show()

def ouput_topic(terms, components, n):
    '''
    用于输出所有主题前n个重要的词
    '''
    for i, comp in enumerate(components):
        terms_comp = zip(terms, comp)
        sorted_terms = sorted(terms_comp, key=lambda x:x[1], reverse=True)[:n]
        print("Topic "+str(i)+": ")
        for t in sorted_terms:
            print(t[0], end=' ')
        print()
    
def convert_tobit_data(coordinates, data):
    '''
    将数据转换为tobit的输入格式
    '''
    x = pd.DataFrame(coordinates)
    y = pd.Series(data.tolist())
    n_quantiles = 3 # two-thirds of the data is truncated
    quantile = 100/float(n_quantiles)
    lower = np.percentile(y, quantile)
    upper = np.percentile(y, (n_quantiles - 1) * quantile)
    left = y < lower
    right = y > upper
    ns = x.shape[0]
    cens = pd.Series(np.zeros((ns,)))
    cens[left] = -1
    cens[right] = 1
    return x, y, cens

def save_token(save_path, token):
    with open(save_path, 'w') as f:
        for item in token:
            f.write("%s\n" % item)