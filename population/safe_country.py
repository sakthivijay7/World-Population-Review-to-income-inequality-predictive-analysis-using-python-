from bs4 import BeautifulSoup
import requests
import pandas as pd

url=f"https://worldpopulationreview.com/country-rankings/safest-countries-in-the-world"
response=requests.get(url)
parse=BeautifulSoup(response.text,"lxml")

table=parse.find("table").find("tbody")
table_row=table.find_all("tr")
dataset=[]
try:
    for row in table_row:
        tab_data=row.find_all("td")
        data=[i.text.strip() for i in tab_data]
        dataset.append(data)
except Exception as e:
    print(f"Error fetching{e}")  
print(dataset[0])     
population=pd.DataFrame(dataset,columns=["empty","Country","GlobalPeaceIndex(GPI)2024(1-5)"]) 
population.to_csv("safe_data.csv")   
print(population.head()) 
    
    
