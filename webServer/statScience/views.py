from django.http import HttpResponse
from django.shortcuts import render
# use of json package
import json

with open('summaryData.json') as json_file:
    summData = json.load(json_file)

# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("hello")'list':tasks_new_v_new
    return render(request, "home.html", {'summData': summData})
