import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.ensemble import RandomForestClassifier

path_csv= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

attributes = ['Runtime', 'Aspect_Ratio', 'Content_Rating_Score', 'Genre_Musical', 'Genre_Romance', 'Genre_Sport', 'Genre_Crime', 'Genre_Documentary', 'Genre_Film-Noir', 'Genre_Short', 'Genre_Fantasy', 'Genre_Horror', 'Genre_Comedy', 'Genre_Western', 'Genre_Thriller', 'Genre_War', 'Genre_Animation', 'Genre_Family', 'Genre_Mystery', 'Genre_Adventure', 'Genre_Drama', 'Genre_History', 'Genre_Biography', 'Genre_Sci-Fi', 'Genre_News', 'Genre_Action', 'Release_Month', 'Director_Avg_Movie_Revenue', 'Lead_Actor_Avg_Movie_Revenue', 'Budget', 'Lead_Actor_Name', 'Director_Name', 'Revenue', 'class']

df = pd.read_csv(path_csv +'/program/real.csv')
#print(df.head())

X = np.array(df.iloc[:,0:30])
y = np.array(df['class'])

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=1/5,random_state=0)


# from sklearn.preprocessing import StandardScaler

# sc = StandardScaler()
# X_train = sc.fit_transform(X_train)
# X_test = sc.transform(X_test)



#Create a Gaussian Classifier
clf=RandomForestClassifier(n_estimators=24, random_state=42,n_jobs=-1)

#Train the model using the training sets y_pred=clf.predict(X_test)
clf.fit(X_train,y_train)

# y_pred=clf.predict(X_test)








if((sys.argv[31])!='0'):
    if((sys.argv[31])=='1'):
        avg_actor = 266
    if((sys.argv[31])=='2'):
        avg_actor = 316
    if((sys.argv[31])=='3'):
        avg_actor = 438
    if((sys.argv[31])=='4'):
        avg_actor = 488
    if((sys.argv[31])=='5'):
        avg_actor = 538


else:
    i=0
    b = sys.argv[29]
    a = np.array(df['Lead_Actor_Name'])
    c = np.array(df['Lead_Actor_Avg_Movie_Revenue'])
    for x in a:
        i=i+1
        if(x==b):
            avg_actor = int(c[i-1])
            break  

#print(avg_actor)2787


if((sys.argv[32])!='0'):
    if((sys.argv[32])=='1'):
        avg_direc = 314
    if((sys.argv[32])=='2'):
        avg_direc = 364
    if((sys.argv[32])=='3'):
        avg_direc = 414
    if((sys.argv[32])=='4'):
        avg_direc = 464
    if((sys.argv[32])=='5'):
        avg_direc = 514

else:
    ii=0
    bi = sys.argv[28]
    ai = np.array(df['Director_Name'])
    ci = np.array(df['Director_Avg_Movie_Revenue'])
    for xi in ai:
        ii=ii+1
        if(xi==bi):
            avg_direc = int(ci[ii-1])
            break
#print(avg_direc)

aaa=sys.argv[27]
iii=int(aaa[5])
jjj=int(aaa[6])
iii=str(((iii*10)+jjj)-1)
#print(iii)


for l in range(4,27):
     if(sys.argv[l]=='None'):
          sys.argv[l]=0
          







test=np.array([[sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7],sys.argv[8],sys.argv[9],sys.argv[10],sys.argv[11],sys.argv[12],sys.argv[13],sys.argv[14],sys.argv[15],sys.argv[16],sys.argv[17],sys.argv[18],sys.argv[19],sys.argv[20],sys.argv[21],sys.argv[22],sys.argv[23],sys.argv[24],sys.argv[25],sys.argv[26],iii,avg_direc,avg_actor,sys.argv[30]]], dtype=float)

pred = clf.predict(test)
output="Rain Hi your input is  %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s and the prediction is %s"%(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7],sys.argv[8],sys.argv[9],sys.argv[10],sys.argv[11],sys.argv[12],sys.argv[13],sys.argv[14],sys.argv[15],sys.argv[16],sys.argv[17],sys.argv[18],sys.argv[19],sys.argv[20],sys.argv[21],sys.argv[22],sys.argv[23],sys.argv[24],sys.argv[25],sys.argv[26],sys.argv[27],sys.argv[28],sys.argv[29],sys.argv[30],pred)
print(output)


# plt.plot(k_value, k_acc_score)
# plt.xlabel("K")
# plt.ylabel("Accuracy")
# plt.show()

# regressor = RandomForestRegressor(n_estimators=20, random_state=0,n_jobs=-1)
# regressor.fit(X_train, y_train)


# pred = regressor.predict(X_test)

# print("accuracy : {}".format(accuracy_score(y_test,y_pred)))


# y_pred = regressor.predict(X_test)


# print(confusion_matrix(y_test,y_pred))
# print(classification_report(y_test,y_pred))
# print(accuracy_score(y_test, y_pred))



# k_value = [i for i in range(1, 100, 2)]
# k_acc_score =[ ]


# for k in k_value:
#      knn = KNeighborsClassifier(n_neighbors=k, n_jobs=-1)
#      cv_scores = cross_val_score(knn,X_train,y_train,cv=5,scoring='accuracy')
#      print(cv_scores)
#      k_acc_score.append(cv_scores.mean())
#      print(cv_scores.mean())

# print(print(cv_scores.mean()))
# optimal_k = k_value[k_acc_score.index(max(k_acc_score))]     

# # print("Our optimal k value is {}".format(optimal_k))
# print(f"Our optimal k value is {optimal_k}")

# knn = KNeighborsClassifier(n_neighbors=11, n_jobs=-1)
# #training

# knn.fit(X_train, y_train)

# print("hello")

# test=np.array([[sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7],sys.argv[8],sys.argv[9],sys.argv[10],sys.argv[11],sys.argv[12],sys.argv[13],sys.argv[14],sys.argv[15],sys.argv[16],sys.argv[17],sys.argv[18],sys.argv[19],sys.argv[20],sys.argv[21],sys.argv[22],sys.argv[23],sys.argv[24],sys.argv[25],sys.argv[26],sys.argv[27],sys.argv[28],sys.argv[29],sys.argv[30]]], dtype=float)
# pred = knn.predict(test)
# output="Hi your input is  %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s and the prediction is %s"%(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7],sys.argv[8],sys.argv[9],sys.argv[10],sys.argv[11],sys.argv[12],sys.argv[13],sys.argv[14],sys.argv[15],sys.argv[16],sys.argv[17],sys.argv[18],sys.argv[19],sys.argv[20],sys.argv[21],sys.argv[22],sys.argv[23],sys.argv[24],sys.argv[25],sys.argv[26],sys.argv[27],sys.argv[28],sys.argv[29],sys.argv[30],pred)
# print(output)


# plt.plot(k_value, k_acc_score)
# plt.xlabel("K")
# plt.ylabel("Accuracy")
# plt.show()


