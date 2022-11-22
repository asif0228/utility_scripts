#!/usr/bin/env python3
# For future: https://stackoverflow.com/questions/60757698/formatting-a-dataframe-into-a-table-stored-as-png-jpeg
from matplotlib import pyplot as plt
import ctypes
import pandas as pd
import datetime
import calendar

def getSchedule():
    return { # November
            8:[
                "Task 1",
                "Task 2"
                ],
            9:[
                "Task 3",
                "Task 4"
                ],
            10:[
                "Task 5"
                ],
            15:[
                "Task 6"
                ],
            20:[
                "Task 7",
                "Task 8"
                ],
            21:[
                "Task 9",
                "Task 10"
                ],
            22:[
                "Task 11",
                "Task 12"
                ],
            27:[
                "Task 13"
                ]
        }

def getTable(year, month):
    schedule = getSchedule();
    r=[[],[]]
    cnt=0
    d = pd.Timestamp(str(year)+'-'+str(month)+'-01')
    for i in range(d.dayofweek+1):
        r[cnt].append("")
        r[cnt+1].append("")
        
    for i in range(1, calendar.monthrange(year, month)[1] + 1):
        if len(r[cnt])>=7:
            cnt+=2
            r.append([])
            r.append([])
        r[cnt].append(i)
        if i in schedule:
            t=""
            for j in schedule[i]:
                t+="\n- "+j
            r[cnt+1].append(t)
        else:
            r[cnt+1].append("")
    for i in range(7-len(r[cnt])):
        r[cnt].append("")
        r[cnt+1].append("")
    return r

def plotTable():
    plt.rcParams["figure.figsize"] = [11, 5]
    plt.rcParams["figure.autolayout"] = True
    fig, ax = plt.subplots(1, 1)
    
    # hide axes
    fig.patch.set_visible(False)
    ax.axis('tight')
    ax.axis('off')
    
    plt.title("Month: "+datetime.datetime.now().strftime("%B"))
    df = pd.DataFrame(getTable(datetime.date.today().year,datetime.date.today().month), columns=["Sunday","Monday","Tuesday","Wednessday","Thursday","Friday","Saturday"])
    table = ax.table(cellText=df.values, colLabels=df.columns, loc='center', cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(7)
    table.scale(1.3,1.8)
    #fig.tight_layout()


def main():
    print("Creating new calander schedule");
    #plt.plot([1, 2, 3], [1, 4, 9])
    plotTable()
    #plt.show()
    plt.savefig('C:/Users/ASUS/Desktop/plan.jpg')
    ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:/Users/ASUS/Desktop/plan.jpg" , 0)

main()
