from django.http import HttpResponse
from django.shortcuts import render
# use of json package
import json


# Create your views here.
def home_view(request, *args, **kwargs):

    print(request.user)
    summDict = {}
    with open('../summaryData.json', 'r') as json_file:
        summData = json.load(json_file)
    return render(request, "home.html", {'summData': summData})


def teacher_view(request, *args, **kwargs):

    print(request.user)
    teacherData = {}
    with open('../teacherData.json', 'r') as json_file:
        teacherData = json.load(json_file)
    return render(request, "teacher.html", {'teacherData': teacherData})


def violation(request, *args, **kwargs):

    print(request.user)
    lostData = {}
    with open('../lostData.json', 'r') as json_file:
        lostData = json.load(json_file)
    return render(request, "violation.html", {'lostData': lostData})
    #return render(request, "summary.html")
