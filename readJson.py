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

teacherJson = {}
# how many class
# how many students
# how many collected

lostJson = {}
# class that is lower than 50%
# how many students
teachList = list(data.keys())
summaryJson["Teachers_Count"] = len(teachList)
#print(summaryJson)



def summaryJsonFun():

    classList = []
    regStudent = 0
    augPayment = 0
    sepPayment = 0
    octPayment = 0
    for teach in teachList:
        keys = list(data[teach].keys())
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
    summaryJson["Aug_Rate"] = round((augPayment/regStudent)*100)
    summaryJson["Sep_Count"] = sepPayment
    summaryJson["Sep_Rate"] = round((sepPayment/regStudent)*100)
    summaryJson["Oct_Count"] = octPayment
    summaryJson["Oct_Rate"] = round((octPayment/regStudent)*100)

    with open('summaryData.json', 'w') as outfile:
        json.dump(summaryJson, outfile)
    print(summaryJson)

def teacherJsonFun():

    for teach in teachList:
        keys = list(data[teach].keys())
        classCount = len(keys)
        teacherJson[teach] = {}
        teacherJson[teach]["CLASS_COUNT"] = classCount
        teacherJson[teach]["SUM"] = 0
        teacherJson[teach]["AUG"] = 0
        teacherJson[teach]["SEP"] = 0
        teacherJson[teach]["OCT"] = 0
        keys = list(data[teach].keys())
        for clas in keys:
            teacherJson[teach]["SUM"] += data[teach][clas]["SUM"]
            if "Aug" in list(data[teach][clas].keys()):
                teacherJson[teach]["AUG"] += data[teach][clas]["Aug"]
            if "Sep" in list(data[teach][clas].keys()):
                teacherJson[teach]["SEP"] += data[teach][clas]["Sep"]
            if "Oct" in list(data[teach][clas].keys()):
                teacherJson[teach]["OCT"] += data[teach][clas]["Oct"]

    with open('teacherData.json', 'w') as outfile:
        json.dump(teacherJson, outfile)
    print(teacherJson)

def lostJsonFun():

    for teach in teachList:
        keys = list(data[teach].keys())
        lostJson[teach] = {}

        for clas in keys:
            studentSum = data[teach][clas]["SUM"]
            #data[teach][clas]["OCT"]
            if "Oct" in list(data[teach][clas].keys()):
                octPayment = data[teach][clas]["Oct"]
                if (studentSum > 0):
                    classRatio = round((octPayment/studentSum)*100)
                    if (classRatio < 60):
                        lostJson[teach][clas] = {}
                        lostJson[teach][clas]["OCT"] = octPayment
                        lostJson[teach][clas]["RATIO"] = classRatio
                else:
                    lostJson[teach][clas] = "not defined"


    with open('lostData.json', 'w') as outfile:
        json.dump(lostJson, outfile)
    print(lostJson)

lostJsonFun()
teacherJsonFun()
summaryJsonFun()
