from tkinter import*
from tkinter import ttk
from EnglishToGujaratiDictionary import eng_to_guj,eng_to_guj2
from EnglishToHindiDictionary import eng_to_hin,eng_to_hin2
from EnglishToMarathiDictionary import eng_to_mara

def translate():
    ip = engVariable.get()
    language = lang.get()
    if(language=="Gujarati"):
        l = list(ip.split(' '))
        translatedList = list()
        for i in l:
            try:
                translatedWord = eng_to_guj[i]
                translatedList.append(translatedWord)
            except:
                lst = []
                i = list(i)
                for j in range(len(i)):
                    lst.append(i[j])
                    try:
                        lst.append(i[j]+i[j+1])
                        lst.append(i[j]+i[j+1]+i[j+2])
                    except:
                        lst.append("a")
                #print(lst)
                for k in lst:
                    try:
                        translatedWord = eng_to_guj2[k]
                        translatedList.append(translatedWord)
                    except:
                        ls1 =[]
        translatedString = ' '.join(translatedList)
        transVariable.set(translatedString)
    elif(language=="Hindi"):
        l = list(ip.split(' '))
        translatedList = list()
        for i in l:
            try:
                translatedWord = eng_to_hin[i]
                translatedList.append(translatedWord)
            except:
                lst1 = []
                i = list(i)
                for j in range(len(i)):
                    lst1.append(i[j])
                    try:
                        lst1.append(i[j]+i[j+1])
                        lst1.append(i[j]+i[j+1]+i[j+2])
                    except:
                        lst1.append("a")
                #print(lst1)
                for k in lst1:
                    try:
                        translatedWord = eng_to_hin2[k]
                        translatedList.append(translatedWord)
                    except:
                        ls1 =[]
        translatedString = ' '.join(translatedList)
        transVariable.set(translatedString)
    elif(language=="Marathi"):
        l = list(ip.split(' '))
        translatedList = list()
        for i in l:
            try:
                translatedWord = eng_to_mara[i]
                translatedList.append(translatedWord)
            except:
                translatedList.append(i)
        translatedString = ' '.join(translatedList)
        transVariable.set(translatedString)

root =Tk()
root.geometry("600x200")
root["bg"]="#20325B"
root.title("Language Translator - DWM Project")
global engVariable
global transVariable
global lang;
engVariable=StringVar()
transVariable=StringVar()
lang=StringVar()
Entry(root,text="Hello",textvariable=engVariable,font="Arial 12",fg="black",width=42).place(x=80,y=30)
fontExample = ("Courier", 12, "bold")
comboExample = ttk.Combobox(root,textvariable=lang,
                            values=[
                                    "Gujarati","Hindi","Marathi"],
                            font = fontExample)

root.option_add('*TCombobox*Listbox.font', fontExample)
comboExample.place(x=80,y=70)

Button(root,text="Translate",font="Arial 12 bold",width="10",command=translate,bg="orange").place(x=350,y=70)
Label(root,text="Translation is",textvariable=transVariable,font="Arial 12",bg="#20325B",fg="white").place(x=80,y=120)
root.mainloop()
