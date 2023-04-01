from matplotlib import pyplot as plt
file1=None


def getTextFile(name):
    global file1
    file1 = open(name, 'r')
    return

def getText():
    return file1.readline()

def saveFile(name,txt):
    csfont = {'fontname':'Times New Roman','size'   : 48}
    plt.title(txt,**csfont)
    plt.savefig(name+'.JPG')
    return

def main():
    
    # Setting
    plt.rcParams["figure.figsize"] = [14,1.7] # width,height
    plt.rcParams["figure.autolayout"] = True
    fig, ax = plt.subplots(1, 1)
    # hide axes
    fig.patch.set_visible(False)
    ax.axis('tight')
    ax.axis('off')
    
    getTextFile("Text_To_Image.txt")
    t=""
    i=1
    while True:
        t = getText()
        if not t:
            return
        t += getText()
        #print(t)
        saveFile(str(i),t.strip())
        i+=1
    
    
    return



main()