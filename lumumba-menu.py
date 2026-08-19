import requests
from bs4 import BeautifulSoup

URL = "http://rodzinnagastronomia.pl/menu"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find("div", class_="subpage")
job_elements = results.find_all("section", class_="menu")

for job_element in job_elements:
    tytul = results.find("h1", class_="slide-top")
    zupy = job_element.find("p")
    dania = job_element.find("p", id="last-item")
    #tytul_dania = job_element.find("h2", string="Dania główne")
    #tytul_zupy = job_element.find("h2", string="Zupa dnia")

    print(tytul.text.strip())
    print("Otwarte: pn-pt 11:30-17.00")
    print("-----------------------------")
    print("Zupa dnia:")
    print(zupy.text.strip())
    print("Dania główne:")
    print(dania.text.strip())
    print()
