from bs4 import BeautifulSoup
from flask import Flask, render_template, redirect, url_for
import requests


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'


CHROME_DRIVER_PATH = "C:/Program Files/Google/Chrome/Application"
# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = chrome_options)


productList = []
companyList = []
namesList = []
pricesList = []
item = {}

# PART1 - WEB SCRAPING WITH BEAUTIFUL SOUP

urlOne = "https://www.walmart.com/ip/Soontrans-Laptop-Desk-Bed-Tray-Table-Foldable-Lap-Cup-Slot-Adjustable-Breakfast-Stand-Tablet-Notebook-Eating-Breakfast-Watching-iPad-Books-Couch-Sofa/1191198287?athbdg=L1600&from=/search"
header = {"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0", "Accept-Language": "en-US,en;q=0.5" }

response = requests.get(urlOne, headers=header)
walmart_table_page = response.text


soup = BeautifulSoup(walmart_table_page, "html.parser")

walmart_logo = "static/walmart-logo.jpg"


walmart_table_name = soup.find(name="h1", id="main-title")
walmart_laptop_desk_name = walmart_table_name.getText().split(",")[0]


walmart_table_price = soup.find(name="span", itemprop="price")
walmart_laptop_desk_price = walmart_table_price.getText().split(" ")[1]


walmart_table_img = "static/walmart-laptop-desk.jpg"


productDict = {"Logo": walmart_logo, "Name": walmart_laptop_desk_name, "Price": walmart_laptop_desk_price,"Img": walmart_table_img}
productList.append(productDict)

urlTwo = "https://www.walmart.com/ip/Straight-Talk-Samsung-Galaxy-A14-5G-64GB-Black-Prepaid-Smartphone-Locked-to-Straight-Talk/2311706193?from=/search"
header = {"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0", "Accept-Language": "en-US,en;q=0.5" }

response = requests.get(urlTwo, headers=header)
walmart_phone_page = response.text

soup = BeautifulSoup(walmart_phone_page, "html.parser")

walmart_logo = "static/walmart-logo.jpg"


walmart_phone_name = soup.find(name="h1", id="main-title")
walmart_mobile_phone_name = walmart_phone_name.getText().split(",")[0].split(" ")[2] + " " + walmart_phone_name.getText().split(",")[3].split("-")[1].split("[")[0]


walmart_phone_price = soup.find(name="span", itemprop="price")
walmart_mobile_phone_price = walmart_phone_price.getText().split(" ")[1]


walmart_phone_img = "static/walmart-phone.jpg"

productDict={"Logo": walmart_logo, "Name": walmart_mobile_phone_name,"Price": walmart_mobile_phone_price, "Img": walmart_phone_img}
productList.append(productDict)

urlThree = "https://www.walmart.com/ip/FDW-8-Inch-Queen-Gel-Memory-Foam-Mattress-Fiberglass-Free-Bed-in-a-Box-Comfy-Support/635607345?athbdg=L1600&adsRedirect=true"
header = {"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0", "Accept-Language": "en-US,en;q=0.5" }

response = requests.get(urlThree, headers=header)
walmart_mattress_page = response.text

soup = BeautifulSoup(walmart_mattress_page, "html.parser")

walmart_logo = "static/walmart-logo.jpg"

walmart_mattress_name = soup.find(name="h1", id="main-title")
walmart_memory_foam_mattress_name = walmart_mattress_name.getText().split(" ")[3] + " " + walmart_mattress_name.getText().split(" ")[5] + " " + walmart_mattress_name.getText().split(" ")[6] + " " + walmart_mattress_name.getText().split(" ")[7]

walmart_mattress_price = soup.find(name="span", itemprop="price")
walmart_memory_foam_mattress_price = walmart_mattress_price.getText()

walmart_mattress_img = "static/walmart-mattress.jpg"

productDict = {"Logo": walmart_logo, "Name": walmart_memory_foam_mattress_name, "Price": walmart_memory_foam_mattress_price, "Img": walmart_mattress_img}
productList.append(productDict)


urlFour = "https://www.walmart.com/ip/PowerSmart-Gas-Push-Lawn-Mower-Powered-21-inch-3-in-1-with-144cc-Engine-6-Position-Height-Adjustment/3626501432?athbdg=L1200&from=/search"
header = {"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0", "Accept-Language": "en-US,en;q=0.5" }

response = requests.get(urlFour, headers=header)
walmart_lawnmower_page = response.text

soup = BeautifulSoup(walmart_lawnmower_page, "html.parser")

walmart_logo = "static/walmart-logo.jpg"

walmart_lawnmower_name = soup.find(name="h1", id="main-title")
walmart_lawn_mower_name = walmart_lawnmower_name.getText().split(" ")[0] + " " + walmart_lawnmower_name.getText().split(" ")[2] + " " + walmart_lawnmower_name.getText().split(" ")[3] + " " + walmart_lawnmower_name.getText().split(" ")[4] + " " + walmart_lawnmower_name.getText().split(" ")[5]

walmart_lawnmower_price = soup.find(name="span", itemprop="price")
walmart_lawn_mower_price = walmart_lawnmower_price.getText().split(" ")[0]

walmart_lawnmower_img = "static/walmart-lawnmower.jpg"

productDict = {"Logo": walmart_logo, "Name": walmart_lawn_mower_name, "Price": walmart_lawn_mower_price, "Img": walmart_lawnmower_img}
productList.append(productDict)

urlFive = "https://www.walmart.com/ip/Hamilton-Beach-15-6-cu-Ft-Side-by-side-Stainless-Refrigerator-Freestanding-Installation-HZ8551/2465807248"
header = {"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0", "Accept-Language": "en-US,en;q=0.5" }

response = requests.get(urlFive, headers=header)
walmart_refrigerator_page = response.text

soup = BeautifulSoup(walmart_refrigerator_page, "html.parser")

walmart_logo = "static/walmart-logo.jpg"

walmart_refrigerator_name = soup.find(name="h1", id="main-title")
walmart_fridge_name = walmart_refrigerator_name.getText().split(" ")[0] + " " + walmart_refrigerator_name.getText().split(" ")[1] + " " + walmart_refrigerator_name.getText().split(" ")[8] + " " + walmart_refrigerator_name.getText().split(" ")[9]


walmart_refrigerator_price = soup.find(name="span", itemprop="price")
walmart_fridge_price = walmart_refrigerator_price.getText()

walmart_fridge_img = "static/walmart-fridge.jpg"


productDict = {"Logo": walmart_logo, "Name": walmart_fridge_name, "Price": walmart_fridge_price, "Img": walmart_fridge_img}
productList.append(productDict)

urlSix = "https://www.walmart.com/ip/Famistar-4-Piece-Hardside-Luggage-Suitcase-Set-360-Double-Spinner-Wheels-Integrated-TSA-Lock-14-Travel-Case-20-Carry-On-Luggage-24-Checked-28-Black/3443589199?athbdg=L1900&from=/search"
header = {"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0", "Accept-Language": "en-US,en;q=0.5" }

response = requests.get(urlSix, headers=header)
walmart_luggage_page = response.text

soup = BeautifulSoup(walmart_luggage_page, "html.parser")

walmart_logo = "static/walmart-logo.jpg"

walmart_luggage_name = soup.find(name="h1", id="main-title")
walmart_four_pc_luggage_name = walmart_luggage_name.getText().split(",")[0].split(" ")[0] + " " + walmart_luggage_name.getText().split(",")[0].split(" ")[4] + " " + walmart_luggage_name.getText().split(",")[0].split(" ")[6]

walmart_luggage_price = soup.find(name="span", itemprop="price")
walmart_four_pc_luggage_price = walmart_luggage_price.getText().split(" ")[1]

walmart_luggage_img = "static/walmart-luggage.jpg"


productDict = {"Logo": walmart_logo, "Name": walmart_four_pc_luggage_name, "Price": walmart_four_pc_luggage_price, "Img": walmart_luggage_img}
productList.append(productDict)


urlSeven = "https://www.ebay.com/itm/225886206440?itmmeta=01J0TM4YXRBNJ3BKHVK5E1Q1QG&hash=item3497ddf9e8:g:JGAAAOSwEH5kk9Il&itmprp=enc%3AAQAJAAAA0MiLTXLdUjw%2BEQT7VT5dhMY%2Bv8xBc1cBoLJqufiNcdhbnd53F5sn%2Fkfu83FiA2zysAGq9DhyP0zaYJFoEcSJr5%2BsKKSRg4ZX65zbL2Kos89EJqQUgGR7kKvM%2FeHOZ0S5juekS6wUJyR4x6XM0z7%2F6fSUI75gTsmw0AIT6exNMOh0RkqKzC70ySFwLydBIh9dQs1HPnX0RqA3u7ZvbYYSUsXAMXYL4CdZsdZWrKDVJe4v%2B4Dag1uslGmLG5KdfFbRKFSvHgSuIHzPvkKjnivZZmE%3D%7Ctkp%3ABk9SR4Lvk9SGZA"
header = {"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0", "Accept-Language": "en-US,en;q=0.5" }

response = requests.get(urlSeven, headers=header)
eBay_table_page = response.text

soup = BeautifulSoup(eBay_table_page, "html.parser")

eBay_logo = "static/eBay-logo.jpg"

eBay_table_name = soup.find(name="h1", class_="x-item-title__mainTitle")
eBay_laptop_desk_name = eBay_table_name.getText().split(",")[0]

eBay_table_price = soup.find(name="div", class_="x-price-primary")
eBay_laptop_desk_price = eBay_table_price.getText().split(" ")[1].split("/")[0]

eBay_table_img="static/eBay-laptop-desk.jpg"


productDict = {"Logo": eBay_logo, "Name": eBay_laptop_desk_name, "Price": eBay_laptop_desk_price, "Img": eBay_table_img}
productList.append(productDict)

urlEight = "https://www.ebay.com/itm/145764237548?epid=12047683712&itmmeta=01J0WMC6H0XT3R1KRCJKT10E9T&hash=item21f039c0ec:g:O-QAAOSw4hZmOo6o&itmprp=enc%3AAQAJAAAAsEOZb4LL7DzqQEPmViazg29pWN2eMhML9EF6PRODMBtoAjL05g8fipfvmqhrKZQ35Ju9XZhxUS8aucSwlucqqGYRH2XQNDovAHnSThPB8k%2F6LfmClYLFx1wZsgjVbPP7TEMMzPdKBQCBr1FYKBu0Sj1%2BnwGDNlTcU1dgrzkvchBorVKoS6Kj7%2FrJDjFy2DQ69TzMFPeYgIInq8XhvfZcgYbXrvpyIySbEWhSa6NODBPb%7Ctkp%3ABk9SR8rosJSHZA"
header = {"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0", "Accept-Language": "en-US,en;q=0.5" }

response = requests.get(urlEight, headers=header)
eBay_phone_page = response.text

soup = BeautifulSoup(eBay_phone_page, "html.parser")

eBay_logo = "static/eBay-logo.jpg"

eBay_phone_name = soup.find(name="h1", class_="x-item-title__mainTitle")
eBay_mobile_phone_name = eBay_phone_name.getText().split("-")[0] + " " + eBay_phone_name.getText().split("-")[2]

eBay_phone_price = soup.find(name="div", class_="x-price-primary")
eBay_mobile_phone_price = eBay_phone_price.getText().split(" ")[1]


eBay_phone_img = "static/eBay-phone.jpg"

productDict = {"Logo": eBay_logo, "Name": eBay_mobile_phone_name, "Price": eBay_mobile_phone_price, "Img": eBay_phone_img}
productList.append(productDict)

urlNine = "https://www.ebay.com/itm/362997414367?itmmeta=01J0WK61HJF9DB2B4NHMTQX019&hash=item548454f9df:g:8N4AAOSwV7xj4x~v&itmprp=enc%3AAQAJAAAA8EtvckcXhYoTfpiK7ugQ6vvAV7hUATZEF13ejUWs6MNB6QkMjOIRjMBg7f6j%2BeNIVKh8yb72fDE4HL7XgroM5oqLMRrKZT6yLIgLFXedqR42mCiKTrh7wOdrWL7n2nXXcw%2Fx1k0%2BnHDweB7ubs0OnU10GaX4F9YnG%2B%2FocfNGf7lr3jhQIUSGAnWuEMh91vXAydPP78g3ve8H1Ty2xqaJC6P5XmfAD1L4uvKYCHtrBdoTJ3o5ZR%2F2E%2BP7Yo2EQFjGPeT%2FvJ41oy3SSjbiHCTUOnc%2BfqNuT3PAGovi%2BvHKeBkb%2Fhyc5KzhJRshKbhZtm2nIQ%3D%3D%7Ctkp%3ABFBMtJmYk4dk"
header = {"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0", "Accept-Language": "en-US,en;q=0.5" }

response = requests.get(urlNine, headers=header)
eBay_mattress_page = response.text

soup = BeautifulSoup(eBay_mattress_page, "html.parser")

eBay_logo = "static/eBay-logo.jpg"


eBay_mattress_name = soup.find(name="h1", class_="x-item-title__mainTitle")
eBay_memory_foam_mattress_name = eBay_mattress_name.getText().split(",")[0].split("-")[1].split(" ")[1] + " " + eBay_mattress_name.getText().split(",")[0].split("-")[1].split(" ")[2] + " " + eBay_mattress_name.getText().split(",")[0].split("-")[1].split(" ")[3]


eBay_mattress_price = soup.find(name="div", class_="x-price-primary")
eBay_memory_foam_mattress_price = eBay_mattress_price.getText().split(" ")[1]

eBay_mattress_img="static/eBay-mattress.jpg"


productDict = {"Logo": eBay_logo, "Price": eBay_memory_foam_mattress_price, "Name": eBay_memory_foam_mattress_name, "Img": eBay_mattress_img}
productList.append(productDict)

urlTen = "https://www.ebay.com/itm/204843051793?epid=2325934118&itmmeta=01J0WP001WBZPMYT6RW5QNG2SQ&hash=item2fb198eb11:g:kIAAAOSwFldmXVI-&itmprp=enc%3AAQAJAAAA4G%2Fj6fAp7WNzJjzNsjc25HorfDqpPeNmNl%2FdyD3zI5Pq6OyrSU0OZywqd2580ISebOihjQtmwb%2BIWsob%2BXSMhirMnsbPC2g4YixZIq9uX1m7TsCBRDI4LjQ5zEoo4gxRDONg6cz%2F9IPjfpUYfOhayyTOHn4wuyMhK7q73cpw%2BpS%2BDgfAAAi8uGlBibqlsgWojq%2BYjrxrjX8bmlZWve5mmYsiGg%2Fn%2BP0UbWyOJbPHusuLLW77evw6wALXetCs%2BZbGHOhwl%2B9MCXvrGaY9lykspgDkhh2dH5RGR50yXwUInzHK%7Ctkp%3ABk9SR4SBgJaHZA"
header = {"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0", "Accept-Language": "en-US,en;q=0.5" }

response = requests.get(urlTen, headers=header)
eBay_lawnmower_page = response.text

soup = BeautifulSoup(eBay_lawnmower_page, "html.parser")

eBay_logo = "static/eBay-logo.jpg"


eBay_lawnmower_name = soup.find(name="h1", class_="x-item-title__mainTitle")
eBay_lawn_mower_name = eBay_lawnmower_name.getText().split(" ")[0] + " " + eBay_lawnmower_name.getText().split(" ")[1] + " " + eBay_lawnmower_name.getText().split(" ")[2] + " " + eBay_lawnmower_name.getText().split(" ")[3] + " " + eBay_lawnmower_name.getText().split(" ")[7] + " " + eBay_lawnmower_name.getText().split(" ")[8]


eBay_lawnmower_price = soup.find(name="div", class_="x-price-primary")
eBay_lawn_mower_price = eBay_lawnmower_price.getText().split(" ")[0]


eBay_lawnmower_img="static/eBay-lawnmower.jpg"

productDict = {"Logo": eBay_logo, "Name": eBay_lawn_mower_name, "Price": eBay_lawn_mower_price, "Img": eBay_lawnmower_img}
productList.append(productDict)

urlEleven = "https://www.ebay.com/itm/395010555339?itmmeta=01J0WPPHDH4B5D7HNTYVMNW03Z&hash=item5bf876bdcb:g:ztAAAOSwWFhlWpej&itmprp=enc%3AAQAJAAAA4N3%2FMhCtIuUqA3goRr2ZxCOiMPXB8w4f4i%2Fem2yQm3GW0KobyOU5Q8lvMMpOyFLnt6zaXC1m33kKMfbgujDbsieXsQUPoMPSnuVwOsdeQ1eDhyZmDnB18NLSC7JHOcyR3uJz9yMLsjZrZF0pjngx6g2ICcHQtF8IOndc4TrTO6E6W2kmvO7jEHEei8fIUreqhmQ4zZVay68b943sXFFqjFZXup%2BngBYwrgON7rmPlf2qOWMBSlQdfP4ejLWyixLzDdjF9LGow1J%2FCAiMBKS1glnqDoxEF0M6tpQzOLHydePg%7Ctkp%3ABk9SR-yW2paHZA"
header = {"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0", "Accept-Language": "en-US,en;q=0.5" }

response = requests.get(urlEleven, headers=header)
eBay_refrigerator_page = response.text

soup = BeautifulSoup(eBay_refrigerator_page, "html.parser")

eBay_logo = "static/eBay-logo.jpg"


eBay_refrigerator_name = soup.find(name="h1", class_="x-item-title__mainTitle")
eBay_fridge_name = eBay_refrigerator_name.getText().split(" ")[1] + " " + eBay_refrigerator_name.getText().split(" ")[2] + " " + eBay_refrigerator_name.getText().split(" ")[3] + " " + eBay_refrigerator_name.getText().split(" ")[4] + " " + eBay_refrigerator_name.getText().split(" ")[9]


eBay_refrigerator_price = soup.find(name="div", class_="x-price-primary")
eBay_fridge_price = eBay_refrigerator_price.getText().split(" ")[1]
#print(eBay_fridge_price)

eBay_fridge_img = "static/eBay-fridge.jpg"
#print(eBay_fridge_img)

productDict = {"Logo": eBay_logo, "Name": eBay_fridge_name, "Price": eBay_fridge_price, "Img": eBay_fridge_img}
productList.append(productDict)

urlTwelve = "https://www.ebay.com/itm/334892956025?epid=2255542543&itmmeta=01J0WTK10NYC6VSM5QSD28V59A&hash=item4df92cf979:g:nvUAAOSwrthkdp~L&itmprp=enc%3AAQAJAAAA0PQ3bOsHOLst%2FRDULpY0w9co%2B68oiYN9sAYg8Zh2nh02k9aKt0QpQJtGlpWUgdfapxmm4LkCIwKV3iM9Bvt7xxR0vgaWMyoBrY5u%2BEwh3OTnCVM0GoLXLKMlVRsbmQQwg5N8mLOIWIDh6JW8DK6aXuadahUMIourrWqSrx4inp06L8tVMN9%2BrwAUuFV9n4XC8gqm55eBqiZ%2BfvYHxq6pZVn8eATNjteL%2Bl6280BehHKVEPM%2Fps%2BUJtJSNnwbCr6jN8RsPkE%2BWhMjKSKzTjmtOLU%3D%7Ctkp%3ABk9SR7yQzJqHZA"
header = {"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0", "Accept-Language": "en-US,en;q=0.5" }

response = requests.get(urlTwelve, headers=header)
eBay_luggage_page = response.text

soup = BeautifulSoup(eBay_luggage_page, "html.parser")

eBay_logo = "static/eBay-logo.jpg"


eBay_luggage_name = soup.find(name="h1", class_="x-item-title__mainTitle")
eBay_four_pc_luggage_name = eBay_luggage_name.getText().split(" ")[1] + " " + eBay_luggage_name.getText().split(" ")[2] + " "  + eBay_luggage_name.getText().split(" ")[3] + " " + eBay_luggage_name.getText().split(" ")[4] + " " + eBay_luggage_name.getText().split(" ")[5]


eBay_luggage_price = soup.find(name="div", class_="x-price-primary")
eBay_four_pc_luggage_price = eBay_luggage_price.getText().split(" ")[1]


eBay_luggage_img = "static/eBay-luggage.jpg"

productDict = {"Logo": eBay_logo, "Name": eBay_four_pc_luggage_name, "Price": eBay_four_pc_luggage_price, "Img": eBay_luggage_img}
productList.append(productDict)

urlThirteen = "https://www.amazon.com/EWX-Adjustable-Foldable-Breakfast-Studying/dp/B0CG9J3KWG/ref=sr_1_1_sspa?crid=J2677CXK3U0T&dib=eyJ2IjoiMSJ9.Ha3CAB7udfl_5ZwGqn3O7ti04pxwcWxkhSCjxGeiuoyFigriK_bXRTTPjQsi4skqO57kL_iHtTpQd0LCG83ChExx5hLucPFB4NOQG_w0DNC0UKZCn7IbFPtSHYbgbP8zfHapmVs5Xi6UCSMfnPAmCkC14HnM-q-MsHRZmP5VRKB3osXXdnA1QQAENXeuJbwZRakAfDk0ppsz6VNtGWnCve30gXB1-PgY5MzxUxS4gDuiE96numVPRwF2evT0mI3hKuPIERtp7FP3FxBw2mSVxht8VP-rw7XBr_q5rlTPz-k.C_P_YlnaLIUOWfiMSOygrk79tH6PWcKHA2hFB3Yxqkk&dib_tag=se&keywords=laptop%2Bfoldable%2Bbed%2Btable&qid=1719025442&sprefix=laptop%2Bfoldable%2Bbed%2Btable%2Caps%2C163&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
header = {"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0", "Accept-Language": "en-US,en;q=0.5" }

response = requests.get(urlThirteen, headers=header)
amazon_table_page = response.text

soup = BeautifulSoup(amazon_table_page, "html.parser")

amazon_logo = "static/amazon-logo.jpg"


amazon_table_name = soup.find(name="span", id="productTitle")
amazon_laptop_desk_name = amazon_table_name.getText().split(",")[0]
amazon_laptop_desk_name = amazon_laptop_desk_name.lstrip()

amazon_table_price = soup.find(name="span", class_="a-offscreen")
amazon_laptop_desk_price = amazon_table_price.getText()

amazon_laptop_desk_img="static/amazon-laptop-desk.jpg"


amazon_laptop_desk = soup.find(name="div", class_="imageBlockThumbnailImageGrayOverlay")

productDict = {"Logo": amazon_logo, "Name": amazon_laptop_desk_name, "Price": amazon_laptop_desk_price,"Img": amazon_laptop_desk_img}
productList.append(productDict)

urlFourteen = "https://www.amazon.com/SAMSUNG-Unlocked-Smartphone-Expandable-Security/dp/B0CN1QSH8Q/ref=sr_1_1?crid=2Q0VA8FW8SV5B&dib=eyJ2IjoiMSJ9.appjRMx7PTlrQkQz90VUu0Sr0EV8572Vx-Hl-tc-FfjjMv51D4qB9GwVLmCsjhE69MT8zJ1KVxY872vgiEQXXj7JjPPdU61uRyugC7P5GMASU4plyHMer50qN7Gk8cL-qldXUSzSZBCb1Qs0P6M2FftCMd5xoYejiz1o-C08U43jcKZoQBswRQt2-Ojoq1JuTmtBxj5cYTcYtFEGqP-2N4xKwcPB9Fi8h6MRqEUjEsI.EmKmOD9-J1hYX9kWCZyvFgNprX4AY-sPokgNRGVHgPk&dib_tag=se&keywords=phone&qid=1719026617&sprefix=phone%2Caps%2C190&sr=8-1&th=1"
header = {"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0", "Accept-Language": "en-US,en;q=0.5" }

response = requests.get(urlFourteen, headers=header)
amazon_phone_page = response.text

soup = BeautifulSoup(amazon_phone_page, "html.parser")

amazon_logo = "static/amazon-logo.jpg"

amazon_phone_name = soup.find(name="span", id="productTitle")
amazon_mobile_phone_name = amazon_phone_name.getText().split(",")[0].split(" ")[8] + " " + amazon_phone_name.getText().split(",")[0].split(" ")[9] + " " + amazon_phone_name.getText().split(",")[0].split(" ")[14] + " " + amazon_phone_name.getText().split(",")[0].split(" ")[15]


amazon_phone_price = soup.find(name="span", class_="aok-offscreen")
amazon_mobile_phone_price = amazon_phone_price.getText()


amazon_phone_img="static/amazon-phone.jpg"


amazon_phone_link = soup.find(name="div", class_="imageBlockThumbnailImageGrayOverlay")


productDict = {"Logo": amazon_logo, "Name": amazon_mobile_phone_name, "Price": amazon_mobile_phone_price, "Img": amazon_phone_img}
productList.append(productDict)


urlFifteen = "https://www.amazon.com/Deegari-Mattress-Innerspring-Individual-Isolation/dp/B0CXLNC5XG/ref=sr_1_12_sspa?crid=2VMSQCV6WZW0Q&dib=eyJ2IjoiMSJ9.lbHluN2GmwhhU8UGy0UwyygRiewvge8DJ9DjtnY0IIirufH5yN4P--IWsBcxZr8zYZlP59_OqMQdulun67HOEtVkZduc5H8dbU_2MkOXmJVLu3XDw6reZXN9U-hscZNjNlvMFQE9VCh17GFNe1p9Z-wehKnqKVsGBriqMO31uaed_zwBsCocthPt_9YyJGsfHHu6IOXSnZ_rdU2eCOj-VR1HXk3t3vbd8CNRR6CpuLow5lfFgRiU_ljAHIvmLF9_un3HgUP8g3sKWidBekDp60WX8Z0vj4EVPh5Yc84hvJI.3v2LhiBeKu9mf52gigAm9PmjQvdnnBfFpaBTf63FUxA&dib_tag=se&keywords=memory%2Bfoam%2Bmattress&qid=1719028185&sprefix=memory%2Bfoam%2Bmattress%2Caps%2C168&sr=8-12-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9tdGY&th=1"
header = {"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0", "Accept-Language": "en-US,en;q=0.5" }

response = requests.get(urlFifteen, headers=header)
amazon_mattress_page = response.text

soup = BeautifulSoup(amazon_mattress_page, "html.parser")

amazon_logo = "static/amazon-logo.jpg"


amazon_mattress_name = soup.find(name="span", id="productTitle")
amazon_memory_foam_mattress_name = amazon_mattress_name.getText().split(",")[0]
amazon_memory_foam_mattress_name = amazon_memory_foam_mattress_name.lstrip()


amazon_mattress_price = soup.find(name="span", class_="a-offscreen")
amazon_memory_foam_mattress_price = amazon_mattress_price.getText()


amazon_mattress_img="static/amazon-mattress.jpg"

amazon_mattress_link = soup.find(name="div", class_="imageBlockThumbnailImageGrayOverlay")


productDict = {"Logo": amazon_logo, "Name": amazon_memory_foam_mattress_name,"Price": amazon_memory_foam_mattress_price, "Img": amazon_mattress_img}
productList.append(productDict)

urlSixteen = "https://www.amazon.com/PowerSmart-21-Inch-Versatility-6-Position-Adjustment/dp/B0CB9XSR1S/ref=sr_1_1_sspa?crid=W07V44BHJNWD&dib=eyJ2IjoiMSJ9.p5ExlcGJI3FnTSoO2mKLli1ARpR1JagtjGW1zkhJ40yc-Q9Iur6AEHcbIB9jAsdmpLF8ESDpEKwaFpbJ1dKuJqKGJZcu-0BhdtDlLwibhT9IoK-EmQCz1ajwU9sIOn2H4JdxZAh0zZpshEIQRaq1OHOhtZH9FTO7IFYfZzN6b4SpEu3tBDWDXunhd-0vRUXBmkLG92F0n2EDu9F803EoJ-bRVr37hTyhptCZTzeV6-M.XMb4rdN8hzK9l1FwnRFWS7CgRxv5YdqzuT_xiQpeKrE&dib_tag=se&keywords=lawnmower&qid=1719029020&sprefix=lawnmower%2Caps%2C180&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
header = {"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0", "Accept-Language": "en-US,en;q=0.5" }

response = requests.get(urlSixteen, headers=header)
amazon_lawnmower_page = response.text

soup = BeautifulSoup(amazon_lawnmower_page, "html.parser")

amazon_logo = "static/amazon-logo.jpg"


amazon_lawnmower_name = soup.find(name="span", id="productTitle")
amazon_lawn_mower_name = amazon_lawnmower_name.getText().strip().split(" ")[0] + " " + amazon_lawnmower_name.getText().strip().split(" ")[1] + " " + amazon_lawnmower_name.getText().strip().split(" ")[2] + " " + amazon_lawnmower_name.getText().strip().split(" ")[3] + " " + amazon_lawnmower_name.getText().strip().split(" ")[4]


amazon_lawnmower_price = soup.find(name="span", class_="a-offscreen")
amazon_lawn_mower_price = amazon_lawnmower_price.getText()


amazon_lawnmower_img="static/amazon-lawnmower.jpg"

amazon_lawnmower_link = soup.find(name="div", class_="imageBlockThumbnailImageGrayOverlay")


productDict = {"Logo": amazon_logo, "Name": amazon_lawn_mower_name, "Price": amazon_lawn_mower_price, "Img": amazon_lawnmower_img}
productList.append(productDict)


urlSeventeen = "https://www.amazon.com/Frigidaire-EFR751-Apartment-Refrigerator-Stainless/dp/B088G26FRM/ref=sr_1_4?crid=HPYC7ZDQTWGS&dib=eyJ2IjoiMSJ9.4OQySzyaA7Vl3n7kq5LshAL3iim2c9fnHxS6CrrWP-6pfbASEGqByOQbfc5DcIz89XSuiHDb1FLV2ssOd1p3naIl7jzSduBx7oH-0KAKEQteLc3nBGi0oknQvjjEiKVJmuO23i3JrwoR_iLg3vVFasFh3-IakVtPUdX-Rn6Ie0p9c_87dXwh32Lke1anjWvUV95_SfEsvnVcXAwxLwk7L7BT4a8wWdT0GpfqL1sE-Ys.gGKT3c9makQyzcR21tw2J0pj2OgWdAVCvm3fTC3UThw&dib_tag=se&keywords=refrigerator&qid=1719030682&sprefix=refrigerator%2Caps%2C250&sr=8-4"
header = {"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0", "Accept-Language": "en-US,en;q=0.5" }

response = requests.get(urlSeventeen, headers=header)
amazon_refrigerator_page = response.text

soup = BeautifulSoup(amazon_refrigerator_page, "html.parser")

amazon_logo = "static/amazon-logo.jpg"


amazon_refrigerator_name = soup.find(name="span", id="productTitle")
amazon_fridge_name = amazon_refrigerator_name.getText().strip().split(",")[0].split(" ")[0] + " " + amazon_refrigerator_name.getText().strip().split(",")[1].split(" ")[5] + " " + amazon_refrigerator_name.getText().strip().split(",")[1].split(" ")[6] + " " + amazon_refrigerator_name.getText().strip().split(",")[1].split(" ")[7] + " "  + amazon_refrigerator_name.getText().strip().split(",")[1].split(" ")[8]


amazon_refrigerator_price = soup.find(name="span", class_="a-offscreen")
amazon_fridge_price = amazon_refrigerator_price.getText()

amazon_fridge_img="static/amazon-fridge.jpg"


productDict = {"Logo": amazon_logo, "Name": amazon_fridge_name, "Price": amazon_fridge_price, "Img": amazon_fridge_img}
productList.append(productDict)

urlEighteen = "https://www.amazon.com/SHOWKOO-Luggage-Expandable-Durable-Suitcase/dp/B0B96S8XLR/ref=sr_1_3_sspa?crid=W89QLNVFU11T&dib=eyJ2IjoiMSJ9.rQplfqaOzPlI4NCB936SU9r7I3bH2Haq6WRyXVZQLu3QdQgZfRWFUDWFLe_yo083P-KmCgZbLyRbCbnYzq-Owr2Dd0UOXZjkSKtiU4u3BtT_AE_c0DVLmoh9LEpSaz_9CsDQyx50aqSm3cNrTUkWL5VPYL4e78sSkPqBXImtBwty-492yJ6159zS_Ef9YE9ZtxU0rYtjbxSScf2ob2_Kl9dBghCaoc7Fg2Mi5kDGouDqA_phkeD-UpsMj3dvGpE6pfA7MGp497SEOqg0833uG0QMnfChtluJ4AgYM_qivNM.5ddgReiJshZfOmDtCpWxcXu_4Rkqzkz5_mO8c9EWboc&dib_tag=se&keywords=luggage+set+4+pc&qid=1719032406&sprefix=luggage+set+4+pc%2Caps%2C191&sr=8-3-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
header = {"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0", "Accept-Language": "en-US,en;q=0.5" }

response = requests.get(urlEighteen, headers=header)
amazon_luggage_page = response.text

soup = BeautifulSoup(amazon_luggage_page, "html.parser")

amazon_logo = "static/amazon-logo.jpg"

amazon_luggage_name = soup.find(name="span", id="productTitle")
amazon_four_pc_luggage_name = amazon_luggage_name.getText().strip().split(" ")[0] + " "  + amazon_luggage_name.getText().strip().split(" ")[12] + " " + amazon_luggage_name.getText().strip().split(" ")[13] + " " + amazon_luggage_name.getText().strip().split(" ")[14]  + " " + amazon_luggage_name.getText().strip().split(" ")[15]


amazon_luggage_price = soup.find(name="span", class_="a-offscreen")
amazon_four_pc_luggage_price = amazon_luggage_price.getText()


amazon_luggage_img="static/amazon-luggage.jpg"

amazon_luggage_link="https://m.media-amazon.com/images/G/01/apparel/rcxgs/tile._CB483369110_.gif"


productDict = {"Logo": amazon_logo, "Name": amazon_four_pc_luggage_name, "Price": amazon_four_pc_luggage_price, "Img": amazon_luggage_img}
productList.append(productDict)


@app.route("/")
def home():
    return render_template("index.html", products=productList)


#PART2 - WEBSCRAPING USING SELENIUM
def create_new_list(productList):

    for product in productList:

        if "walmart" in product["Logo"]:
            item["company_name"] = "Walmart"
            item["name"] = product["Name"]
            item["price"] = product["Price"]
            companyList.append(item["company_name"])
            namesList.append(item["name"])
            pricesList.append(item["price"])


        if "eBay" in product["Logo"]:
            item["company_name"] = "eBay"
            item["name"] = product["Name"]
            item["price"] = product["Price"]
            companyList.append(item["company_name"])
            namesList.append(item["name"])
            pricesList.append(item["price"])


        if "amazon" in product["Logo"]:
            item["company_name"] = "Amazon"
            item["name"] = product["Name"]
            item["price"] = product["Price"]
            companyList.append(item["company_name"])
            namesList.append(item["name"])
            pricesList.append(item["price"])

    return companyList, namesList, pricesList


cList, nList, pList = create_new_list(productList)

print(cList)
print(nList)
print(pList)



driver.get(
    "https://docs.google.com/forms/d/e/1FAIpQLSeosFyNwKJy0iABHUGPSNAmKcM0kO-HahJ59QRynmawyNX_EQ/viewform?usp=sf_link")
time.sleep(2)


for n in range(18):
    company_area = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    company_area.send_keys(cList[n])
    name_area = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    name_area.send_keys(nList[n])
    price_area = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_area.send_keys(pList[n])
    submit_btn = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_btn.click()
    print_another_response_btn = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    print_another_response_btn.click()


if __name__ == '__main__':
    app.run(debug=True)
