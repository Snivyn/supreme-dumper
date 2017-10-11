import bs4
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from datetime import datetime as dt

print("------------------------------------------------------------------")
print("supreme dumper v1.2")
print("developed by @snivynGOD\n")
print("Outputs current products (name, image, price, stock) on Supreme's")
print("site to a CSV file.")
print("------------------------------------------------------------------\n")


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
info = " [INFO] Creating CSV files..."
print(dt.now().strftime("%H:%M:%S") + info)

export = "products_raw.csv"
csv = open(export, "w")
product_data_csv = "products.csv"
edit_product_data_csv = open(product_data_csv, "w")

info = " [INFO] CSV files created."
print(dt.now().strftime("%H:%M:%S") + info)

# Downloading raw page data
info = " [INFO] Downloading Supreme site data..."
print(dt.now().strftime("%H:%M:%S") + info)

site = "http://www.supremenewyork.com/shop"
download = req(site)
raw_html = download.read()
download.close()

# Parsing data
info = " [INFO] Parsing raw HTML from Supreme..."
print(dt.now().strftime("%H:%M:%S") + info)
parsed_html = soup(raw_html, "html.parser")

# Grabbing product links
info = " [INFO] Grabbing product links from Supreme..."
print(dt.now().strftime("%H:%M:%S") + info)

jackets_raw = parsed_html.findAll("li", {"class": "jackets"})
jackets = parse_products(jackets_raw)
shirts_raw = parsed_html.findAll("li", {"class": "shirts"})
shirts = parse_products(shirts_raw)
tops_sweaters_raw = parsed_html.findAll("li", {"class": "tops/sweaters"})
tops_sweaters = parse_products(tops_sweaters_raw)
sweatshirts_raw = parsed_html.findAll("li", {"class": "sweatshirts"})
sweatshirts = parse_products(sweatshirts_raw)
pants_raw = parsed_html.findAll("li", {"class": "pants"})
pants = parse_products(pants_raw)
tshirts_raw = parsed_html.findAll("li", {"class": "t-shirts"})
tshirts = parse_products(tshirts_raw)
hats_raw = parsed_html.findAll("li", {"class": "hats"})
hats = parse_products(hats_raw)
bags_raw = parsed_html.findAll("li", {"class": "bags"})
bags = parse_products(bags_raw)
accessories_raw = parsed_html.findAll("li", {"class": "accessories"})
accessories = parse_products(accessories_raw)
skate_raw = parsed_html.findAll("li", {"class": "skate"})
skate = parse_products(skate_raw)

info = " [INFO] Received product links from Supreme."
print(dt.now().strftime("%H:%M:%S") + info)
csv.close()

# Reading CSV file and extracting data from product pages
info = " [INFO] Grabbing product info from Supreme..."
print(dt.now().strftime("%H:%M:%S") + info)

with open("products_raw.csv", "r") as csv_load:
    for link in csv_load.readlines():
        product_download = req(link)
        product_raw_html = product_download.read()
        product_download.close()
        product_parsed_html = soup(product_raw_html, "html.parser")

        # Grabbing category, product name, price
        info_raw = product_parsed_html.findAll("div", {"id": "details"})
        category = info_raw[0].h1["data-category"]
        name = info_raw[0].h1.string

        # Formatting name
        name = (str)(name.encode("ascii", "ignore"))
        name = name[2:-1]

        # Grabbing image
        info_raw = product_parsed_html.findAll("img", {"id": "img-main"})
        image = "http:" + info_raw[0]["src"]

        # Grabbing price
        info_raw = product_parsed_html.findAll("p", {"class": "price"})
        price = info_raw[0].string

        # Checking stock status
        try:
            info_raw = product_parsed_html.findAll("form", {"class": "add"})
            info_raw[0] = "Does it exist!?"
            in_stock = "True"
        except:
            in_stock = "False"

        # Output gathered data to CSV file
        info = " [INFO] Product found: " + category + " | " + name + " | "
        info += price + " | In Stock: " + in_stock + " | Image Link: " + image

        print(dt.now().strftime("%H:%M:%S") + info)

        product = link.strip() + "," + category + "," + name + "," + price
        product += "," + in_stock + "," + image + "\n"

        edit_product_data_csv.write(product)

# Closing CSV file
edit_product_data_csv.close()

info = " [INFO] CSV files are now ready for use."
print(dt.now().strftime("%H:%M:%S") + info)
info = " [INFO] All tasks complete."
print(dt.now().strftime("%H:%M:%S") + info)
