import os
import sys
import csv
import requests
import pandas as pd
import numpy as np
from string import Template
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from subprocess import run,PIPE

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))




# Create your views here.
def index(request):
    if request.user.is_anonymous:
        print("Anonamus")
        return redirect("/login")
    return render(request,'index.html')


def loginuser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutuser(request):
    # return HttpResponse("this is homepage")
    logout(request)
    return redirect("/login")

def selectuser(request):
    return render(request, 'select.html')

def datauser1(request):
    return render(request, 'data1.html')

def datauser2(request):
    return render(request, 'data2.html')

def datauser3(request):
    return render(request, 'data3.html')

def datauser4(request):
    return render(request, 'data4.html')

    # return HttpResponse("this is python")

def proguser1(request):
    if request.method=="POST":
        Runtime = request.POST.get('Runtime')
        Aspect_Ratio = request.POST.get('inlineRadioOptions')
        Content_Rating_Score = request.POST.get('inlineRadioOptionss')
        Release_Month = request.POST.get('date')
        Budget = request.POST.get('Budget')
        Lead_Actor_Name = request.POST.get('Lead_Actor_Name')
        Director_Name = request.POST.get('Director_Name')
        new_director = request.POST.get('new_director')
        new_actor = request.POST.get('new_actor')
        Genre_Musical = request.POST.get('Genre_Musical')
        Genre_Romance = request.POST.get('Genre_Romance')
        Genre_Sport = request.POST.get('Genre_Sport')
        Genre_Crime = request.POST.get('Genre_Crime')
        Genre_Documentary = request.POST.get('Genre_Documentary')
        Genre_Film_Noir = request.POST.get('Genre_Film_Noir')
        Genre_Short = request.POST.get('Genre_Short')
        Genre_Fantasy = request.POST.get('Genre_Fantasy')
        Genre_Horror = request.POST.get('Genre_Horror')
        Genre_Comedy = request.POST.get('Genre_Comedy')
        Genre_Western = request.POST.get('Genre_Western')
        Genre_Thriller = request.POST.get('Genre_Thriller')
        Genre_War = request.POST.get('Genre_Warv')
        Genre_Animation = request.POST.get('Genre_Animation')
        Genre_Family = request.POST.get('Genre_Family')
        Genre_Mystery = request.POST.get('Genre_Mystery')
        Genre_Adventure = request.POST.get('Genre_Adventure')
        Genre_Drama = request.POST.get('Genre_Drama')
        Genre_History = request.POST.get('Genre_History')
        Genre_Biography = request.POST.get('Genre_Biography')
        Genre_Sci_Fi = request.POST.get('Genre_Sci_Fi')
        Genre_News = request.POST.get('Genre_News')
        Genre_Action = request.POST.get('Genre_Action')


        # print(sepal_length,sepal_width,petal_length,petal_width)
        # print("###############")
        # print(Runtime, Aspect_Ratio, Content_Rating_Score, type(Genre_Musical), Genre_Romance, Genre_Sport, Genre_Crime, Genre_Documentary, Genre_Film_Noir, Genre_Short, Genre_Fantasy, Genre_Horror, Genre_Comedy, Genre_Western, Genre_Thriller, Genre_War, Genre_Animation, Genre_Family, Genre_Mystery, Genre_Adventure, Genre_Drama, Genre_History, Genre_Biography, Genre_Sci_Fi, Genre_News, Genre_Action, Release_Month, Budget, Lead_Actor_Name, Director_Name)
        # print("################")


        new_actor = str(new_actor)
        new_director = str(new_director)

        Genre_Musical = str(Genre_Musical)
        Genre_Romance = str(Genre_Romance)
        Genre_Sport = str(Genre_Sport)
        Genre_Crime = str(Genre_Crime)
        Genre_Documentary = str(Genre_Documentary)
        Genre_Film_Noir = str(Genre_Film_Noir)
        Genre_Short = str(Genre_Short)
        Genre_Fantasy = str(Genre_Fantasy)
        Genre_Horror = str(Genre_Horror)
        Genre_Comedy = str(Genre_Comedy)
        Genre_Western = str(Genre_Western)
        Genre_Thriller = str(Genre_Thriller)
        Genre_War = str(Genre_War)
        Genre_Animation = str(Genre_Animation)
        Genre_Family = str(Genre_Family)
        Genre_Mystery = str(Genre_Mystery)
        Genre_Adventure = str(Genre_Adventure)
        Genre_Drama = str(Genre_Drama)
        Genre_History = str(Genre_History)
        Genre_Biography = str(Genre_Biography)
        Genre_Sci_Fi = str(Genre_Sci_Fi)
        Genre_News = str(Genre_News)
        Genre_Action = str(Genre_Action)

        out=run([sys.executable,BASE_DIR +'/static/program/knn3.py',str(Runtime),str(Aspect_Ratio), str(Content_Rating_Score), str(Genre_Musical), str(Genre_Romance), str(Genre_Sport), str(Genre_Crime), str(Genre_Documentary), str(Genre_Film_Noir), str(Genre_Short), str(Genre_Fantasy), str(Genre_Horror), str(Genre_Comedy), str(Genre_Western), str(Genre_Thriller), str(Genre_War), str(Genre_Animation), str(Genre_Family), str(Genre_Mystery), str(Genre_Adventure), str(Genre_Drama), str(Genre_History), str(Genre_Biography), str(Genre_Sci_Fi), str(Genre_News), str(Genre_Action), str(Release_Month), str(Director_Name), str(Lead_Actor_Name), str(Budget), str(new_actor), str(new_director)],shell=False,stdout=PIPE)
        arr=out.stdout.decode("utf-8")
        crr=arr[(len(arr))-3]
        crr=int(crr)
        
        if(crr==5):
            ans='Super Hit !!!'
        elif(crr==4):
            ans='Hit !!!'
        elif(crr==3):
            ans='Average !!!'
        elif(crr==2):
            ans='Below Average !!!'
        else:
            ans='Flope'            

        
        


        # return HttpResponse("<h1>%s</h1>" %out.stdout.decode("utf-8"))
        return render(request,'knn.html',{'data1':ans,'data2':crr})
    return HttpResponse("this is python3.0")



def proguser2(request):
    if request.method=="POST":
        Runtime = request.POST.get('Runtime')
        Aspect_Ratio = request.POST.get('inlineRadioOptions')
        Content_Rating_Score = request.POST.get('inlineRadioOptionss')
        Release_Month = request.POST.get('date')
        Budget = request.POST.get('Budget')
        Lead_Actor_Name = request.POST.get('Lead_Actor_Name')
        Director_Name = request.POST.get('Director_Name')
        new_director = request.POST.get('new_director')
        new_actor = request.POST.get('new_actor')        
        Genre_Musical = request.POST.get('Genre_Musical')
        Genre_Romance = request.POST.get('Genre_Romance')
        Genre_Sport = request.POST.get('Genre_Sport')
        Genre_Crime = request.POST.get('Genre_Crime')
        Genre_Documentary = request.POST.get('Genre_Documentary')
        Genre_Film_Noir = request.POST.get('Genre_Film_Noir')
        Genre_Short = request.POST.get('Genre_Short')
        Genre_Fantasy = request.POST.get('Genre_Fantasy')
        Genre_Horror = request.POST.get('Genre_Horror')
        Genre_Comedy = request.POST.get('Genre_Comedy')
        Genre_Western = request.POST.get('Genre_Western')
        Genre_Thriller = request.POST.get('Genre_Thriller')
        Genre_War = request.POST.get('Genre_Warv')
        Genre_Animation = request.POST.get('Genre_Animation')
        Genre_Family = request.POST.get('Genre_Family')
        Genre_Mystery = request.POST.get('Genre_Mystery')
        Genre_Adventure = request.POST.get('Genre_Adventure')
        Genre_Drama = request.POST.get('Genre_Drama')
        Genre_History = request.POST.get('Genre_History')
        Genre_Biography = request.POST.get('Genre_Biography')
        Genre_Sci_Fi = request.POST.get('Genre_Sci_Fi')
        Genre_News = request.POST.get('Genre_News')
        Genre_Action = request.POST.get('Genre_Action')


        # print(sepal_length,sepal_width,petal_length,petal_width)
        # print("###############")
        # print(Runtime, Aspect_Ratio, Content_Rating_Score, type(Genre_Musical), Genre_Romance, Genre_Sport, Genre_Crime, Genre_Documentary, Genre_Film_Noir, Genre_Short, Genre_Fantasy, Genre_Horror, Genre_Comedy, Genre_Western, Genre_Thriller, Genre_War, Genre_Animation, Genre_Family, Genre_Mystery, Genre_Adventure, Genre_Drama, Genre_History, Genre_Biography, Genre_Sci_Fi, Genre_News, Genre_Action, Release_Month, Budget, Lead_Actor_Name, Director_Name)
        # print("################")

        new_actor = str(new_actor)
        new_director = str(new_director)


        Genre_Musical = str(Genre_Musical)
        Genre_Romance = str(Genre_Romance)
        Genre_Sport = str(Genre_Sport)
        Genre_Crime = str(Genre_Crime)
        Genre_Documentary = str(Genre_Documentary)
        Genre_Film_Noir = str(Genre_Film_Noir)
        Genre_Short = str(Genre_Short)
        Genre_Fantasy = str(Genre_Fantasy)
        Genre_Horror = str(Genre_Horror)
        Genre_Comedy = str(Genre_Comedy)
        Genre_Western = str(Genre_Western)
        Genre_Thriller = str(Genre_Thriller)
        Genre_War = str(Genre_War)
        Genre_Animation = str(Genre_Animation)
        Genre_Family = str(Genre_Family)
        Genre_Mystery = str(Genre_Mystery)
        Genre_Adventure = str(Genre_Adventure)
        Genre_Drama = str(Genre_Drama)
        Genre_History = str(Genre_History)
        Genre_Biography = str(Genre_Biography)
        Genre_Sci_Fi = str(Genre_Sci_Fi)
        Genre_News = str(Genre_News)
        Genre_Action = str(Genre_Action)

        out=run([sys.executable,BASE_DIR +'/static/program/rain.py',str(Runtime),str(Aspect_Ratio), str(Content_Rating_Score), str(Genre_Musical), str(Genre_Romance), str(Genre_Sport), str(Genre_Crime), str(Genre_Documentary), str(Genre_Film_Noir), str(Genre_Short), str(Genre_Fantasy), str(Genre_Horror), str(Genre_Comedy), str(Genre_Western), str(Genre_Thriller), str(Genre_War), str(Genre_Animation), str(Genre_Family), str(Genre_Mystery), str(Genre_Adventure), str(Genre_Drama), str(Genre_History), str(Genre_Biography), str(Genre_Sci_Fi), str(Genre_News), str(Genre_Action), str(Release_Month), str(Director_Name), str(Lead_Actor_Name), str(Budget), str(new_actor), str(new_director)],shell=False,stdout=PIPE)
        arr=out.stdout.decode("utf-8")
        crr=arr[(len(arr))-3]
        crr=int(crr)
        
        if(crr==5):
            ans='Super Hit !!!'
        elif(crr==4):
            ans='Hit !!!'
        elif(crr==3):
            ans='Average !!!'
        elif(crr==2):
            ans='Below Average !!!'
        else:
            ans='Flope'            


        # return HttpResponse("<h1>%s</h1>" %out.stdout.decode("utf-8"))
        return render(request,'rand.html',{'data1':ans,'data2':crr})
    return HttpResponse("this is python3.0")
    


def proguser3(request):
    if request.method=="POST":
        Runtime = request.POST.get('Runtime')
        Aspect_Ratio = request.POST.get('inlineRadioOptions')
        Content_Rating_Score = request.POST.get('inlineRadioOptionss')
        Release_Month = request.POST.get('date')
        Budget = request.POST.get('Budget')
        Lead_Actor_Name = request.POST.get('Lead_Actor_Name')
        Director_Name = request.POST.get('Director_Name')
        new_director = request.POST.get('new_director')
        new_actor = request.POST.get('new_actor')
        Genre_Musical = request.POST.get('Genre_Musical')
        Genre_Romance = request.POST.get('Genre_Romance')
        Genre_Sport = request.POST.get('Genre_Sport')
        Genre_Crime = request.POST.get('Genre_Crime')
        Genre_Documentary = request.POST.get('Genre_Documentary')
        Genre_Film_Noir = request.POST.get('Genre_Film_Noir')
        Genre_Short = request.POST.get('Genre_Short')
        Genre_Fantasy = request.POST.get('Genre_Fantasy')
        Genre_Horror = request.POST.get('Genre_Horror')
        Genre_Comedy = request.POST.get('Genre_Comedy')
        Genre_Western = request.POST.get('Genre_Western')
        Genre_Thriller = request.POST.get('Genre_Thriller')
        Genre_War = request.POST.get('Genre_Warv')
        Genre_Animation = request.POST.get('Genre_Animation')
        Genre_Family = request.POST.get('Genre_Family')
        Genre_Mystery = request.POST.get('Genre_Mystery')
        Genre_Adventure = request.POST.get('Genre_Adventure')
        Genre_Drama = request.POST.get('Genre_Drama')
        Genre_History = request.POST.get('Genre_History')
        Genre_Biography = request.POST.get('Genre_Biography')
        Genre_Sci_Fi = request.POST.get('Genre_Sci_Fi')
        Genre_News = request.POST.get('Genre_News')
        Genre_Action = request.POST.get('Genre_Action')


        # print(sepal_length,sepal_width,petal_length,petal_width)
        # print("###############")
        # print(Runtime, Aspect_Ratio, Content_Rating_Score, type(Genre_Musical), Genre_Romance, Genre_Sport, Genre_Crime, Genre_Documentary, Genre_Film_Noir, Genre_Short, Genre_Fantasy, Genre_Horror, Genre_Comedy, Genre_Western, Genre_Thriller, Genre_War, Genre_Animation, Genre_Family, Genre_Mystery, Genre_Adventure, Genre_Drama, Genre_History, Genre_Biography, Genre_Sci_Fi, Genre_News, Genre_Action, Release_Month, Budget, Lead_Actor_Name, Director_Name)
        # print("################")


        new_actor = str(new_actor)
        new_director = str(new_director)

        Genre_Musical = str(Genre_Musical)
        Genre_Romance = str(Genre_Romance)
        Genre_Sport = str(Genre_Sport)
        Genre_Crime = str(Genre_Crime)
        Genre_Documentary = str(Genre_Documentary)
        Genre_Film_Noir = str(Genre_Film_Noir)
        Genre_Short = str(Genre_Short)
        Genre_Fantasy = str(Genre_Fantasy)
        Genre_Horror = str(Genre_Horror)
        Genre_Comedy = str(Genre_Comedy)
        Genre_Western = str(Genre_Western)
        Genre_Thriller = str(Genre_Thriller)
        Genre_War = str(Genre_War)
        Genre_Animation = str(Genre_Animation)
        Genre_Family = str(Genre_Family)
        Genre_Mystery = str(Genre_Mystery)
        Genre_Adventure = str(Genre_Adventure)
        Genre_Drama = str(Genre_Drama)
        Genre_History = str(Genre_History)
        Genre_Biography = str(Genre_Biography)
        Genre_Sci_Fi = str(Genre_Sci_Fi)
        Genre_News = str(Genre_News)
        Genre_Action = str(Genre_Action)

        out=run([sys.executable,BASE_DIR +'/static/program/svm.py',str(Runtime),str(Aspect_Ratio), str(Content_Rating_Score), str(Genre_Musical), str(Genre_Romance), str(Genre_Sport), str(Genre_Crime), str(Genre_Documentary), str(Genre_Film_Noir), str(Genre_Short), str(Genre_Fantasy), str(Genre_Horror), str(Genre_Comedy), str(Genre_Western), str(Genre_Thriller), str(Genre_War), str(Genre_Animation), str(Genre_Family), str(Genre_Mystery), str(Genre_Adventure), str(Genre_Drama), str(Genre_History), str(Genre_Biography), str(Genre_Sci_Fi), str(Genre_News), str(Genre_Action), str(Release_Month), str(Director_Name), str(Lead_Actor_Name), str(Budget), str(new_actor), str(new_director)],shell=False,stdout=PIPE)
        arr=out.stdout.decode("utf-8")
        crr=arr[(len(arr))-3]
        crr=int(crr)
        
        if(crr==5):
            ans='Super Hit !!!'
        elif(crr==4):
            ans='Hit !!!'
        elif(crr==3):
            ans='Average !!!'
        elif(crr==2):
            ans='Below Average !!!'
        else:
            ans='Flope'            

        
        


        # return HttpResponse("<h1>%s</h1>" %out.stdout.decode("utf-8"))
        return render(request,'svm.html',{'data1':ans,'data2':crr})
    return HttpResponse("this is python3.0")






def proguser4(request):
    if request.method=="POST":
        Runtime = request.POST.get('Runtime')
        Aspect_Ratio = request.POST.get('inlineRadioOptions')
        Content_Rating_Score = request.POST.get('inlineRadioOptionss')
        Release_Month = request.POST.get('date')
        Budget = request.POST.get('Budget')
        Lead_Actor_Name = request.POST.get('Lead_Actor_Name')
        Director_Name = request.POST.get('Director_Name')
        new_director = request.POST.get('new_director')
        new_actor = request.POST.get('new_actor')
        Genre_Musical = request.POST.get('Genre_Musical')
        Genre_Romance = request.POST.get('Genre_Romance')
        Genre_Sport = request.POST.get('Genre_Sport')
        Genre_Crime = request.POST.get('Genre_Crime')
        Genre_Documentary = request.POST.get('Genre_Documentary')
        Genre_Film_Noir = request.POST.get('Genre_Film_Noir')
        Genre_Short = request.POST.get('Genre_Short')
        Genre_Fantasy = request.POST.get('Genre_Fantasy')
        Genre_Horror = request.POST.get('Genre_Horror')
        Genre_Comedy = request.POST.get('Genre_Comedy')
        Genre_Western = request.POST.get('Genre_Western')
        Genre_Thriller = request.POST.get('Genre_Thriller')
        Genre_War = request.POST.get('Genre_Warv')
        Genre_Animation = request.POST.get('Genre_Animation')
        Genre_Family = request.POST.get('Genre_Family')
        Genre_Mystery = request.POST.get('Genre_Mystery')
        Genre_Adventure = request.POST.get('Genre_Adventure')
        Genre_Drama = request.POST.get('Genre_Drama')
        Genre_History = request.POST.get('Genre_History')
        Genre_Biography = request.POST.get('Genre_Biography')
        Genre_Sci_Fi = request.POST.get('Genre_Sci_Fi')
        Genre_News = request.POST.get('Genre_News')
        Genre_Action = request.POST.get('Genre_Action')


        # print(sepal_length,sepal_width,petal_length,petal_width)
        # print("###############")
        # print(Runtime, Aspect_Ratio, Content_Rating_Score, type(Genre_Musical), Genre_Romance, Genre_Sport, Genre_Crime, Genre_Documentary, Genre_Film_Noir, Genre_Short, Genre_Fantasy, Genre_Horror, Genre_Comedy, Genre_Western, Genre_Thriller, Genre_War, Genre_Animation, Genre_Family, Genre_Mystery, Genre_Adventure, Genre_Drama, Genre_History, Genre_Biography, Genre_Sci_Fi, Genre_News, Genre_Action, Release_Month, Budget, Lead_Actor_Name, Director_Name)
        # print("################")


        new_actor = str(new_actor)
        new_director = str(new_director)

        Genre_Musical = str(Genre_Musical)
        Genre_Romance = str(Genre_Romance)
        Genre_Sport = str(Genre_Sport)
        Genre_Crime = str(Genre_Crime)
        Genre_Documentary = str(Genre_Documentary)
        Genre_Film_Noir = str(Genre_Film_Noir)
        Genre_Short = str(Genre_Short)
        Genre_Fantasy = str(Genre_Fantasy)
        Genre_Horror = str(Genre_Horror)
        Genre_Comedy = str(Genre_Comedy)
        Genre_Western = str(Genre_Western)
        Genre_Thriller = str(Genre_Thriller)
        Genre_War = str(Genre_War)
        Genre_Animation = str(Genre_Animation)
        Genre_Family = str(Genre_Family)
        Genre_Mystery = str(Genre_Mystery)
        Genre_Adventure = str(Genre_Adventure)
        Genre_Drama = str(Genre_Drama)
        Genre_History = str(Genre_History)
        Genre_Biography = str(Genre_Biography)
        Genre_Sci_Fi = str(Genre_Sci_Fi)
        Genre_News = str(Genre_News)
        Genre_Action = str(Genre_Action)

        out=run([sys.executable,BASE_DIR +'/static/program/social.py',str(Runtime),str(Aspect_Ratio), str(Content_Rating_Score), str(Genre_Musical), str(Genre_Romance), str(Genre_Sport), str(Genre_Crime), str(Genre_Documentary), str(Genre_Film_Noir), str(Genre_Short), str(Genre_Fantasy), str(Genre_Horror), str(Genre_Comedy), str(Genre_Western), str(Genre_Thriller), str(Genre_War), str(Genre_Animation), str(Genre_Family), str(Genre_Mystery), str(Genre_Adventure), str(Genre_Drama), str(Genre_History), str(Genre_Biography), str(Genre_Sci_Fi), str(Genre_News), str(Genre_Action), str(Release_Month), str(Director_Name), str(Lead_Actor_Name), str(Budget), str(new_actor), str(new_director)],shell=False,stdout=PIPE)
        arr=out.stdout.decode("utf-8")
        crr=arr[(len(arr))-3]
        crr=int(crr)
        
        if(crr==5):
            ans='Super Hit !!!'
        elif(crr==4):
            ans='Hit !!!'
        elif(crr==3):
            ans='Average !!!'
        elif(crr==2):
            ans='Below Average !!!'
        else:
            ans='Flope'            

        
        


        # return HttpResponse("<h1>%s</h1>" %out.stdout.decode("utf-8"))
        return render(request,'mean.html',{'data1':ans,'data2':crr})
    return HttpResponse("this is python3.0")







def knn_graphuser(request):
    return render(request, 'knn_graph.html')    

def rand_graphuser(request):
    return render(request, 'rand_graph.html') 


def aboutuser(request):
    return render(request, 'about.html')

def workuser(request):
    return render(request, 'work.html')

def priceuser(request):
    return render(request, 'price.html')

def contactuser(request):
    return render(request, 'contact.html')

def indexuser(request):
    return render(request, 'index.html')

