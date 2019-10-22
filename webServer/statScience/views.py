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
    return render(request, "teacher.html", {'summData': summData})

def violation(request, *args, **kwargs):
    print(request.user)
    return render(request, "violation.html", {'summData': summData})
    #return render(request, "summary.html")
