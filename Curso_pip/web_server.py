import requests
import pandas as pd

def get_categories():
    r=requests.get("https://api.escuelajs.co/api/v1/categories")
    #print(r.statatus_code)

    print(f"status =  {r.status_code}")
    print(f"Texto = {r.text}")
    print(f" tipo = {type(r.text)}")
    categories= r.json()
    print("*-"*15)
    for cate in categories:
        print(cate["name"])