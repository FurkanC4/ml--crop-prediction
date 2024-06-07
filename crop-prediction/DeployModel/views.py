from django.http import HttpResponse
from django.shortcuts import render
import joblib

def home(request):
   return render(request, 'home.html')


def result(request):
       cls = joblib.load("finall.sav")
       lis = []

       lis.append(request.GET["N"])
       lis.append(request.GET["P"])
       lis.append(request.GET["K"])
       lis.append(request.GET["T"])
       lis.append(request.GET["NEM"])
       lis.append(request.GET["pH"])
       lis.append(request.GET["mm"])
       

      

       ans = cls.predict([lis])
       print(lis)
       print(ans)
       







       return render(request,'result.html',{"ans":ans,"lis":lis})


       


def model(request):
       return render(request, 'model.html')

