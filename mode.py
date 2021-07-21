from collections import Counter
import csv
with open("data.csv",newline="")as f:
    reader=csv.reader(f)
    filedata=list(reader)

filedata.pop(0)
new_data=[]
for i in range(len(filedata)):
    num=filedata[i][2]
    new_data.append(float(num))


data=Counter(new_data)
mode1={
    "75-85":0,
    "85-95":0,
    "95-105":0,
    "105-115":0,
    "115-125":0,
    "125-135":0,
    "135-145":0,
    "145-155":0,
    "155-165":0,
    "165-175":0,
}
for weight, occurance in data.items():
    if 75<float(weight)<85:
        mode1["75-85"]+=occurance
    elif 85<float(weight)<95:
        mode1["85-95"]+=occurance
    elif 95<float(weight)<105:
        mode1["95-105"]+=occurance 
    elif 105<float(weight)<115:
        mode1["105-115"]+=occurance
    elif 115<float(weight)<125:
        mode1["115-125"]+=occurance
    elif 125<float(weight)<135:
        mode1["125-135"]+=occurance
    elif 135<float(weight)<145:
        mode1["135-145"]+=occurance
    elif 145<float(weight)<155:
        mode1["145-155"]+=occurance
    elif 155<float(weight)<165:
        mode1["155-165"]+=occurance
    elif 165<float(weight)<175:
        mode1["165-175"]+=occurance

mode_range,mode_occurance=0,0
for range,occurance in mode1.items():
    if occurance>mode_occurance:
        mode_range,mode_occurance=[int(range.split("-")[0]),int(range.split("-")[1])],occurance

mode=float((mode_range[0]+mode_range[1])/2)
print(mode)