import os
import sys
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

path_csv= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

attributes = ['Runtime', 'Aspect_Ratio', 'Content_Rating_Score', 'Genre_Musical', 'Genre_Romance', 'Genre_Sport', 'Genre_Crime', 'Genre_Documentary', 'Genre_Film-Noir', 'Genre_Short', 'Genre_Fantasy', 'Genre_Horror', 'Genre_Comedy', 'Genre_Western', 'Genre_Thriller', 'Genre_War', 'Genre_Animation', 'Genre_Family', 'Genre_Mystery', 'Genre_Adventure', 'Genre_Drama', 'Genre_History', 'Genre_Biography', 'Genre_Sci-Fi', 'Genre_News', 'Genre_Action', 'Release_Month', 'Director_Avg_Movie_Revenue', 'Lead_Actor_Avg_Movie_Revenue', 'Budget', 'Lead_Actor_Name', 'Director_Name', 'Revenue', 'class']

df = pd.read_csv(path_csv +'/program/real.csv')
# print(df.head())

X = np.array(df.iloc[:,0:30])
y = np.array(df['class'])

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=1/5,random_state=42)



svm = SVC(C=10.0,kernel = 'poly',random_state=0)
svm.fit(X_train, y_train)


knn = KNeighborsClassifier(n_neighbors=5, n_jobs=-1)
knn.fit(X_train, y_train)



clf=RandomForestClassifier(n_estimators=24, random_state=42,n_jobs=-1)
clf.fit(X_train,y_train)


# actor ka mamla

if((sys.argv[31])!='0'):
    if((sys.argv[31])=='1'):
        avg_actor1 = 266
    if((sys.argv[31])=='2'):
        avg_actor1 = 316
    if((sys.argv[31])=='3'):
        avg_actor1 = 438
    if((sys.argv[31])=='4'):
        avg_actor1 = 488
    if((sys.argv[31])=='5'):
        avg_actor1 = 538

else:
    i=0
    b = sys.argv[29]
    a = np.array(df['Lead_Actor_Name'])
    c = np.array(df['Lead_Actor_Avg_Movie_Revenue'])
    for x in a:
        i=i+1
        if(x==b):
            avg_actor1 = int(c[i-1])
            break  

# actor insta

hola=sys.argv[33]
bola=int(hola)

if(bola!= 0):
    if(bola<=100):
        avg_actor2 = 266
    elif(bola<=200):
        avg_actor2 = 316
    elif(bola<=500):
        avg_actor2 = 438
    elif(bola<=800):
        avg_actor2 = 488
    elif(bola<=1000):
        avg_actor2 = 538

else:
    avg_actor2=avg_actor1
    


avg_actor = round((avg_actor1 + avg_actor2)/2)
























# director ka mamla


if((sys.argv[32])!='0'):
    if((sys.argv[32])=='1'):
        avg_direc1 = 314
    if((sys.argv[32])=='2'):
        avg_direc1 = 364
    if((sys.argv[32])=='3'):
        avg_direc1 = 414
    if((sys.argv[32])=='4'):
        avg_direc1 = 464
    if((sys.argv[32])=='5'):
        avg_direc1 = 514

else:
    ii=0
    bi = sys.argv[28]
    ai = np.array(df['Director_Name'])
    ci = np.array(df['Director_Avg_Movie_Revenue'])
    for xi in ai:
        ii=ii+1
        if(xi==bi):
            avg_direc1 = int(ci[ii-1])
            break

# director insta

holaa=sys.argv[34]
bolaa=int(holaa)

if(bolaa!= 0):
    if(bolaa<=100):
        avg_direc2 = 314
    elif(bolaa<=200):
        avg_direc2 = 364
    elif(bolaa<=500):
        avg_direc2 = 414
    elif(bolaa<=800):
        avg_direc2 = 464
    elif(bolaa<=1000):
        avg_direc2 = 514

else:
    avg_direc2=avg_direc1
    


avg_direc = round((avg_direc1 + avg_direc2)/2)















#date ka mamla

aaa=sys.argv[27]
iii=int(aaa[5])
jjj=int(aaa[6])
iii=str(((iii*10)+jjj)-1)

#Movie Genre ka mamla

for l in range(4,27):
     if(sys.argv[l]=='None'):
          sys.argv[l]=0
          



test=np.array([[sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7],sys.argv[8],sys.argv[9],sys.argv[10],sys.argv[11],sys.argv[12],sys.argv[13],sys.argv[14],sys.argv[15],sys.argv[16],sys.argv[17],sys.argv[18],sys.argv[19],sys.argv[20],sys.argv[21],sys.argv[22],sys.argv[23],sys.argv[24],sys.argv[25],sys.argv[26],iii,avg_direc,avg_actor,sys.argv[30]]], dtype=float)


pred=[]

pred1 = svm.predict(test)
pred2 = clf.predict(test)
pred3 = clf.predict(test)

x=int(round((int(pred1[0])+int(pred2[0])+int(pred3[0]))/3))
pred.append(x)

output="Hi your input is  %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s and the prediction is %s"%(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7],sys.argv[8],sys.argv[9],sys.argv[10],sys.argv[11],sys.argv[12],sys.argv[13],sys.argv[14],sys.argv[15],sys.argv[16],sys.argv[17],sys.argv[18],sys.argv[19],sys.argv[20],sys.argv[21],sys.argv[22],sys.argv[23],sys.argv[24],sys.argv[25],sys.argv[26],sys.argv[27],sys.argv[28],sys.argv[29],sys.argv[30],pred)
print(output)




