# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 18:10:32 2023

@author: wyl
"""
import matplotlib.pyplot as plt
import jieba
import jieba.posseg as pseg
import wordcloud
from collections import Counter

font = r'C:\Windows\Fonts\FZSTK.TTF'
text=[]
word=[]
adj=[]
with open('E:\python\作业\punctuation.txt',encoding='utf-8') as f:
    punc=f.read()
with open('E:\python\作业\weibo.txt','r',encoding='utf-8') as f:
    for line in f:
        temp=f.readline()
        text.append(temp.split('\t')[1])
    for w,f in pseg.cut(line.strip().split('\t')[1]):
        if f=='a':
            adj.append(w)
    for str in text:
        ntext = jieba.lcut(str)
        for i in ntext:
            word.append(i)
    counts={}
    for i in word:
        counts[i]=counts.get(i,0)+1
    for p in punc:
        counts.pop(p,0)
    fre=sorted(counts.items(),key=lambda x:x[1],reverse=True)
    highfre=dict(fre[:50])
    print(highfre)#高频词
    print(fre[-50:])#低频词
#高频词词云图
    wc=wordcloud.WordCloud(font_path=font,background_color='white')
    wc.fit_words(highfre)
    plt.imshow(wc)
    plt.axis("off")
    plt.show()

    
#形容词词云图    
    freq=dict(Counter(adj))
    wc=wordcloud.WordCloud(font_path=font,background_color='white')
    wc.fit_words(freq)
    plt.imshow(wc)
    plt.axis("off")
    plt.show()
    
    
    
 