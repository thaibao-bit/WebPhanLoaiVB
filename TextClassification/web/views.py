from django.shortcuts import render
import pickle
import joblib
from .models import *

from bs4 import BeautifulSoup
import urllib.request
import matplotlib.pyplot as plt
import string
import re


# Create your views here.
def home(request, *args, **kwargs):
    links = Link.objects.all()
    labels = Label.objects.all()
    context = {"links": links, "labels":labels}
    return render(request, "web/home.html", context)

def about(request, *args, **kwargs):
    links = Link.objects.all()
    labels = Label.objects.all()
    context = {"links": links, "labels":labels}
    return render(request, "web/about.html", context)


def text_classification(request, *args , **kwargs):

    context = {}
    output = ""
    links=""
    labels = Label.objects.all()
    if request.method == "POST":
        text = request.POST['data']
        filename = "naive_bayes.pkl"
        loaded_model = joblib.load(filename)
        output = loaded_model.predict([text])
        output = label_by_number(output)
        links = Link.objects.filter(label = output)
        labels = Label.objects.filter(label = output)
    context={"output": output, "labels":labels, "links":links}
    return render(request, "web/index.html", context)


def link_classification(request, *args, **kwargs):
    context = {}
    output = ""
    title = ""
    links = ""
    labels = Label.objects.all()
    if request.method == "POST":
        url = request.POST['link']
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html,"html.parser")
        print("Chu de: ", soup.title)
        title = re.sub('<title.*?>|</title>', "", str(soup.title))
        # Get paragraph content
        getParagraph = soup.find_all("p")
        getParagraph = str(getParagraph)
        txt = re.sub('<p.*?>|</p>', "", str(getParagraph))
        txt = re.sub('<em.*?>|</em>', "", txt)

        text = ""
        for t in txt:
            text = text +t
        # if request.method == "POST":
        # text = request.POST['data']
        filename = "naive_bayes.pkl"
        loaded_model = joblib.load(filename)
        output = loaded_model.predict([text])
        output = label_by_number(output)
        
        link, created = Link.objects.get_or_create(link = url,label = output)
        link.title = title
        print("created == ", created)
        if created == False:
            priority = link.priority
            print("priority == " ,priority)
            link.priority += 1


        try:
            body = soup.find("div", id="main-detail-body")
            image = body.find("img").attrs["src"]
            print("Hinh anh minh hoa: ",image)
            link.imageurl = image
        except:
            print("Some error")
            link.save()
            links = Link.objects.filter(label = output)
            context={"output": output, "title": title, "links":links, "labels":labels}
            return render(request, "web/linkclf.html", context)
        
        
        link.save()
        labels = Label.objects.filter(label = output)
        links = Link.objects.filter(label = output)

    context={"output": output, "title": title, "links":links, "labels":labels}
    
    
       
    return render(request, "web/linkclf.html", context)
def get_by_label(request, label, *args, **kwargs):
    labels = Label.objects.all()
    links = Link.objects.filter(label = label)
    return render(request, "web/bylabel.html", context={"links":links, "labels":labels, "label":label})





def label_by_number(output):
    if output == 16:
        output = "??m nh???c"
    elif output == 17:
        output = "???m th???c"
    elif output == 15:
        output = "Xu???t b???n"
    elif output == 14:
        output = "Xe"
    elif output == 13:
        output = "Th???i trang"
    elif output == 12:
        output = "Th???i s???"
    elif output == 11:
        output = "Th??? thao"
    elif output == 10:
        output = "Th??? gi???i"
    elif output == 9:
        output = "S???c kh???e"
    elif output == 8:
        output = "S???ng tr???"
    elif output == 7:
        output = "Ph??p lu???t"
    elif output == 6:
        output = "Phim ???nh"
    elif output == 5:
        output = "Nh???p s???ng"
    elif output == 4:
        output = "Kinh doanh"
    elif output == 3:
        output = "Gi???i tr??"
    elif output == 2:
        output = "Gi??o d???c"
    elif output == 1:
        output = "Du l???ch"
    else:
        output = "C??ng ngh???"
    return(output)
