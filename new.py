import pdb
import requests
import re
import csv
import pickle

#!/usr/bin/python3.5
# coding: utf-8

url='https://www.footlocker.fr/en/women/shoes/running/'
request_headers={'User-Agent': "(Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6" }

req=requests.get(url,headers=request_headers)
content=req.text


content=content.replace('\n','')
content=content.replace('(','')
content=content.replace(')','')




#donne le lien pour chaque produit
pattern='<a href="(.+?(?="><span itemprop="name">))'
output=re.findall(pattern,content)

for ele in output:
    request_headers=request_headers={'User-Agent': "(Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6" }
    req=requests.get(ele,headers=request_headers)
    new=req.text

#trouver le nom du produit
    
    pattern2='<span itemprop="name">(.+?(?=</span>))'
    produit=re.findall(pattern2,new)

#trouver le prix

    


