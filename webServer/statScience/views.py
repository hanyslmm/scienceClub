from django.http import HttpResponse
from django.shortcuts import render
# use of json package
import json

summDict = {}
with open('../summaryData.json', 'r') as json_file:
    summData = json.load(json_file)

# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse("hello")#'list':tasks_new_v_new
    print(request.user)
    return render(request, "home.html", {'summData': summData})

def teacher_view(request, *args, **kwargs):
    print(request.user)
    return render(request, "teacher.html")

def summary(request, *args, **kwargs):
    print(request.user)
    return HttpResponse("<h1>Summary Page</h1>")
    #return render(request, "summary.html")
