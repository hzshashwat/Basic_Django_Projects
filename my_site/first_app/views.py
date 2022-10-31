from django.urls import reverse
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def first_app(request):
    return render(request,"first_app/example.html")

def simple_view(request):
    return HttpResponse("SIMPLE VIEW")

articles=   { "sports": "Sports Page",
            "finance": "Finance Page",
            "politics": "Politics Page",
            "international": "International News"
            }

def news_view(request,topic):
    try:
        results=articles[topic]
        return HttpResponse(articles[topic])
    except:
        #return HttpResponseNotFound("This topic isn't available yet.")
        raise Http404("404 : Not Found") # Custom 404.html Template

def num_page_view(request,page_num):
    topic_list = list(articles.keys())
    topic = topic_list[page_num]

    #return HttpResponseRedirect(topic)
    return HttpResponseRedirect(reverse("topic-view",args=[topic]))

def add_view(request,num1,num2):
    result=num1+num2
    show=f"{num1}+{num2}={result}"
    return HttpResponse(show)