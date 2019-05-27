import requests
from bs4 import BeautifulSoup
def news():
    url='https://www.cnbc.com/world/?region=world'
    resp=requests.get(url)
    if resp.status_code==200:
        soup=BeautifulSoup(resp.text,'html.parser')
        l=soup.find("div",{"class":"HeroLedePlusThreeDeck-stories"})
        for i in l.findAll("li"):
            var=i.text
            x=var.replace("span",' ')
            print(x)
    else:
        print("Error,Internet connection is not available")

news()
input("Press enter to exit ;)")
