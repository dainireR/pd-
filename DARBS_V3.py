import json


import csv



with open("uzd3.json.","r",encoding="utf-8") as datne:
    dati= json.load(datne)
uznemumi=[]
vid_cena=[]
for i in dati:
    uznemumi.append("SIA laiks")
    vid_cena=sum(cenas)/len(cenas)

with open("akciju_analize.csv","w",encoding="utf-8"):





