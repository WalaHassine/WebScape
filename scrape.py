from bs4 import BeautifulSoup  # Importing BeautifulSoup for parsing HTML
from urllib.request import urlopen as uReq  # Importing the urlopen function to open URLs
import csv

url= "https://www.flipkart.com/search?q=samsung+mobiles&amp;sid=tyy%2C4io&amp;as=on&amp;as-show=on&amp;otracker=AS_QueryStore_HistoryAutoSuggest_0_2&amp;otracker1=AS_QueryStore_HistoryAutoSuggest_0_2&amp;as-pos=0&amp;as-type=HISTORY&amp;as-searchtext=sa"
# Opening the URL and reading the HTML content
uClient = uReq(url)
page_html = uClient.read()
uClient.close()
page_soup = BeautifulSoup(page_html, "html.parser") # Parsing (analyse) the HTML content with BeautifulSoup


""""
containers = page_soup.findAll("div", {"class": "tUxRFH"})  # Finding all product containers with the specified class
products = []  # Initializing an empty list to store product data
for container in containers:
    product = {}  # Initializing an empty dictionary for each product
    product["name"] = container.find("a", {"class": "product-item-link"}).text.strip()  # Extracting the product name
    product["price"] = container.find("span", {"class": "price"}).text.strip()  # Extracting the product price
    product["link"] = container.find("a", {"class": "product-item-link"})["href"]  # Extracting the product link
    products.append(product)  # Adding the product dictionary to the products list

    # Printing the list of products
    for product in products:
        print(f"Name: {product['name']}")
        print(f"Price: {product['price']}")
        print(f"Link: {product['link']}")
        print("-" * 40)
        # Closing the URL connection
        print("Scraping completed successfully!")
        uClient.close() """


containers = page_soup.find_all("div", { "class": "tUxRFH"})
print(len(containers))

"print(containers[0].prettify()) #prettify() doesn't take arguments"



#extracting and printing the product name, price, and rating
container = containers[0]
name_tag = container.find(class_="KzDlHZ")
if name_tag:
        print(name_tag.get_text(strip=True))
else:
        print("Name tag with class 'KzDlHZ' not found.")

price = container.find_all("div", {"class": "Nx9bqj _4b5DiR"})
print(price[0].text)


rating = container.find_all("span", {"class": "Wphh3N"})
print(rating[0].text)

#creation of csv file to store all the data (name,price,rating) of the products
filename = "products.csv"
f = open(filename, "w")
headers = "Product_Name, Pricing, Ratings \n"
f.write(headers)

"""for container in containers:
    # Get product name from class 'KzDlHZ'
    name_tag = container.find(class_="KzDlHZ")
    product_name = name_tag.get_text(strip=True) if name_tag else "N/A"

    # Get price
    price_container = container.find_all("div", {"class": "Nx9bqj _4b5DiR"})
    price = price_container[0].get_text(strip=True) if price_container else "N/A"

    # Get rating
    rating_container = container.find_all("span", {"class": "Wphh3N"})
    rating = rating_container[0].get_text(strip=True) if rating_container else "N/A"

    print("Product_Name: " + product_name)
    print("Price: " + price)
    print("Ratings: " + rating)
    print("-" * 40)"""

# Open a CSV file for writing
with open("products.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(["Product_Name", "Price", "Ratings"])

    # Loop through containers and write data
    for container in containers:
        name_tag = container.find(class_="KzDlHZ")
        product_name = name_tag.get_text(strip=True) if name_tag else "N/A"

        price_container = container.find_all("div", {"class": "Nx9bqj _4b5DiR"})
        price = price_container[0].get_text(strip=True) if price_container else "N/A"

        rating_container = container.find_all("span", {"class": "Wphh3N"})
        rating = rating_container[0].get_text(strip=True) if rating_container else "N/A"

        # Write the row to the CSV
        writer.writerow([product_name, price, rating])