
from bs4 import BeautifulSoup
import requests
import pandas as pd

url={"gini":"https://worldpopulationreview.com/country-rankings/gini-coefficient-by-country",
     "billionaire":"https://worldpopulationreview.com/country-rankings/billionaires-by-country",
     "education":"https://worldpopulationreview.com/country-rankings/education-spending-by-country",
     "agriculture":"https://worldpopulationreview.com/country-rankings/agricultural-exports-by-country",
     "crime":"https://worldpopulationreview.com/country-rankings/crime-rate-by-country"}

def scrap(url):
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
   return dataset    
   
   
gini=scrap(url["gini"])
print(gini[0])     
gini_data=pd.DataFrame(gini,columns=["empty","Country","Gini coefficient(World_bank)%","DataYear(World_bank)","Gini coefficient(CIA)%","DataYear(CIA)"])
gini_data.to_csv("Gini_data.csv",index=False)

bills_data=scrap(url["billionaire"])
print(bills_data[0])
billionaires=pd.DataFrame(bills_data,columns=["empty","Country","Billionaires2024","Billionaires per Million people","Name","RichestNetworld(Bn)"])
billionaires.to_csv("Billionaire.csv",index=False) 

education=scrap(url["education"])
print(education[0])
edu_data=pd.DataFrame(education,columns=["empty","Country","Spend on Education %","Year","spend per student"])
edu_data.to_csv("education.csv",index=False)

agriculture=scrap(url["agriculture"])
print(agriculture[0])
agriculture_data=pd.DataFrame(agriculture,columns=["empty","Country","Export Commodity(Tonees)","Commodity_Name"])  
agriculture_data.to_csv("agriculture.csv",index=False)


crime=scrap(url["crime"])
print(crime[0])
crime_data=pd.DataFrame(crime,columns=["empty","Country","CrimeIndex%","SafetyIndex%"])  
crime_data.to_csv("crime_data.csv",index=False)

    
