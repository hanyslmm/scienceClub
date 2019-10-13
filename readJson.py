# use of json package
import json

with open('data.json') as json_file:
    data = json.load(json_file)

summaryJson = {}
# this json should answer the following:
# how many teachers you have? **
# how many class you have? **
# how many registered student? **
# how many student pay for sep & oct? **
# what is the percentage for sep & oct? **

staffJson = {}
# how many student she collected in each month
# percentage in each month
# class that is lower than 80%


teachList = list(data.keys())
summaryJson["Teachers_Count"] = len(teachList)
#print(summaryJson)
classList = []
regStudent = 0
augPayment = 0
sepPayment = 0
octPayment = 0
for teach in teachList:
    keys = list(data[teach].keys())
    print (keys)
    classList += keys
    for clas in keys:
        regStudent += data[teach][clas]["SUM"]
        if "Aug" in list(data[teach][clas].keys()):
            augPayment += data[teach][clas]["Aug"]
        if "Sep" in list(data[teach][clas].keys()):
            sepPayment += data[teach][clas]["Sep"]
        if "Oct" in list(data[teach][clas].keys()):
            octPayment += data[teach][clas]["Oct"]

summaryJson["Class_Count"] = len(classList)
summaryJson["Student_Count"] = regStudent
summaryJson["Aug_Count"] = augPayment
summaryJson["Aug_%%"] = round((augPayment/regStudent)*100)
summaryJson["Sep_Count"] = sepPayment
summaryJson["Sep_%%"] = round((sepPayment/regStudent)*100)
summaryJson["Oct_Count"] = octPayment
summaryJson["Oct_%%"] = round((octPayment/regStudent)*100)


print(summaryJson)
#for
