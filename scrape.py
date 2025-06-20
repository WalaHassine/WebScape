from bs4 import BeautifulSoup  # Importing BeautifulSoup for parsing HTML
from urllib.request import urlopen as uReq  # Importing the urlopen function to open URLs


url= "https://www.flipkart.com/search?q=samsung+mobiles&amp;sid=tyy%2C4io&amp;as=on&amp;as-show=on&amp;otracker=AS_QueryStore_HistoryAutoSuggest_0_2&amp;otracker1=AS_QueryStore_HistoryAutoSuggest_0_2&amp;as-pos=0&amp;as-type=HISTORY&amp;as-searchtext=sa"
# Opening the URL and reading the HTML content
uClient = uReq(url)
page_html = uClient.read()
uClient.close()
page_soup = BeautifulSoup(page_html, "html.parser") # Parsing (analyse) the HTML content with BeautifulSoup


""""
containers = page_soup.findAll("div", {"class": "product-item-info"})  # Finding all product containers with the specified class
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