print("------------------------------------------------------------------")
print("sharanga supreme dumper v1.1")
print("developed by @snivynGOD")
print("")
print("Outputs current products (name, image, price, stock) on Supreme's"
      + "\nsite to a CSV file.")
print("------------------------------------------------------------------\n")

import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from datetime import datetime as dt

def parse_products(product_class):
    count = 0
    for products in product_class:
        # Grabbing product link
        link = product_class[count].a["href"]
        
        # Adding product link to .csv file
        csv.write("http://www.supremenewyork.com" + link + "\n")
        
        # Incrementing counter for the next product
        count += 1


# Creating .csv file to export product data
print(dt.now().strftime("%H:%M:%S") + " [INFO] Creating CSV files...")
export = "products_raw.csv"
csv = open(export, "w")
product_data_csv = "products.csv"
edit_product_data_csv = open(product_data_csv, "w")
print(dt.now().strftime("%H:%M:%S") + " [INFO] CSV files created.")

# Downloading raw page data
print(dt.now().strftime("%H:%M:%S") + " [INFO] Downloading Supreme site data...")
site = "http://www.supremenewyork.com/shop"
download = req(site)
raw_html = download.read()
download.close()

# Parsing data
print(dt.now().strftime("%H:%M:%S") + " [INFO] Parsing raw html from Supreme...")
parsed_html = soup(raw_html, "html.parser")

# Grabbing products
print(dt.now().strftime("%H:%M:%S") + " [INFO] Grabbing products from Supreme...")
jackets_raw = parsed_html.findAll("li",{"class":"jackets"})
jackets = parse_products(jackets_raw)

shirts_raw = parsed_html.findAll("li",{"class":"shirts"})
shirts = parse_products(shirts_raw)

tops_sweaters_raw = parsed_html.findAll("li",{"class":"tops/sweaters"})
tops_sweaters = parse_products(tops_sweaters_raw)

sweatshirts_raw = parsed_html.findAll("li",{"class":"sweatshirts"})
sweatshirts = parse_products(sweatshirts_raw)

pants_raw = parsed_html.findAll("li",{"class":"pants"})
pants = parse_products(pants_raw)

tshirts_raw = parsed_html.findAll("li",{"class":"t-shirts"})
tshirts = parse_products(tshirts_raw)

hats_raw = parsed_html.findAll("li",{"class":"hats"})
hats = parse_products(hats_raw)

bags_raw = parsed_html.findAll("li",{"class":"bags"})
bags = parse_products(bags_raw)

accessories_raw = parsed_html.findAll("li",{"class":"accessories"})
accessories = parse_products(accessories_raw)

skate_raw = parsed_html.findAll("li",{"class":"skate"})
skate = parse_products(skate_raw)

# Open each site in CSV file
print(dt.now().strftime("%H:%M:%S") + " [INFO] Received product links from Supreme.")
print(dt.now().strftime("%H:%M:%S") + " [INFO] Grabbing product info from Supreme...")

csv.close()

# Reading lines and extracting data
with open("products_raw.csv", "r") as csv_load:
    for link in csv_load.readlines():
        product_download = req(link)
        product_raw_html = product_download.read()
        product_download.close()
        product_parsed_html = soup(product_raw_html, "html.parser")

        # Grabbing category, product name, price
        product_info_raw = product_parsed_html.findAll("div", {"id":"details"})
        category = product_info_raw[0].h1["data-category"]
        name = product_info_raw[0].h1.string
        
        # Formatting name
        name = (str)(name.encode("ascii", "ignore"))
        name = name[2:-1]
        
        # Grabbing image
        product_info_raw = product_parsed_html.findAll("img", {"id":"img-main"})
        image = "http:" + product_info_raw[0]["src"]

        # Grabbing price
        product_info_raw = product_parsed_html.findAll("p", {"class":"price"})
        price = product_info_raw[0].string
    
        # Checking stock status
        try:
            product_info_raw = product_parsed_html.findAll("form", {"class":"add"})
            product_info_raw[0] = "Does it exist!?"
            in_stock = "True"
        except:
            in_stock = "False"
    
    
        # Output product name, image link, and the product link to a new CSV file
        print(dt.now().strftime("%H:%M:%S") + " [INFO] Product found: " + category + " | " + name + " | " + price + " | In Stock: " + in_stock + " | Image Link: " + image) 
        edit_product_data_csv.write(category + "," + name + "," + price + "," + in_stock + "," + image + "\n")

# Closing CSV file
edit_product_data_csv.close()
print(dt.now().strftime("%H:%M:%S") + " [INFO] CSV files are now ready for use.")