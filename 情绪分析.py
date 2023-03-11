# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 14:03:40 2023

@author: wyl
"""
import jieba

import random

#建立jieba情绪词词典
def emotion_dic():
    jieba.load_userdict(r'E:\python\作业\情绪词\anger.txt')
    jieba.load_userdict(r'E:\python\作业\情绪词\joy.txt')
    jieba.load_userdict(r'E:\python\作业\情绪词\sadness.txt')
    jieba.load_userdict(r'E:\python\作业\情绪词\disgust.txt')
    jieba.load_userdict(r'E:\python\作业\情绪词\fear.txt')
    return

emotion_dic()

#导入情绪词库
with open('E:\python\作业\情绪词\\anger.txt',encoding='utf-8') as f:
    anger=f.read()
with open('E:\python\作业\情绪词\\joy.txt',encoding='utf-8') as f:
    joy=f.read()
with open('E:\python\作业\情绪词\\disgust.txt',encoding='utf-8') as f:
    disgust=f.read()
with open('E:\python\作业\情绪词\\sadness.txt',encoding='utf-8') as f:
    sadness=f.read()
with open('E:\python\作业\情绪词\\fear.txt',encoding='utf-8') as f:
    fear=f.read()

#情绪判断函数（混合）
def judge_emotion_mixed(list):
    Sadness=0
    Fear=0
    Anger=0
    Joy=0
    Disgust=0
    for i in list:
        if i in anger:
            Anger+=1
        elif i in joy:
            Joy+=1
        elif i in fear:
            Fear+=1
        elif i in disgust:
            Disgust+=1
        elif i in sadness:
            Sadness+=1
    total=Anger+Joy+Fear+Disgust+Sadness
    if total == 0:
        print('thr emotion is neutral')
    else:
        print('the emotion is {:.2%} anger,{:.2%} joy,{:.2%} fear,{:.2%} sadness,{:.2%} disgust'.format(Anger/total,Joy/total,Fear/total,Sadness/total,Disgust/total))


#情绪判断函数（单一）
def judge_emotion_single(list):
    lis=[]
    dic={'Sadness':0,'Fear':0,'Anger':0,'Joy':0,'Disgust':0}
    for i in list:
        if i in anger:
            dic['Anger']+=1
        elif i in joy:
            dic['Joy']+=1
        elif i in fear:
            dic['Fear']+=1
        elif i in disgust:
            dic['Disgust']+=1
        elif i in sadness:
            dic['Sadness']+=1
    fre=sorted(dic.items(),key=lambda x:x[1],reverse=True)
    if fre[0][1]==0:
#        print('the emotion is neutral')
        return None
    else:
        
        for i in range(5):
            if fre[i][1]==fre[0][1]:
                lis.append(fre[i][0])
                
#        print('the emotion is '+lis[random.randint(1,10000)%len(lis)])
               
        return lis[random.randint(1,10000)%len(lis)]
                
        
#导入停用词
with open ('E:\python\作业\punctuation.txt',encoding='utf-8') as f:
    punc=f.read()

#导入weibo评论内容
with open('E:\python\作业\weibo.txt','r',encoding='utf-8') as f:
    for line in f:
        word=[]
        temp=f.readline()
        temp2=jieba.lcut(temp.split('\t')[1])
        for i in temp2:
            if i not in punc:
                word.append(i)
#        judge_emotion_mixed(word)
        judge_emotion_single(word)
        
        
#情绪时间分布
def time_emotion(int,str):
    week_total=[0,0,0,0,0,0,0]
    hour_total=[0]*24
    week={'Sunday':0,'Monday':0,'Tuesday':0,'Wednesday':0,'Thursday':0,'Friday':0,'Saturday':0}
    hour={'00':0,'01':0,'02':0,'03':0,'04':0,'05':0,'06':0,'07':0,'08':0,'09':0,\
          '10':0,'11':0,'12':0,'13':0,'14':0,'15':0,'16':0,'17':0,'18':0,'19':0,'20':0,'21':0,'22':0,'23':0}
    with open('E:\python\作业\weibo.txt','r',encoding='utf-8') as f:
        for line in f:
            word=[]
            temp=f.readline()
            temp2=jieba.lcut(temp.split('\t')[1])
            for i in temp2:
                if i not in punc:
                    word.append(i)
            emo=judge_emotion_single(word)
#按周划分每天的总评论数
            if (temp.split('\t')[2]).split()[0]=='Sun':
                week_total[0]+=1
            elif (temp.split('\t')[2]).split()[0]=='Mon':
                week_total[1]+=1
            elif (temp.split('\t')[2]).split()[0]=='Tue':
                week_total[2]+=1
            elif (temp.split('\t')[2]).split()[0]=='Wed':
                week_total[3]+=1
            elif (temp.split('\t')[2]).split()[0]=='Thu':
                week_total[4]+=1
            elif (temp.split('\t')[2]).split()[0]=='Fri':
                week_total[5]+=1
            elif (temp.split('\t')[2]).split()[0]=='Sat':
                week_total[6]+=1
#按小时划分每小时评论总数
            if (temp.split('\t')[2].split()[3].split(':')[0])=='00':
                 hour_total[0]+=1
            elif(temp.split('\t')[2].split()[3].split(':')[0])=='01':
                 hour_total[1]+=1
            elif(temp.split('\t')[2].split()[3].split(':')[0])=='02':
                 hour_total[2]+=1
            elif(temp.split('\t')[2].split()[3].split(':')[0])=='03':
                 hour_total[3]+=1
            elif(temp.split('\t')[2].split()[3].split(':')[0])=='04':
                 hour_total[4]+=1
            elif(temp.split('\t')[2].split()[3].split(':')[0])=='05':
                 hour_total[5]+=1
            elif(temp.split('\t')[2].split()[3].split(':')[0])=='06':
                 hour_total[6]+=1
            elif(temp.split('\t')[2].split()[3].split(':')[0])=='07':
                 hour_total[7]+=1
            elif(temp.split('\t')[2].split()[3].split(':')[0])=='08':
                 hour_total[8]+=1
            elif(temp.split('\t')[2].split()[3].split(':')[0])=='09':
                 hour_total[9]+=1
            elif(temp.split('\t')[2].split()[3].split(':')[0])=='10':
                 hour_total[10]+=1
            elif(temp.split('\t')[2].split()[3].split(':')[0])=='11':
                 hour_total[11]+=1
            elif(temp.split('\t')[2].split()[3].split(':')[0])=='12':
                 hour_total[12]+=1
            elif(temp.split('\t')[2].split()[3].split(':')[0])=='13':
                 hour_total[13]+=1
            elif(temp.split('\t')[2].split()[3].split(':')[0])=='14':
                 hour_total[14]+=1
            elif(temp.split('\t')[2].split()[3].split(':')[0])=='15':
                 hour_total[15]+=1
            elif(temp.split('\t')[2].split()[3].split(':')[0])=='16':
                 hour_total[16]+=1
            elif(temp.split('\t')[2].split()[3].split(':')[0])=='17':
                 hour_total[17]+=1
            elif(temp.split('\t')[2].split()[3].split(':')[0])=='18':
                 hour_total[18]+=1
            elif(temp.split('\t')[2].split()[3].split(':')[0])=='19':
                 hour_total[19]+=1
            elif(temp.split('\t')[2].split()[3].split(':')[0])=='20':
                 hour_total[20]+=1
            elif(temp.split('\t')[2].split()[3].split(':')[0])=='21':
                 hour_total[21]+=1
            elif(temp.split('\t')[2].split()[3].split(':')[0])=='22':
                 hour_total[22]+=1
            elif(temp.split('\t')[2].split()[3].split(':')[0])=='23':
                 hour_total[23]+=1
#按周划分每天特定情绪的评论数
            if int==0 and emo==str:
                if (temp.split('\t')[2]).split()[0]=='Sun':
                    week['Sunday']+=1
                elif (temp.split('\t')[2]).split()[0]=='Mon':
                    week['Monday']+=1
                elif (temp.split('\t')[2]).split()[0]=='Tue':
                    week['Tuesday']+=1
                elif (temp.split('\t')[2]).split()[0]=='Wed':
                    week['Wednesday']+=1
                elif (temp.split('\t')[2]).split()[0]=='Thu':
                    week['Thursday']+=1
                elif (temp.split('\t')[2]).split()[0]=='Fri':
                    week['Friday']+=1
                elif (temp.split('\t')[2]).split()[0]=='Sat':
                    week['Saturday']+=1
             
                

            elif int==1 and emo==str:
                if (temp.split('\t')[2].split()[3].split(':')[0])=='00':
                    hour['00']+=1
                elif(temp.split('\t')[2].split()[3].split(':')[0])=='01':
                    hour['01']+=1
                elif(temp.split('\t')[2].split()[3].split(':')[0])=='02':
                    hour['02']+=1
                elif(temp.split('\t')[2].split()[3].split(':')[0])=='03':
                    hour['03']+=1
                elif(temp.split('\t')[2].split()[3].split(':')[0])=='04':
                    hour['04']+=1
                elif(temp.split('\t')[2].split()[3].split(':')[0])=='05':
                    hour['05']+=1
                elif(temp.split('\t')[2].split()[3].split(':')[0])=='06':
                    hour['06']+=1
                elif(temp.split('\t')[2].split()[3].split(':')[0])=='07':
                    hour['07']+=1
                elif(temp.split('\t')[2].split()[3].split(':')[0])=='08':
                    hour['08']+=1
                elif(temp.split('\t')[2].split()[3].split(':')[0])=='09':
                    hour['09']+=1
                elif(temp.split('\t')[2].split()[3].split(':')[0])=='10':
                    hour['10']+=1
                elif(temp.split('\t')[2].split()[3].split(':')[0])=='11':
                    hour['11']+=1
                elif(temp.split('\t')[2].split()[3].split(':')[0])=='12':
                    hour['12']+=1
                elif(temp.split('\t')[2].split()[3].split(':')[0])=='13':
                    hour['13']+=1
                elif(temp.split('\t')[2].split()[3].split(':')[0])=='14':
                    hour['14']+=1
                elif(temp.split('\t')[2].split()[3].split(':')[0])=='15':
                    hour['15']+=1
                elif(temp.split('\t')[2].split()[3].split(':')[0])=='16':
                    hour['16']+=1
                elif(temp.split('\t')[2].split()[3].split(':')[0])=='17':
                    hour['17']+=1
                elif(temp.split('\t')[2].split()[3].split(':')[0])=='18':
                    hour['18']+=1
                elif(temp.split('\t')[2].split()[3].split(':')[0])=='19':
                    hour['19']+=1
                elif(temp.split('\t')[2].split()[3].split(':')[0])=='20':
                    hour['20']+=1
                elif(temp.split('\t')[2].split()[3].split(':')[0])=='21':
                    hour['21']+=1
                elif(temp.split('\t')[2].split()[3].split(':')[0])=='22':
                    hour['22']+=1
                elif(temp.split('\t')[2].split()[3].split(':')[0])=='23':
                    hour['23']+=1
    if int==0:
        lis1=[]
        lis2=[]
        for i in week.values():
            lis1.append(i)
        for i in week.keys():
            lis2.append(i)
        for p in range(7):
            print(lis2[p]+' {:.2%} '.format(lis1[p]/week_total[p]))            
    elif int ==1:
        lis3=[]
        lis4=[]
        for i in hour.values():
            lis3.append(i)
        for i in hour.keys():
            lis4.append(i)
        for p in range(24):
            print(lis4[p]+' {:.2%} '.format(lis3[p]/hour_total[p]))
time_emotion(0,'Anger')                