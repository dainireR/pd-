import json


import csv



with open("uzd3.json.","r",encoding="utf-8") as datne:
    dati= json.load(datne)
uznemumi=[]
vid_cena=[]
for i in dati:
    uznemumi.append("SIA laiks")# jābūt atslēgas nosaukumam, lai pievienotu vērtību, i["atslēga"]
    vid_cena=sum(cenas)/len(cenas) #katram uzņēmuma vid jāpievieno sarakstam, vērtības tiek pārrakstītas pa virsu viena otrai

with open("akciju_analize.csv","w",encoding="utf-8"):   # nepievienoji as datne:ir atvērts, bet netiek ierakstīts.





