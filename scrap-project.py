from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
page = requests.get(url)
soup = bs(page.text,"html.parser")
startable = soup.find_all("table")
temp_list = []
tablerows = startable[7].find_all("tr")
for a in tablerows:
    td = a.find_all("td")
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

Star_names = []
Distance =[]
Mass = []
Radius =[]

for i in range(1,len(temp_list)):
    Star_names.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][7])
    Radius.append(temp_list[i][8])
df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius)),columns = ["Star_names","Distance","Mass","Radius"])
df2.to_csv("dwarf_stars.csv")